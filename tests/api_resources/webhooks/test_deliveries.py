# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types import WebhookDeliveryDetail
from micro_so._utils import parse_datetime
from micro_so.types.webhooks import DeliveryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Micro) -> None:
        delivery = client.webhooks.deliveries.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Micro) -> None:
        delivery = client.webhooks.deliveries.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after=parse_datetime("2019-12-27T18:11:19.117Z"),
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
            status="success",
            type="delivery",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Micro) -> None:
        response = client.webhooks.deliveries.with_raw_response.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Micro) -> None:
        with client.webhooks.deliveries.with_streaming_response.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.list(
                webhook_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Micro) -> None:
        delivery = client.webhooks.deliveries.get(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookDeliveryDetail, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Micro) -> None:
        response = client.webhooks.deliveries.with_raw_response.get(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(WebhookDeliveryDetail, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Micro) -> None:
        with client.webhooks.deliveries.with_streaming_response.get(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(WebhookDeliveryDetail, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.get(
                delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.get(
                delivery_id="",
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMicro) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMicro) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after=parse_datetime("2019-12-27T18:11:19.117Z"),
            before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
            status="success",
            type="delivery",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMicro) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMicro) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.list(
                webhook_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMicro) -> None:
        delivery = await async_client.webhooks.deliveries.get(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookDeliveryDetail, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMicro) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.get(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(WebhookDeliveryDetail, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMicro) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.get(
            delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(WebhookDeliveryDetail, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.get(
                delivery_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.get(
                delivery_id="",
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
