"""Transport failures must not repeat writes unless explicitly requested."""

from typing import Optional

import httpx
import pytest

from micro_so import Micro, AsyncMicro, APIConnectionError, InternalServerError
from micro_so._models import FinalRequestOptions


def no_delay(*_args: object) -> float:
    return 0


@pytest.mark.parametrize("failure", ["status", "transport"])
@pytest.mark.parametrize(
    "method,path,explicit,expected",
    [
        ("POST", "/v2/prism/team/document", None, 1),
        ("PATCH", "/v2/prism/team/document/id", None, 1),
        ("DELETE", "/v2/prism/team/document/id", None, 1),
        ("POST", "/v2/webhooks/team", None, 1),
        ("POST", "/v2/prism/team/document/query/extra", None, 1),
        ("GET", "/v2/prism/team/document", None, 2),
        ("GET", "/v2/prism/team/document", 0, 1),
        ("POST", "/v2/prism/team/document/query", None, 2),
        ("POST", "/v2/prism/query/team/document", None, 2),
        ("POST", "/v2/prism/team/document", 1, 2),
    ],
)
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retry_safety(
    failure: str,
    method: str,
    path: str,
    explicit: Optional[int],
    expected: int,
    asynchronous: bool,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    attempts = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1 and failure == "transport":
            raise httpx.ReadError("connection lost after send", request=request)
        return httpx.Response(
            500 if attempts == 1 else 200,
            headers={"x-should-retry": "true", "retry-after": "0"},
            json={},
        )

    options = FinalRequestOptions.construct(
        method=method,
        url=path,
        json_data={"value": "test"},
        headers={"Idempotency-Key": "operation-id"},
    )
    if explicit is not None:
        options.max_retries = explicit
    if asynchronous:
        async with AsyncMicro(
            api_key="test",
            team_id="team",
            max_retries=1,
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
        ) as client:
            monkeypatch.setattr(client, "_calculate_retry_timeout", no_delay)
            if expected == 1:
                with pytest.raises((APIConnectionError, InternalServerError)):
                    await client.request(httpx.Response, options)
            else:
                await client.request(httpx.Response, options)
    else:
        with Micro(
            api_key="test",
            team_id="team",
            max_retries=1,
            http_client=httpx.Client(transport=httpx.MockTransport(handle)),
        ) as sync_client:
            monkeypatch.setattr(sync_client, "_calculate_retry_timeout", no_delay)
            if expected == 1:
                with pytest.raises((APIConnectionError, InternalServerError)):
                    sync_client.request(httpx.Response, options)
            else:
                sync_client.request(httpx.Response, options)
    assert attempts == expected
