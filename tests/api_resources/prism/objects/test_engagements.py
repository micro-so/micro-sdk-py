# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types.prism.objects import (
    EngagementGetResponse,
    EngagementFindResponse,
    EngagementListResponse,
    EngagementCountResponse,
    EngagementQueryResponse,
    EngagementCreateResponse,
    EngagementUpdateResponse,
    EngagementUpsertResponse,
    EngagementRestoreResponse,
    EngagementDuplicateResponse,
    EngagementBulkCreateResponse,
    EngagementBulkDeleteResponse,
    EngagementBulkUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEngagements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.create()
        assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.create(
            default={"foo": "bar"},
            list={},
            idempotency_key="x",
        )
        assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default={"foo": "bar"},
            list={},
            idempotency_key="x",
            if_match="If-Match",
        )
        assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            client.prism.objects.engagements.with_raw_response.update(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.list()
        assert_matches_type(EngagementListResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.list(
            cursor="cursor",
            deleted=True,
            include_total=True,
            limit=1,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            select="select",
            sort="sort",
        )
        assert_matches_type(EngagementListResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementListResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementListResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert engagement is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            if_match="If-Match",
        )
        assert engagement is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert engagement is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert engagement is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            client.prism.objects.engagements.with_raw_response.delete(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.bulk_create(
            objects=[{}],
        )
        assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.bulk_create(
            objects=[
                {
                    "default": {"foo": "bar"},
                    "list": {},
                }
            ],
            options={
                "case_insensitive": True,
                "dedupe_by": "dedupe_by",
                "list_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            idempotency_key="x",
        )
        assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_create(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.bulk_create(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.bulk_create(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_delete_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            idempotency_key="x",
        )
        assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_update(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_update_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            idempotency_key="x",
        )
        assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_update(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_count(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.count()
        assert_matches_type(EngagementCountResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_count_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.count(
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementCountResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementCountResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementCountResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="x",
        )
        assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            client.prism.objects.engagements.with_raw_response.duplicate(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.find(
            value="value",
            slug="slug",
        )
        assert_matches_type(EngagementFindResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.find(
            value="value",
            slug="slug",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementFindResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.find(
            value="value",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementFindResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.find(
            value="value",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementFindResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_find(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.prism.objects.engagements.with_raw_response.find(
                value="value",
                slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value` but received ''"):
            client.prism.objects.engagements.with_raw_response.find(
                value="",
                slug="slug",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementGetResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            select="select",
        )
        assert_matches_type(EngagementGetResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementGetResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementGetResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            client.prism.objects.engagements.with_raw_response.get(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.query(
            query={"select": ["string"]},
        )
        assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.query(
            query={
                "select": ["string"],
                "combinator": "AND",
                "cursor": "cursor",
                "filter": [{"foo": {"api_empty": "string"}}],
                "limit": 1,
                "list_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "page": 0,
                "sort": [{"foo": "asc"}],
            },
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            boxes=["string"],
            cursor="cursor",
            deleted=True,
            include_total=True,
            sources=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.query(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.query(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="x",
        )
        assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            client.prism.objects.engagements.with_raw_response.restore(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.upsert(
            value="value",
            slug="slug",
        )
        assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Micro) -> None:
        engagement = client.prism.objects.engagements.upsert(
            value="value",
            slug="slug",
            default={"foo": "bar"},
            list={},
            idempotency_key="x",
        )
        assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Micro) -> None:
        response = client.prism.objects.engagements.with_raw_response.upsert(
            value="value",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = response.parse()
        assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Micro) -> None:
        with client.prism.objects.engagements.with_streaming_response.upsert(
            value="value",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = response.parse()
            assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.prism.objects.engagements.with_raw_response.upsert(
                value="value",
                slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value` but received ''"):
            client.prism.objects.engagements.with_raw_response.upsert(
                value="",
                slug="slug",
            )


class TestAsyncEngagements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.create()
        assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.create(
            default={"foo": "bar"},
            list={},
            idempotency_key="x",
        )
        assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementCreateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default={"foo": "bar"},
            list={},
            idempotency_key="x",
            if_match="If-Match",
        )
        assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.update(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementUpdateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.update(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.list()
        assert_matches_type(EngagementListResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.list(
            cursor="cursor",
            deleted=True,
            include_total=True,
            limit=1,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            select="select",
            sort="sort",
        )
        assert_matches_type(EngagementListResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementListResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementListResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert engagement is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            if_match="If-Match",
        )
        assert engagement is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert engagement is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.delete(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert engagement is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.delete(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.bulk_create(
            objects=[{}],
        )
        assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.bulk_create(
            objects=[
                {
                    "default": {"foo": "bar"},
                    "list": {},
                }
            ],
            options={
                "case_insensitive": True,
                "dedupe_by": "dedupe_by",
                "list_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            idempotency_key="x",
        )
        assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.bulk_create(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.bulk_create(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementBulkCreateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_delete_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            idempotency_key="x",
        )
        assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.bulk_delete(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementBulkDeleteResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            idempotency_key="x",
        )
        assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.bulk_update(
            items=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementBulkUpdateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.count()
        assert_matches_type(EngagementCountResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_count_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.count(
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementCountResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementCountResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementCountResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="x",
        )
        assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.duplicate(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementDuplicateResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.duplicate(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.find(
            value="value",
            slug="slug",
        )
        assert_matches_type(EngagementFindResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.find(
            value="value",
            slug="slug",
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementFindResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.find(
            value="value",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementFindResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.find(
            value="value",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementFindResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_find(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.find(
                value="value",
                slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.find(
                value="",
                slug="slug",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementGetResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            select="select",
        )
        assert_matches_type(EngagementGetResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementGetResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.get(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementGetResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.get(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.query(
            query={"select": ["string"]},
        )
        assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.query(
            query={
                "select": ["string"],
                "combinator": "AND",
                "cursor": "cursor",
                "filter": [{"foo": {"api_empty": "string"}}],
                "limit": 1,
                "list_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "page": 0,
                "sort": [{"foo": "asc"}],
            },
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            boxes=["string"],
            cursor="cursor",
            deleted=True,
            include_total=True,
            sources=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.query(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.query(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementQueryResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            idempotency_key="x",
        )
        assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.restore(
            engagement_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementRestoreResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `engagement_id` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.restore(
                engagement_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.upsert(
            value="value",
            slug="slug",
        )
        assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncMicro) -> None:
        engagement = await async_client.prism.objects.engagements.upsert(
            value="value",
            slug="slug",
            default={"foo": "bar"},
            list={},
            idempotency_key="x",
        )
        assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.engagements.with_raw_response.upsert(
            value="value",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        engagement = await response.parse()
        assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.engagements.with_streaming_response.upsert(
            value="value",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            engagement = await response.parse()
            assert_matches_type(EngagementUpsertResponse, engagement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.upsert(
                value="value",
                slug="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `value` but received ''"):
            await async_client.prism.objects.engagements.with_raw_response.upsert(
                value="",
                slug="slug",
            )
