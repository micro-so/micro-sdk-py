# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro.types.prism import MetadataPropertiesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_properties(self, client: Micro) -> None:
        metadata = client.prism.metadata.properties(
            object_type="deal",
        )
        assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_properties_with_all_params(self, client: Micro) -> None:
        metadata = client.prism.metadata.properties(
            object_type="deal",
            autofill=True,
            crm_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            term="term",
        )
        assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_properties(self, client: Micro) -> None:
        response = client.prism.metadata.with_raw_response.properties(
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_properties(self, client: Micro) -> None:
        with client.prism.metadata.with_streaming_response.properties(
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_properties(self, async_client: AsyncMicro) -> None:
        metadata = await async_client.prism.metadata.properties(
            object_type="deal",
        )
        assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_properties_with_all_params(self, async_client: AsyncMicro) -> None:
        metadata = await async_client.prism.metadata.properties(
            object_type="deal",
            autofill=True,
            crm_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            term="term",
        )
        assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_properties(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.metadata.with_raw_response.properties(
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_properties(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.metadata.with_streaming_response.properties(
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(MetadataPropertiesResponse, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True
