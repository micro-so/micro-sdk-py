# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types.prism.properties import (
    PropertyOption,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        option = client.prism.properties.options.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        option = client.prism.properties.options.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
            color_scheme="color_scheme",
            description="description",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            option_group="option_group",
            slug="slug",
            sort_index=0,
            idempotency_key="x",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.prism.properties.options.with_raw_response.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.prism.properties.options.with_streaming_response.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(PropertyOption, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.prism.properties.options.with_raw_response.create(
                property_id="",
                object_type="comment",
                type="num",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        option = client.prism.properties.options.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        option = client.prism.properties.options.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
            color_scheme="color_scheme",
            description="description",
            enabled=True,
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            option_group="option_group",
            slug="slug",
            sort_index=0,
            value="value",
            idempotency_key="x",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.prism.properties.options.with_raw_response.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.prism.properties.options.with_streaming_response.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(PropertyOption, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.prism.properties.options.with_raw_response.update(
                option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                object_type="comment",
                property_id="",
                type="num",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_id` but received ''"):
            client.prism.properties.options.with_raw_response.update(
                option_id="",
                object_type="comment",
                property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                type="num",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Micro) -> None:
        option = client.prism.properties.options.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )
        assert option is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Micro) -> None:
        option = client.prism.properties.options.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert option is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.prism.properties.options.with_raw_response.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert option is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.prism.properties.options.with_streaming_response.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert option is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            client.prism.properties.options.with_raw_response.delete(
                option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                object_type="comment",
                property_id="",
                type="num",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_id` but received ''"):
            client.prism.properties.options.with_raw_response.delete(
                option_id="",
                object_type="comment",
                property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                type="num",
            )


class TestAsyncOptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        option = await async_client.prism.properties.options.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        option = await async_client.prism.properties.options.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
            color_scheme="color_scheme",
            description="description",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            option_group="option_group",
            slug="slug",
            sort_index=0,
            idempotency_key="x",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.options.with_raw_response.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.options.with_streaming_response.create(
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            object_type="comment",
            type="num",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(PropertyOption, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.prism.properties.options.with_raw_response.create(
                property_id="",
                object_type="comment",
                type="num",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        option = await async_client.prism.properties.options.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        option = await async_client.prism.properties.options.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
            color_scheme="color_scheme",
            description="description",
            enabled=True,
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            option_group="option_group",
            slug="slug",
            sort_index=0,
            value="value",
            idempotency_key="x",
        )
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.options.with_raw_response.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(PropertyOption, option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.options.with_streaming_response.update(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(PropertyOption, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.prism.properties.options.with_raw_response.update(
                option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                object_type="comment",
                property_id="",
                type="num",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_id` but received ''"):
            await async_client.prism.properties.options.with_raw_response.update(
                option_id="",
                object_type="comment",
                property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                type="num",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        option = await async_client.prism.properties.options.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )
        assert option is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMicro) -> None:
        option = await async_client.prism.properties.options.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert option is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.properties.options.with_raw_response.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert option is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.properties.options.with_streaming_response.delete(
            option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="comment",
            property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
            type="num",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert option is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_id` but received ''"):
            await async_client.prism.properties.options.with_raw_response.delete(
                option_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                object_type="comment",
                property_id="",
                type="num",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `option_id` but received ''"):
            await async_client.prism.properties.options.with_raw_response.delete(
                option_id="",
                object_type="comment",
                property_id="2fdcD1Dc-bbDb-2BBD-0Afa-1A3C33cFaADc",
                type="num",
            )
