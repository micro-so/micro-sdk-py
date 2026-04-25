# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro import Micro, AsyncMicro

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGrant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_grant(self, client: Micro) -> None:
        grant = client.prism.grant.retrieve_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_grant(self, client: Micro) -> None:
        response = client.prism.grant.with_raw_response.retrieve_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_grant(self, client: Micro) -> None:
        with client.prism.grant.with_streaming_response.retrieve_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert grant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_grant(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.prism.grant.with_raw_response.retrieve_grant(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_grant(self, client: Micro) -> None:
        grant = client.prism.grant.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_grant_with_all_params(self, client: Micro) -> None:
        grant = client.prism.grant.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
            team_group_id=[{"foo": "a"}],
            body_team_id={"foo": "a"},
            user_id=[{"foo": "a"}],
        )
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_grant(self, client: Micro) -> None:
        response = client.prism.grant.with_raw_response.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_grant(self, client: Micro) -> None:
        with client.prism.grant.with_streaming_response.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert grant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_grant(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.prism.grant.with_raw_response.update_grant(
                object_id="",
                object_type="deal",
            )


class TestAsyncGrant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_grant(self, async_client: AsyncMicro) -> None:
        grant = await async_client.prism.grant.retrieve_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_grant(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.grant.with_raw_response.retrieve_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_grant(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.grant.with_streaming_response.retrieve_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert grant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_grant(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.prism.grant.with_raw_response.retrieve_grant(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_grant(self, async_client: AsyncMicro) -> None:
        grant = await async_client.prism.grant.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_grant_with_all_params(self, async_client: AsyncMicro) -> None:
        grant = await async_client.prism.grant.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
            team_group_id=[{"foo": "a"}],
            body_team_id={"foo": "a"},
            user_id=[{"foo": "a"}],
        )
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_grant(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.grant.with_raw_response.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert grant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_grant(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.grant.with_streaming_response.update_grant(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert grant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_grant(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.prism.grant.with_raw_response.update_grant(
                object_id="",
                object_type="deal",
            )
