# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types.prism.objects import (
    DocumentGetResponse,
    DocumentQueryResponse,
    DocumentCreateResponse,
    DocumentUpdateResponse,
    DocumentRestoreResponse,
    DocumentDuplicateResponse,
    DocumentBulkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        document = client.prism.objects.documents.create()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        document = client.prism.objects.documents.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        document = client.prism.objects.documents.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        document = client.prism.objects.documents.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentUpdateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.prism.objects.documents.with_raw_response.update(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Micro) -> None:
        document = client.prism.objects.documents.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.prism.objects.documents.with_raw_response.delete(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create(self, client: Micro) -> None:
        document = client.prism.objects.documents.bulk_create(
            objects=[{}],
        )
        assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Micro) -> None:
        document = client.prism.objects.documents.bulk_create(
            objects=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "crm": {},
                    "default": {"foo": "bar"},
                    "extended": {},
                }
            ],
            options={
                "case_insensitive": True,
                "crm_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "dedupe_by": "dedupe_by",
            },
        )
        assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_create(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.bulk_create(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.bulk_create(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Micro) -> None:
        document = client.prism.objects.documents.duplicate(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentDuplicateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.duplicate(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentDuplicateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.duplicate(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentDuplicateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.prism.objects.documents.with_raw_response.duplicate(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Micro) -> None:
        document = client.prism.objects.documents.get(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentGetResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.get(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.get(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.prism.objects.documents.with_raw_response.get(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Micro) -> None:
        document = client.prism.objects.documents.query(
            query={"select": ["string"]},
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Micro) -> None:
        document = client.prism.objects.documents.query(
            query={
                "select": ["string"],
                "combinator": "AND",
                "crm_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "filter": [{"foo": {"foo": "string"}}],
                "limit": 1,
                "page": 0,
                "sort": [{"foo": "asc"}],
            },
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            boxes=["string"],
            deleted=True,
            sources=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.query(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.query(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentQueryResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Micro) -> None:
        document = client.prism.objects.documents.restore(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Micro) -> None:
        response = client.prism.objects.documents.with_raw_response.restore(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Micro) -> None:
        with client.prism.objects.documents.with_streaming_response.restore(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentRestoreResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.prism.objects.documents.with_raw_response.restore(
                document_id="",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.create()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.update(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentUpdateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.prism.objects.documents.with_raw_response.update(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.delete(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.prism.objects.documents.with_raw_response.delete(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.bulk_create(
            objects=[{}],
        )
        assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.bulk_create(
            objects=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "crm": {},
                    "default": {"foo": "bar"},
                    "extended": {},
                }
            ],
            options={
                "case_insensitive": True,
                "crm_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "dedupe_by": "dedupe_by",
            },
        )
        assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.bulk_create(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.bulk_create(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentBulkCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.duplicate(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentDuplicateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.duplicate(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentDuplicateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.duplicate(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentDuplicateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.prism.objects.documents.with_raw_response.duplicate(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.get(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentGetResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.get(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.get(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.prism.objects.documents.with_raw_response.get(
                document_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.query(
            query={"select": ["string"]},
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.query(
            query={
                "select": ["string"],
                "combinator": "AND",
                "crm_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "filter": [{"foo": {"foo": "string"}}],
                "limit": 1,
                "page": 0,
                "sort": [{"foo": "asc"}],
            },
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            boxes=["string"],
            deleted=True,
            sources=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.query(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentQueryResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.query(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentQueryResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncMicro) -> None:
        document = await async_client.prism.objects.documents.restore(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.documents.with_raw_response.restore(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.documents.with_streaming_response.restore(
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentRestoreResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.prism.objects.documents.with_raw_response.restore(
                document_id="",
            )
