# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro.types.prism.objects.deals import GrantGetResponse, GrantUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGrant:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        grant = client.prism.objects.deals.grant.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GrantUpdateResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        grant = client.prism.objects.deals.grant.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_group_id=[{"foo": "a"}],
            body_team_id={"foo": "a"},
            user_id=[{"foo": "a"}],
        )
        assert_matches_type(GrantUpdateResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.prism.objects.deals.grant.with_raw_response.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(GrantUpdateResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.prism.objects.deals.grant.with_streaming_response.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(GrantUpdateResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            client.prism.objects.deals.grant.with_raw_response.update(
                deal_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Micro) -> None:
        grant = client.prism.objects.deals.grant.get(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GrantGetResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Micro) -> None:
        response = client.prism.objects.deals.grant.with_raw_response.get(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = response.parse()
        assert_matches_type(GrantGetResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Micro) -> None:
        with client.prism.objects.deals.grant.with_streaming_response.get(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = response.parse()
            assert_matches_type(GrantGetResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            client.prism.objects.deals.grant.with_raw_response.get(
                deal_id="",
            )


class TestAsyncGrant:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        grant = await async_client.prism.objects.deals.grant.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GrantUpdateResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        grant = await async_client.prism.objects.deals.grant.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_group_id=[{"foo": "a"}],
            body_team_id={"foo": "a"},
            user_id=[{"foo": "a"}],
        )
        assert_matches_type(GrantUpdateResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.deals.grant.with_raw_response.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(GrantUpdateResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.deals.grant.with_streaming_response.update(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(GrantUpdateResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            await async_client.prism.objects.deals.grant.with_raw_response.update(
                deal_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMicro) -> None:
        grant = await async_client.prism.objects.deals.grant.get(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GrantGetResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.deals.grant.with_raw_response.get(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        grant = await response.parse()
        assert_matches_type(GrantGetResponse, grant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.deals.grant.with_streaming_response.get(
            deal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            grant = await response.parse()
            assert_matches_type(GrantGetResponse, grant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            await async_client.prism.objects.deals.grant.with_raw_response.get(
                deal_id="",
            )
