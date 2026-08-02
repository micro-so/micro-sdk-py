# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    triggered_automation_list_params,
    triggered_automation_create_params,
    triggered_automation_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.triggered_automation import TriggeredAutomation
from ..types.triggered_automation_list_response import TriggeredAutomationListResponse

__all__ = ["TriggeredAutomationsResource", "AsyncTriggeredAutomationsResource"]


class TriggeredAutomationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TriggeredAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return TriggeredAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TriggeredAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return TriggeredAutomationsResourceWithStreamingResponse(self)

    def create(
        self,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        *,
        path_team_id: str | None = None,
        kind: Literal["update", "lifecycle"],
        name: str,
        id: str | Omit = omit,
        actions: Iterable[triggered_automation_create_params.Action] | Omit = omit,
        changeset: triggered_automation_create_params.Changeset | Omit = omit,
        created_at: str | Omit = omit,
        enabled: bool | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        on_create: bool | Omit = omit,
        on_delete: bool | Omit = omit,
        state: triggered_automation_create_params.State | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        updated_at: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomation:
        """
        Create a triggered automation (state + changeset filter trees)

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          actions: Actions to run when the automation fires; each item has a `type` plus
              type-specific fields.

          changeset: A changeset filter group (update automations only): a combinator plus an array
              of transition clauses matching what is changing. Dot-paths (nested reference
              filters) are NOT permitted — direct properties only.

          on_create: Lifecycle automations only.

          on_delete: Lifecycle automations only.

          state: A filter group: a combinator plus an array of slug-based clauses. Dot-paths
              (e.g. `organization.location`) express nested reference filters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template(
                "/v2/prism/{path_team_id}/{automation_object_type}/triggered_automations",
                path_team_id=path_team_id,
                automation_object_type=automation_object_type,
            ),
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "id": id,
                    "actions": actions,
                    "changeset": changeset,
                    "created_at": created_at,
                    "enabled": enabled,
                    "list_id": list_id,
                    "on_create": on_create,
                    "on_delete": on_delete,
                    "state": state,
                    "body_team_id": body_team_id,
                    "updated_at": updated_at,
                    "user_id": user_id,
                },
                triggered_automation_create_params.TriggeredAutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggeredAutomation,
        )

    def update(
        self,
        automation_id: str,
        *,
        path_team_id: str | None = None,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        kind: Literal["update", "lifecycle"],
        name: str,
        id: str | Omit = omit,
        actions: Iterable[triggered_automation_update_params.Action] | Omit = omit,
        changeset: triggered_automation_update_params.Changeset | Omit = omit,
        created_at: str | Omit = omit,
        enabled: bool | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        on_create: bool | Omit = omit,
        on_delete: bool | Omit = omit,
        state: triggered_automation_update_params.State | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        updated_at: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomation:
        """
        Replace a triggered automation (idempotent full write of the whole tree)

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          actions: Actions to run when the automation fires; each item has a `type` plus
              type-specific fields.

          changeset: A changeset filter group (update automations only): a combinator plus an array
              of transition clauses matching what is changing. Dot-paths (nested reference
              filters) are NOT permitted — direct properties only.

          on_create: Lifecycle automations only.

          on_delete: Lifecycle automations only.

          state: A filter group: a combinator plus an array of slug-based clauses. Dot-paths
              (e.g. `organization.location`) express nested reference filters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._put(
            path_template(
                "/v2/prism/{path_team_id}/{automation_object_type}/triggered_automations/{automation_id}",
                path_team_id=path_team_id,
                automation_object_type=automation_object_type,
                automation_id=automation_id,
            ),
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "id": id,
                    "actions": actions,
                    "changeset": changeset,
                    "created_at": created_at,
                    "enabled": enabled,
                    "list_id": list_id,
                    "on_create": on_create,
                    "on_delete": on_delete,
                    "state": state,
                    "body_team_id": body_team_id,
                    "updated_at": updated_at,
                    "user_id": user_id,
                },
                triggered_automation_update_params.TriggeredAutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggeredAutomation,
        )

    def list(
        self,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        *,
        team_id: str | None = None,
        cursor: str | Omit = omit,
        kind: Literal["update", "lifecycle"] | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomationListResponse:
        """
        List triggered automations for an owner

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          cursor: Opaque pagination cursor (from a prior response's next_cursor); supersedes
              page/limit when present.

          kind: Optional filter to a single automation kind. When omitted, both kinds are
              returned.

          limit: Maximum items per page (<= 50; defaults to 50).

          list_id: List (CRM) id to scope the listing to. When omitted, automations owned by the
              path team are returned.

          page: 1-based page number. Prefer cursor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        return self._get(
            path_template(
                "/v2/prism/{team_id}/{automation_object_type}/triggered_automations",
                team_id=team_id,
                automation_object_type=automation_object_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "kind": kind,
                        "limit": limit,
                        "list_id": list_id,
                        "page": page,
                    },
                    triggered_automation_list_params.TriggeredAutomationListParams,
                ),
            ),
            cast_to=TriggeredAutomationListResponse,
        )

    def delete(
        self,
        automation_id: str,
        *,
        team_id: str | None = None,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a triggered automation and its filter trees

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/{automation_object_type}/triggered_automations/{automation_id}",
                team_id=team_id,
                automation_object_type=automation_object_type,
                automation_id=automation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        automation_id: str,
        *,
        team_id: str | None = None,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomation:
        """
        Read a triggered automation

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return self._get(
            path_template(
                "/v2/prism/{team_id}/{automation_object_type}/triggered_automations/{automation_id}",
                team_id=team_id,
                automation_object_type=automation_object_type,
                automation_id=automation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggeredAutomation,
        )


class AsyncTriggeredAutomationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTriggeredAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncTriggeredAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTriggeredAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncTriggeredAutomationsResourceWithStreamingResponse(self)

    async def create(
        self,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        *,
        path_team_id: str | None = None,
        kind: Literal["update", "lifecycle"],
        name: str,
        id: str | Omit = omit,
        actions: Iterable[triggered_automation_create_params.Action] | Omit = omit,
        changeset: triggered_automation_create_params.Changeset | Omit = omit,
        created_at: str | Omit = omit,
        enabled: bool | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        on_create: bool | Omit = omit,
        on_delete: bool | Omit = omit,
        state: triggered_automation_create_params.State | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        updated_at: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomation:
        """
        Create a triggered automation (state + changeset filter trees)

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          actions: Actions to run when the automation fires; each item has a `type` plus
              type-specific fields.

          changeset: A changeset filter group (update automations only): a combinator plus an array
              of transition clauses matching what is changing. Dot-paths (nested reference
              filters) are NOT permitted — direct properties only.

          on_create: Lifecycle automations only.

          on_delete: Lifecycle automations only.

          state: A filter group: a combinator plus an array of slug-based clauses. Dot-paths
              (e.g. `organization.location`) express nested reference filters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v2/prism/{path_team_id}/{automation_object_type}/triggered_automations",
                path_team_id=path_team_id,
                automation_object_type=automation_object_type,
            ),
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "id": id,
                    "actions": actions,
                    "changeset": changeset,
                    "created_at": created_at,
                    "enabled": enabled,
                    "list_id": list_id,
                    "on_create": on_create,
                    "on_delete": on_delete,
                    "state": state,
                    "body_team_id": body_team_id,
                    "updated_at": updated_at,
                    "user_id": user_id,
                },
                triggered_automation_create_params.TriggeredAutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggeredAutomation,
        )

    async def update(
        self,
        automation_id: str,
        *,
        path_team_id: str | None = None,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        kind: Literal["update", "lifecycle"],
        name: str,
        id: str | Omit = omit,
        actions: Iterable[triggered_automation_update_params.Action] | Omit = omit,
        changeset: triggered_automation_update_params.Changeset | Omit = omit,
        created_at: str | Omit = omit,
        enabled: bool | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        on_create: bool | Omit = omit,
        on_delete: bool | Omit = omit,
        state: triggered_automation_update_params.State | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        updated_at: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomation:
        """
        Replace a triggered automation (idempotent full write of the whole tree)

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          actions: Actions to run when the automation fires; each item has a `type` plus
              type-specific fields.

          changeset: A changeset filter group (update automations only): a combinator plus an array
              of transition clauses matching what is changing. Dot-paths (nested reference
              filters) are NOT permitted — direct properties only.

          on_create: Lifecycle automations only.

          on_delete: Lifecycle automations only.

          state: A filter group: a combinator plus an array of slug-based clauses. Dot-paths
              (e.g. `organization.location`) express nested reference filters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._put(
            path_template(
                "/v2/prism/{path_team_id}/{automation_object_type}/triggered_automations/{automation_id}",
                path_team_id=path_team_id,
                automation_object_type=automation_object_type,
                automation_id=automation_id,
            ),
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "id": id,
                    "actions": actions,
                    "changeset": changeset,
                    "created_at": created_at,
                    "enabled": enabled,
                    "list_id": list_id,
                    "on_create": on_create,
                    "on_delete": on_delete,
                    "state": state,
                    "body_team_id": body_team_id,
                    "updated_at": updated_at,
                    "user_id": user_id,
                },
                triggered_automation_update_params.TriggeredAutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggeredAutomation,
        )

    async def list(
        self,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        *,
        team_id: str | None = None,
        cursor: str | Omit = omit,
        kind: Literal["update", "lifecycle"] | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomationListResponse:
        """
        List triggered automations for an owner

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          cursor: Opaque pagination cursor (from a prior response's next_cursor); supersedes
              page/limit when present.

          kind: Optional filter to a single automation kind. When omitted, both kinds are
              returned.

          limit: Maximum items per page (<= 50; defaults to 50).

          list_id: List (CRM) id to scope the listing to. When omitted, automations owned by the
              path team are returned.

          page: 1-based page number. Prefer cursor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        return await self._get(
            path_template(
                "/v2/prism/{team_id}/{automation_object_type}/triggered_automations",
                team_id=team_id,
                automation_object_type=automation_object_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "kind": kind,
                        "limit": limit,
                        "list_id": list_id,
                        "page": page,
                    },
                    triggered_automation_list_params.TriggeredAutomationListParams,
                ),
            ),
            cast_to=TriggeredAutomationListResponse,
        )

    async def delete(
        self,
        automation_id: str,
        *,
        team_id: str | None = None,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a triggered automation and its filter trees

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/{automation_object_type}/triggered_automations/{automation_id}",
                team_id=team_id,
                automation_object_type=automation_object_type,
                automation_id=automation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        automation_id: str,
        *,
        team_id: str | None = None,
        automation_object_type: Literal[
            "message", "action", "event", "document", "identity", "linkedin_message", "deal", "organization", "contact"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TriggeredAutomation:
        """
        Read a triggered automation

        Args:
          automation_object_type: Object types that support triggered automations. Must match the
              triggered-automation whitelist in @micro/database migrate-sql
              (TRIGGERED_AUTOMATION_OBJECTS).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not automation_object_type:
            raise ValueError(
                f"Expected a non-empty value for `automation_object_type` but received {automation_object_type!r}"
            )
        if not automation_id:
            raise ValueError(f"Expected a non-empty value for `automation_id` but received {automation_id!r}")
        return await self._get(
            path_template(
                "/v2/prism/{team_id}/{automation_object_type}/triggered_automations/{automation_id}",
                team_id=team_id,
                automation_object_type=automation_object_type,
                automation_id=automation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TriggeredAutomation,
        )


class TriggeredAutomationsResourceWithRawResponse:
    def __init__(self, triggered_automations: TriggeredAutomationsResource) -> None:
        self._triggered_automations = triggered_automations

        self.create = to_raw_response_wrapper(
            triggered_automations.create,
        )
        self.update = to_raw_response_wrapper(
            triggered_automations.update,
        )
        self.list = to_raw_response_wrapper(
            triggered_automations.list,
        )
        self.delete = to_raw_response_wrapper(
            triggered_automations.delete,
        )
        self.get = to_raw_response_wrapper(
            triggered_automations.get,
        )


class AsyncTriggeredAutomationsResourceWithRawResponse:
    def __init__(self, triggered_automations: AsyncTriggeredAutomationsResource) -> None:
        self._triggered_automations = triggered_automations

        self.create = async_to_raw_response_wrapper(
            triggered_automations.create,
        )
        self.update = async_to_raw_response_wrapper(
            triggered_automations.update,
        )
        self.list = async_to_raw_response_wrapper(
            triggered_automations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            triggered_automations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            triggered_automations.get,
        )


class TriggeredAutomationsResourceWithStreamingResponse:
    def __init__(self, triggered_automations: TriggeredAutomationsResource) -> None:
        self._triggered_automations = triggered_automations

        self.create = to_streamed_response_wrapper(
            triggered_automations.create,
        )
        self.update = to_streamed_response_wrapper(
            triggered_automations.update,
        )
        self.list = to_streamed_response_wrapper(
            triggered_automations.list,
        )
        self.delete = to_streamed_response_wrapper(
            triggered_automations.delete,
        )
        self.get = to_streamed_response_wrapper(
            triggered_automations.get,
        )


class AsyncTriggeredAutomationsResourceWithStreamingResponse:
    def __init__(self, triggered_automations: AsyncTriggeredAutomationsResource) -> None:
        self._triggered_automations = triggered_automations

        self.create = async_to_streamed_response_wrapper(
            triggered_automations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            triggered_automations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            triggered_automations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            triggered_automations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            triggered_automations.get,
        )
