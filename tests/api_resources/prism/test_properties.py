# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types.prism import (
    PropertyDefinition,
    PropertyListResponse,
    PropertyListAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        property = client.prism.properties.create(
            object_type="comment",
            name="name",
            type="num",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        property = client.prism.properties.create(
            object_type="comment",
            name="name",
            type="num",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            options=[
                {
                    "value": "value",
                    "color_scheme": "color_scheme",
                    "description": "description",
                    "icon": "icon",
                    "option_group": "option_group",
                    "slug": "slug",
                    "sort_index": 0,
                }
            ],
            required=True,
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
            idempotency_key="x",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.prism.properties.with_raw_response.create(
            object_type="comment",
            name="name",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.prism.properties.with_streaming_response.create(
            object_type="comment",
            name="name",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(PropertyDefinition, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        property = client.prism.properties.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        property = client.prism.properties.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
            enabled=True,
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            required=True,
            idempotency_key="x",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.prism.properties.with_raw_response.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.prism.properties.with_streaming_response.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(PropertyDefinition, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.prism.properties.with_raw_response.update(
                property_id="",
                object_type="comment",
                type="num",
            )

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
            include_options="true",
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
    def test_method_delete(self, client: Micro) -> None:
        property = client.prism.properties.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Micro) -> None:
        property = client.prism.properties.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.prism.properties.with_raw_response.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.prism.properties.with_streaming_response.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.prism.properties.with_raw_response.delete(
                property_id="",
                object_type="comment",
                type="num",
            )

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
            include_options="true",
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
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.create(
            object_type="comment",
            name="name",
            type="num",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.create(
            object_type="comment",
            name="name",
            type="num",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            options=[
                {
                    "value": "value",
                    "color_scheme": "color_scheme",
                    "description": "description",
                    "icon": "icon",
                    "option_group": "option_group",
                    "slug": "slug",
                    "sort_index": 0,
                }
            ],
            required=True,
            role_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            slug="slug",
            idempotency_key="x",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.with_raw_response.create(
            object_type="comment",
            name="name",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.with_streaming_response.create(
            object_type="comment",
            name="name",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(PropertyDefinition, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
            enabled=True,
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            required=True,
            idempotency_key="x",
        )
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.with_raw_response.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(PropertyDefinition, property, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.with_streaming_response.update(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(PropertyDefinition, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.prism.properties.with_raw_response.update(
                property_id="",
                object_type="comment",
                type="num",
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
            include_options="true",
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
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMicro) -> None:
        property = await async_client.prism.properties.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.with_raw_response.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert property is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.with_streaming_response.delete(
            property_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.prism.properties.with_raw_response.delete(
                property_id="",
                object_type="comment",
                type="num",
            )

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
            include_options="true",
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
