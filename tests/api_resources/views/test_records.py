# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro.types.views import RecordListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Micro) -> None:
        record = client.views.records.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert_matches_type(RecordListResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Micro) -> None:
        record = client.views.records.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            limit=0,
            page=1,
        )
        assert_matches_type(RecordListResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Micro) -> None:
        response = client.views.records.with_raw_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordListResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Micro) -> None:
        with client.views.records.with_streaming_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordListResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.records.with_raw_response.list(
                view_id="",
                view_object_type="action",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pin(self, client: Micro) -> None:
        record = client.views.records.pin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pin(self, client: Micro) -> None:
        response = client.views.records.with_raw_response.pin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pin(self, client: Micro) -> None:
        with client.views.records.with_streaming_response.pin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pin(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.records.with_raw_response.pin(
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_object_type="action",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.views.records.with_raw_response.pin(
                object_id="",
                view_object_type="action",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reorder(self, client: Micro) -> None:
        record = client.views.records.reorder(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reorder(self, client: Micro) -> None:
        response = client.views.records.with_raw_response.reorder(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reorder(self, client: Micro) -> None:
        with client.views.records.with_streaming_response.reorder(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reorder(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.records.with_raw_response.reorder(
                view_id="",
                view_object_type="action",
                object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpin(self, client: Micro) -> None:
        record = client.views.records.unpin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpin(self, client: Micro) -> None:
        response = client.views.records.with_raw_response.unpin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpin(self, client: Micro) -> None:
        with client.views.records.with_streaming_response.unpin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpin(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.records.with_raw_response.unpin(
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_object_type="action",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.views.records.with_raw_response.unpin(
                object_id="",
                view_object_type="action",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRecords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMicro) -> None:
        record = await async_client.views.records.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert_matches_type(RecordListResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMicro) -> None:
        record = await async_client.views.records.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            limit=0,
            page=1,
        )
        assert_matches_type(RecordListResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.records.with_raw_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordListResponse, record, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMicro) -> None:
        async with async_client.views.records.with_streaming_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordListResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.records.with_raw_response.list(
                view_id="",
                view_object_type="action",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pin(self, async_client: AsyncMicro) -> None:
        record = await async_client.views.records.pin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pin(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.records.with_raw_response.pin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pin(self, async_client: AsyncMicro) -> None:
        async with async_client.views.records.with_streaming_response.pin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pin(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.records.with_raw_response.pin(
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_object_type="action",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.views.records.with_raw_response.pin(
                object_id="",
                view_object_type="action",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reorder(self, async_client: AsyncMicro) -> None:
        record = await async_client.views.records.reorder(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reorder(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.records.with_raw_response.reorder(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reorder(self, async_client: AsyncMicro) -> None:
        async with async_client.views.records.with_streaming_response.reorder(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reorder(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.records.with_raw_response.reorder(
                view_id="",
                view_object_type="action",
                object_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpin(self, async_client: AsyncMicro) -> None:
        record = await async_client.views.records.unpin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpin(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.records.with_raw_response.unpin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert record is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpin(self, async_client: AsyncMicro) -> None:
        async with async_client.views.records.with_streaming_response.unpin(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert record is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpin(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.records.with_raw_response.unpin(
                object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_object_type="action",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.views.records.with_raw_response.unpin(
                object_id="",
                view_object_type="action",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
