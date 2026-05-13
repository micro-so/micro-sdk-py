# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types import (
    ViewGetResponse,
    ViewCreateResponse,
    ViewUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        view = client.views.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
        )
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        view = client.views.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aggregation_prop_def_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aggregation_type="aggregation_type",
            column_layout={"foo": "bar"},
            combinator="AND",
            created_at="created_at",
            filter=[{"foo": "bar"}],
            group_by="group_by",
            group_hidden_option_ids=[{}],
            group_hide_empty=True,
            group_sort="group_sort",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            select=["string"],
            sort=[{"foo": "bar"}],
            sort_order=0,
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            updated_at="updated_at",
            user_id="user_id",
        )
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.views.with_raw_response.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.views.with_streaming_response.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewCreateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        view = client.views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        view = client.views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            aggregation_prop_def_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aggregation_type="aggregation_type",
            column_layout={"foo": "bar"},
            combinator="AND",
            filter=[{"foo": "bar"}],
            group_by="group_by",
            group_hidden_option_ids=[{}],
            group_hide_empty=True,
            group_sort="group_sort",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            select=["string"],
            sort=[{"foo": "bar"}],
            sort_order=0,
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
            view_type="view_type",
        )
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.views.with_raw_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.views.with_streaming_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewUpdateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.update(
                view_id="",
                view_object_type="action",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Micro) -> None:
        view = client.views.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.views.with_raw_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.views.with_streaming_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert view is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.delete(
                view_id="",
                view_object_type="action",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Micro) -> None:
        view = client.views.get(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert_matches_type(ViewGetResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Micro) -> None:
        response = client.views.with_raw_response.get(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewGetResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Micro) -> None:
        with client.views.with_streaming_response.get(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewGetResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.get(
                view_id="",
                view_object_type="action",
            )


class TestAsyncViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        view = await async_client.views.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
        )
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        view = await async_client.views.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aggregation_prop_def_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aggregation_type="aggregation_type",
            column_layout={"foo": "bar"},
            combinator="AND",
            created_at="created_at",
            filter=[{"foo": "bar"}],
            group_by="group_by",
            group_hidden_option_ids=[{}],
            group_hide_empty=True,
            group_sort="group_sort",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            select=["string"],
            sort=[{"foo": "bar"}],
            sort_order=0,
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            updated_at="updated_at",
            user_id="user_id",
        )
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.with_raw_response.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.views.with_streaming_response.create(
            view_object_type="action",
            name="name",
            view_type="view_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewCreateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        view = await async_client.views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        view = await async_client.views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
            aggregation_prop_def_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            aggregation_type="aggregation_type",
            column_layout={"foo": "bar"},
            combinator="AND",
            filter=[{"foo": "bar"}],
            group_by="group_by",
            group_hidden_option_ids=[{}],
            group_hide_empty=True,
            group_sort="group_sort",
            icon="icon",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            select=["string"],
            sort=[{"foo": "bar"}],
            sort_order=0,
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="user_id",
            view_type="view_type",
        )
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.with_raw_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.views.with_streaming_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewUpdateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.update(
                view_id="",
                view_object_type="action",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        view = await async_client.views.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.with_raw_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.views.with_streaming_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert view is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.delete(
                view_id="",
                view_object_type="action",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMicro) -> None:
        view = await async_client.views.get(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )
        assert_matches_type(ViewGetResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMicro) -> None:
        response = await async_client.views.with_raw_response.get(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewGetResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMicro) -> None:
        async with async_client.views.with_streaming_response.get(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_object_type="action",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewGetResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.get(
                view_id="",
                view_object_type="action",
            )
