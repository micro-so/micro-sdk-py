# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types.prism.objects import (
    ContactQueryResponse,
    ContactCreateResponse,
    ContactBulkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        contact = client.prism.objects.contacts.create()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        contact = client.prism.objects.contacts.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.prism.objects.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.prism.objects.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create(self, client: Micro) -> None:
        contact = client.prism.objects.contacts.bulk_create(
            objects=[{}],
        )
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Micro) -> None:
        contact = client.prism.objects.contacts.bulk_create(
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
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_create(self, client: Micro) -> None:
        response = client.prism.objects.contacts.with_raw_response.bulk_create(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Micro) -> None:
        with client.prism.objects.contacts.with_streaming_response.bulk_create(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Micro) -> None:
        contact = client.prism.objects.contacts.query(
            query={"select": ["string"]},
        )
        assert_matches_type(ContactQueryResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Micro) -> None:
        contact = client.prism.objects.contacts.query(
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
        assert_matches_type(ContactQueryResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Micro) -> None:
        response = client.prism.objects.contacts.with_raw_response.query(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactQueryResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Micro) -> None:
        with client.prism.objects.contacts.with_streaming_response.query(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactQueryResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        contact = await async_client.prism.objects.contacts.create()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.prism.objects.contacts.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncMicro) -> None:
        contact = await async_client.prism.objects.contacts.bulk_create(
            objects=[{}],
        )
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.prism.objects.contacts.bulk_create(
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
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.contacts.with_raw_response.bulk_create(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.contacts.with_streaming_response.bulk_create(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactBulkCreateResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncMicro) -> None:
        contact = await async_client.prism.objects.contacts.query(
            query={"select": ["string"]},
        )
        assert_matches_type(ContactQueryResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.prism.objects.contacts.query(
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
        assert_matches_type(ContactQueryResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.objects.contacts.with_raw_response.query(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactQueryResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.objects.contacts.with_streaming_response.query(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactQueryResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
