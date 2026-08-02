# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from micro_so import Micro, AsyncMicro
from tests.utils import assert_matches_type
from micro_so.types import (
    TriggeredAutomation,
    TriggeredAutomationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggeredAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.create(
            automation_object_type="message",
            kind="update",
            name="name",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.create(
            automation_object_type="message",
            kind="update",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "type": "agent",
                    "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "cron_expression": "cron_expression",
                    "delay_seconds": 0,
                    "recipient_email_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_provider_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_object_type": "recipient_view_object_type",
                    "send_as_user_id": "send_as_user_id",
                    "subject": "subject",
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "timezone": "timezone",
                    "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            changeset={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            created_at="created_at",
            enabled=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_create=True,
            on_delete=True,
            state={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            updated_at="updated_at",
            user_id="user_id",
            idempotency_key="x",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Micro) -> None:
        response = client.triggered_automations.with_raw_response.create(
            automation_object_type="message",
            kind="update",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = response.parse()
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Micro) -> None:
        with client.triggered_automations.with_streaming_response.create(
            automation_object_type="message",
            kind="update",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = response.parse()
            assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "type": "agent",
                    "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "cron_expression": "cron_expression",
                    "delay_seconds": 0,
                    "recipient_email_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_provider_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_object_type": "recipient_view_object_type",
                    "send_as_user_id": "send_as_user_id",
                    "subject": "subject",
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "timezone": "timezone",
                    "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            changeset={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            created_at="created_at",
            enabled=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_create=True,
            on_delete=True,
            state={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            updated_at="updated_at",
            user_id="user_id",
            idempotency_key="x",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Micro) -> None:
        response = client.triggered_automations.with_raw_response.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = response.parse()
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Micro) -> None:
        with client.triggered_automations.with_streaming_response.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = response.parse()
            assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.triggered_automations.with_raw_response.update(
                automation_id="",
                automation_object_type="message",
                kind="update",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.list(
            automation_object_type="message",
        )
        assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.list(
            automation_object_type="message",
            cursor="cursor",
            kind="update",
            limit=0,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=1,
        )
        assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Micro) -> None:
        response = client.triggered_automations.with_raw_response.list(
            automation_object_type="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = response.parse()
        assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Micro) -> None:
        with client.triggered_automations.with_streaming_response.list(
            automation_object_type="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = response.parse()
            assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.delete(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )
        assert triggered_automation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Micro) -> None:
        response = client.triggered_automations.with_raw_response.delete(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = response.parse()
        assert triggered_automation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Micro) -> None:
        with client.triggered_automations.with_streaming_response.delete(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = response.parse()
            assert triggered_automation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.triggered_automations.with_raw_response.delete(
                automation_id="",
                automation_object_type="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Micro) -> None:
        triggered_automation = client.triggered_automations.get(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Micro) -> None:
        response = client.triggered_automations.with_raw_response.get(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = response.parse()
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Micro) -> None:
        with client.triggered_automations.with_streaming_response.get(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = response.parse()
            assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Micro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            client.triggered_automations.with_raw_response.get(
                automation_id="",
                automation_object_type="message",
            )


class TestAsyncTriggeredAutomations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.create(
            automation_object_type="message",
            kind="update",
            name="name",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.create(
            automation_object_type="message",
            kind="update",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "type": "agent",
                    "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "cron_expression": "cron_expression",
                    "delay_seconds": 0,
                    "recipient_email_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_provider_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_object_type": "recipient_view_object_type",
                    "send_as_user_id": "send_as_user_id",
                    "subject": "subject",
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "timezone": "timezone",
                    "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            changeset={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            created_at="created_at",
            enabled=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_create=True,
            on_delete=True,
            state={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            updated_at="updated_at",
            user_id="user_id",
            idempotency_key="x",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMicro) -> None:
        response = await async_client.triggered_automations.with_raw_response.create(
            automation_object_type="message",
            kind="update",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = await response.parse()
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMicro) -> None:
        async with async_client.triggered_automations.with_streaming_response.create(
            automation_object_type="message",
            kind="update",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = await response.parse()
            assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actions=[
                {
                    "type": "agent",
                    "agent_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "cron_expression": "cron_expression",
                    "delay_seconds": 0,
                    "recipient_email_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_provider_prop_def_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "recipient_view_object_type": "recipient_view_object_type",
                    "send_as_user_id": "send_as_user_id",
                    "subject": "subject",
                    "template_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "timezone": "timezone",
                    "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
            changeset={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            created_at="created_at",
            enabled=True,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            on_create=True,
            on_delete=True,
            state={
                "combinator": "AND",
                "filter": [{"foo": "bar"}],
            },
            body_team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            updated_at="updated_at",
            user_id="user_id",
            idempotency_key="x",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMicro) -> None:
        response = await async_client.triggered_automations.with_raw_response.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = await response.parse()
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMicro) -> None:
        async with async_client.triggered_automations.with_streaming_response.update(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
            kind="update",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = await response.parse()
            assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.triggered_automations.with_raw_response.update(
                automation_id="",
                automation_object_type="message",
                kind="update",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.list(
            automation_object_type="message",
        )
        assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.list(
            automation_object_type="message",
            cursor="cursor",
            kind="update",
            limit=0,
            list_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=1,
        )
        assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMicro) -> None:
        response = await async_client.triggered_automations.with_raw_response.list(
            automation_object_type="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = await response.parse()
        assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMicro) -> None:
        async with async_client.triggered_automations.with_streaming_response.list(
            automation_object_type="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = await response.parse()
            assert_matches_type(TriggeredAutomationListResponse, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.delete(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )
        assert triggered_automation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMicro) -> None:
        response = await async_client.triggered_automations.with_raw_response.delete(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = await response.parse()
        assert triggered_automation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMicro) -> None:
        async with async_client.triggered_automations.with_streaming_response.delete(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = await response.parse()
            assert triggered_automation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.triggered_automations.with_raw_response.delete(
                automation_id="",
                automation_object_type="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncMicro) -> None:
        triggered_automation = await async_client.triggered_automations.get(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncMicro) -> None:
        response = await async_client.triggered_automations.with_raw_response.get(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        triggered_automation = await response.parse()
        assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncMicro) -> None:
        async with async_client.triggered_automations.with_streaming_response.get(
            automation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            automation_object_type="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            triggered_automation = await response.parse()
            assert_matches_type(TriggeredAutomation, triggered_automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncMicro) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `automation_id` but received ''"):
            await async_client.triggered_automations.with_raw_response.get(
                automation_id="",
                automation_object_type="message",
            )
