# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types.prism import (
    PropertyListResponse,
    PropertyListAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Micro) -> None:
        property = client.prism.properties.list(
            object_type="comment",
        )
        assert_matches_type(PropertyListResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Micro) -> None:
        property = client.prism.properties.list(
            object_type="comment",
            autofill=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            term="term",
        )
        assert_matches_type(PropertyListResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Micro) -> None:
        response = client.prism.properties.with_raw_response.list(
            object_type="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(PropertyListResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Micro) -> None:
        with client.prism.properties.with_streaming_response.list(
            object_type="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(PropertyListResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all(self, client: Micro) -> None:
        property = client.prism.properties.list_all()
        assert_matches_type(PropertyListAllResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all_with_all_params(self, client: Micro) -> None:
        property = client.prism.properties.list_all(
            autofill=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            term="term",
        )
        assert_matches_type(PropertyListAllResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_all(self, client: Micro) -> None:
        response = client.prism.properties.with_raw_response.list_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(PropertyListAllResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_all(self, client: Micro) -> None:
        with client.prism.properties.with_streaming_response.list_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(PropertyListAllResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProperties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.list(
            object_type="comment",
        )
        assert_matches_type(PropertyListResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.list(
            object_type="comment",
            autofill=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            term="term",
        )
        assert_matches_type(PropertyListResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.with_raw_response.list(
            object_type="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(PropertyListResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.with_streaming_response.list(
            object_type="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(PropertyListResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.list_all()
        assert_matches_type(PropertyListAllResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all_with_all_params(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.list_all(
            autofill=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            term="term",
        )
        assert_matches_type(PropertyListAllResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_all(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.with_raw_response.list_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(PropertyListAllResponse, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_all(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.with_streaming_response.list_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(PropertyListAllResponse, property, path=["response"])

        assert cast(Any, response.is_closed) is True
