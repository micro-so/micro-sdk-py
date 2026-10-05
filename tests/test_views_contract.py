"""Keep the published views API usable when regenerating a release."""

import httpx

from micro_so import Micro, AsyncMicro
from micro_so.types.view_get_response import ViewBundle


def view_transport(request: httpx.Request) -> httpx.Response:
    assert request.headers["x-api-key"] == "test-key"
    assert request.url.path.startswith("/v2/prism/test-team/document/views/view-id")
    if request.url.path.endswith("/records"):
        assert request.url.params["cursor"] == "next-page"
        return httpx.Response(200, json={"data": [{"id": "record-id"}], "has_more": False, "next_cursor": None})
    return httpx.Response(200, json={"id": "view-id", "name": "Documents", "view_type": "table"})


def test_views_sync_contract() -> None:
    with Micro(
        api_key="test-key",
        team_id="test-team",
        base_url="https://micro.test",
        http_client=httpx.Client(transport=httpx.MockTransport(view_transport)),
    ) as client:
        view = client.views.get("view-id", view_object_type="document")
        assert isinstance(view, ViewBundle)
        assert view.id == "view-id"
        page = client.views.records.list("view-id", view_object_type="document", cursor="next-page")
        assert page.data == [{"id": "record-id"}]
        assert not page.has_more
        assert page.next_cursor is None


async def test_views_async_contract() -> None:
    async with AsyncMicro(
        api_key="test-key",
        team_id="test-team",
        base_url="https://micro.test",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(view_transport)),
    ) as client:
        view = await client.views.get("view-id", view_object_type="document")
        assert isinstance(view, ViewBundle)
        assert view.id == "view-id"
        page = await client.views.records.list("view-id", view_object_type="document", cursor="next-page")
        assert page.data == [{"id": "record-id"}]
        assert not page.has_more
        assert page.next_cursor is None
