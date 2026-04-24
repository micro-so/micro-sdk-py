# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro import Micro, AsyncMicro
from micro.types import (
    PrismImportObjectsResponse,
    PrismDuplicateObjectResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrism:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_object(self, client: Micro) -> None:
        prism = client.prism.create_object(
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_object_with_all_params(self, client: Micro) -> None:
        prism = client.prism.create_object(
            object_type="deal",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_object(self, client: Micro) -> None:
        response = client.prism.with_raw_response.create_object(
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_object(self, client: Micro) -> None:
        with client.prism.with_streaming_response.create_object(
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_object(self, client: Micro) -> None:
        prism = client.prism.delete_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_object(self, client: Micro) -> None:
        response = client.prism.with_raw_response.delete_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_object(self, client: Micro) -> None:
        with client.prism.with_streaming_response.delete_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_object(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.prism.with_raw_response.delete_object(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate_object(self, client: Micro) -> None:
        prism = client.prism.duplicate_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert_matches_type(PrismDuplicateObjectResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_duplicate_object(self, client: Micro) -> None:
        response = client.prism.with_raw_response.duplicate_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = response.parse()
        assert_matches_type(PrismDuplicateObjectResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_duplicate_object(self, client: Micro) -> None:
        with client.prism.with_streaming_response.duplicate_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = response.parse()
            assert_matches_type(PrismDuplicateObjectResponse, prism, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_duplicate_object(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.prism.with_raw_response.duplicate_object(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_objects(self, client: Micro) -> None:
        prism = client.prism.import_objects(
            object_type="identity",
            objects=[{}],
        )
        assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_import_objects_with_all_params(self, client: Micro) -> None:
        prism = client.prism.import_objects(
            object_type="identity",
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
        assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_import_objects(self, client: Micro) -> None:
        response = client.prism.with_raw_response.import_objects(
            object_type="identity",
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = response.parse()
        assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_import_objects(self, client: Micro) -> None:
        with client.prism.with_streaming_response.import_objects(
            object_type="identity",
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = response.parse()
            assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_object(self, client: Micro) -> None:
        prism = client.prism.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_object_with_all_params(self, client: Micro) -> None:
        prism = client.prism.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_object(self, client: Micro) -> None:
        response = client.prism.with_raw_response.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_object(self, client: Micro) -> None:
        with client.prism.with_streaming_response.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_patch_object(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.prism.with_raw_response.patch_object(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_object(self, client: Micro) -> None:
        prism = client.prism.restore_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_object(self, client: Micro) -> None:
        response = client.prism.with_raw_response.restore_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_object(self, client: Micro) -> None:
        with client.prism.with_streaming_response.restore_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_object(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.prism.with_raw_response.restore_object(
                object_id="",
                object_type="deal",
            )


class TestAsyncPrism:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_object(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.create_object(
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_object_with_all_params(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.create_object(
            object_type="deal",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_object(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.with_raw_response.create_object(
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = await response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_object(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.with_streaming_response.create_object(
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = await response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_object(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.delete_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_object(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.with_raw_response.delete_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = await response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_object(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.with_streaming_response.delete_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = await response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_object(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.prism.with_raw_response.delete_object(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate_object(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.duplicate_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert_matches_type(PrismDuplicateObjectResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_duplicate_object(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.with_raw_response.duplicate_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = await response.parse()
        assert_matches_type(PrismDuplicateObjectResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate_object(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.with_streaming_response.duplicate_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = await response.parse()
            assert_matches_type(PrismDuplicateObjectResponse, prism, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_duplicate_object(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.prism.with_raw_response.duplicate_object(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_objects(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.import_objects(
            object_type="identity",
            objects=[{}],
        )
        assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_import_objects_with_all_params(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.import_objects(
            object_type="identity",
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
        assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_import_objects(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.with_raw_response.import_objects(
            object_type="identity",
            objects=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = await response.parse()
        assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_import_objects(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.with_streaming_response.import_objects(
            object_type="identity",
            objects=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = await response.parse()
            assert_matches_type(PrismImportObjectsResponse, prism, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_object(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_object_with_all_params(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            crm={},
            default={"foo": "bar"},
            extended={},
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_object(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.with_raw_response.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = await response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_object(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.with_streaming_response.patch_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = await response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_patch_object(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.prism.with_raw_response.patch_object(
                object_id="",
                object_type="deal",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_object(self, async_client: AsyncMicro) -> None:
        prism = await async_client.prism.restore_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_object(self, async_client: AsyncMicro) -> None:
        response = await async_client.prism.with_raw_response.restore_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prism = await response.parse()
        assert prism is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_object(self, async_client: AsyncMicro) -> None:
        async with async_client.prism.with_streaming_response.restore_object(
            object_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            object_type="deal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prism = await response.parse()
            assert prism is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_object(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.prism.with_raw_response.restore_object(
                object_id="",
                object_type="deal",
            )
