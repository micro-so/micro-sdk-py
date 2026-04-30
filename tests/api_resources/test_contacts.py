# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro import Micro, AsyncMicro
from micro.types import (
    ContactListResponse,
    ContactImportResponse,
    PrismObjectProperties,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        contact = client.contacts.create()
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        contact = client.contacts.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(PrismObjectProperties, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        contact = client.contacts.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        contact = client.contacts.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.contacts.with_raw_response.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.contacts.with_streaming_response.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(PrismObjectProperties, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.update(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Micro) -> None:
        contact = client.contacts.list(
            query={"select": ["string"]},
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Micro) -> None:
        contact = client.contacts.list(
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
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Micro) -> None:
        response = client.contacts.with_raw_response.list(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Micro) -> None:
        with client.contacts.with_streaming_response.list(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Micro) -> None:
        contact = client.contacts.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.contacts.with_raw_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.contacts.with_streaming_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contacts.with_raw_response.delete(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import(self, client: Micro) -> None:
        contact = client.contacts.import_(
            objects=[{}],
        )
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_with_all_params(self, client: Micro) -> None:
        contact = client.contacts.import_(
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
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import(self, client: Micro) -> None:
        response = client.contacts.with_raw_response.import_(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import(self, client: Micro) -> None:
        with client.contacts.with_streaming_response.import_(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactImportResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.create()
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.create(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.contacts.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.contacts.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(PrismObjectProperties, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.contacts.with_raw_response.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(PrismObjectProperties, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.contacts.with_streaming_response.update(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(PrismObjectProperties, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.update(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.list(
            query={"select": ["string"]},
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.list(
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
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMicro) -> None:
        response = await async_client.contacts.with_raw_response.list(
            query={"select": ["string"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMicro) -> None:
        async with async_client.contacts.with_streaming_response.list(
            query={"select": ["string"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.contacts.with_raw_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.contacts.with_streaming_response.delete(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contacts.with_raw_response.delete(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.import_(
            objects=[{}],
        )
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncMicro) -> None:
        contact = await async_client.contacts.import_(
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
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncMicro) -> None:
        response = await async_client.contacts.with_raw_response.import_(
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactImportResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncMicro) -> None:
        async with async_client.contacts.with_streaming_response.import_(
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactImportResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
