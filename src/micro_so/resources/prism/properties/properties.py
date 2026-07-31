# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from .options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.prism import (
    property_list_params,
    property_create_params,
    property_delete_params,
    property_update_params,
    property_list_all_params,
)
from ...._base_client import make_request_options
from ....types.prism.property_definition import PropertyDefinition
from ....types.prism.property_list_response import PropertyListResponse
from ....types.prism.property_list_all_response import PropertyListAllResponse

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    @cached_property
    def options(self) -> OptionsResource:
        return OptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        *,
        team_id: str | None = None,
        name: str,
        type: Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ],
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        options: Iterable[property_create_params.Option] | Omit = omit,
        required: bool | Omit = omit,
        role_id: Optional[str] | Omit = omit,
        slug: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyDefinition:
        """Define a new property on this object type, scoped to the calling team.

        Search
        the existing properties first (GET this path with `term`) and reuse a match
        instead of defining a second property for the same fact. Pass `list_id` in the
        body to scope the definition to one list/app; without it the property is
        workspace-global and appears on every list. A name already used in that scope,
        an explicitly requested slug already taken, or a slug that a shared property
        already owns all return 409 naming the definition to use instead. The property's
        display format is resolved from `type` automatically — pass `role_id` only to
        override it. For `select_str` and `multiselect_str` types you may pre-seed the
        choices via `options`.

        Args:
          name: Human-readable name, unique within the scope the definition is created in. A
              name already taken in that scope returns 409; the message names the existing
              definition's id, slug and type so you can write to it instead.

          type: Storage type for a property definition. Determines which per-type table holds
              the values, and which display formats the property can take.

          list_id: Scopes the definition to one list/app. Omit it only for a property that
              genuinely belongs to the whole workspace: a definition created without `list_id`
              is workspace-global and surfaces on every list of this object type.

          options: Only honored when `type` is `select_str` or `multiselect_str`.

          required: When true, records must carry a non-empty value for this property on create.
              Defaults to false.

          role_id: Optional display format for the property, drawn from the workspace's property
              roles. Omit it and the canonical role for `type` is applied (plain text, plain
              number, checkbox). Supply it only to pick a narrower format such as email, URL
              or currency; the role's data type must match `type`.

          slug: URL-safe identifier. When omitted it defaults to a slugified `name` and is
              disambiguated with a numeric suffix on conflict. When supplied explicitly it is
              treated as part of your write contract and is never silently renamed — a
              collision returns 409 instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/{object_type}/properties", team_id=team_id, object_type=object_type),
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "icon": icon,
                    "list_id": list_id,
                    "options": options,
                    "required": required,
                    "role_id": role_id,
                    "slug": slug,
                },
                property_create_params.PropertyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyDefinition,
        )

    def update(
        self,
        property_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        type: Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ],
        enabled: bool | Omit = omit,
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        required: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyDefinition:
        """Patches the editable fields (`name`, `icon`, `enabled`) of a property
        definition.

        `type` and scoping fields are immutable; `type` must be supplied in
        the body so the server knows which per-type table to write.

        Args:
          type: Storage type for a property definition. Determines which per-type table holds
              the values, and which display formats the property can take.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._patch(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
            ),
            body=maybe_transform(
                {
                    "type": type,
                    "enabled": enabled,
                    "icon": icon,
                    "list_id": list_id,
                    "name": name,
                    "required": required,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyDefinition,
        )

    def list(
        self,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
        include_options: Union[bool, Literal["true", "false", "0", "1"]] | Omit = omit,
        list_id: str | Omit = omit,
        term: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyListResponse:
        """
        Get metadata properties by object type

        Args:
          include_options: When false, return property definitions without hydrating select/multiselect
              option rows. Defaults to true server-side (parseIncludeOptions). Accepts boolean
              or query-string forms (true/false/0/1). Uses anyOf (not oneOf) so qs/AJV
              boolean-vs-string ambiguity does not 400 when Speakeasy SDKs send
              include_options=true.

          list_id: Scope properties to a specific list/app. Scoping is strict: the response carries
              only that list's definitions, not the workspace-global ones that also apply to
              its records. Call once with `list_id` and once without to see everything a write
              could resolve against.

          term: Case-insensitive substring match on the property name. Use this to find an
              existing property before creating a new one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            path_template("/v2/prism/{team_id}/{object_type}/properties", team_id=team_id, object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "autofill": autofill,
                        "include_options": include_options,
                        "list_id": list_id,
                        "term": term,
                    },
                    property_list_params.PropertyListParams,
                ),
            ),
            cast_to=PropertyListResponse,
        )

    def delete(
        self,
        property_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        type: Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ],
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes the property definition and any of its options.

        Fails with 409
        `property_in_use` if records still reference the property.

        Args:
          type: Storage type of this property definition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "list_id": list_id,
                    },
                    property_delete_params.PropertyDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def list_all(
        self,
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
        include_options: Union[bool, Literal["true", "false", "0", "1"]] | Omit = omit,
        list_id: str | Omit = omit,
        term: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyListAllResponse:
        """
        Get metadata properties

        Args:
          include_options: When false, return property definitions without hydrating select/multiselect
              option rows. Defaults to true server-side (parseIncludeOptions). Accepts boolean
              or query-string forms (true/false/0/1). Uses anyOf (not oneOf) so qs/AJV
              boolean-vs-string ambiguity does not 400 when Speakeasy SDKs send
              include_options=true.

          list_id: Scope properties to a specific list/app. Scoping is strict: the response carries
              only that list's definitions, not the workspace-global ones that also apply to
              its records. Call once with `list_id` and once without to see everything a write
              could resolve against.

          term: Case-insensitive substring match on the property name. Use this to find an
              existing property before creating a new one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get(
            path_template("/v2/prism/{team_id}/properties", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "autofill": autofill,
                        "include_options": include_options,
                        "list_id": list_id,
                        "term": term,
                    },
                    property_list_all_params.PropertyListAllParams,
                ),
            ),
            cast_to=PropertyListAllResponse,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    @cached_property
    def options(self) -> AsyncOptionsResource:
        return AsyncOptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        *,
        team_id: str | None = None,
        name: str,
        type: Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ],
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        options: Iterable[property_create_params.Option] | Omit = omit,
        required: bool | Omit = omit,
        role_id: Optional[str] | Omit = omit,
        slug: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyDefinition:
        """Define a new property on this object type, scoped to the calling team.

        Search
        the existing properties first (GET this path with `term`) and reuse a match
        instead of defining a second property for the same fact. Pass `list_id` in the
        body to scope the definition to one list/app; without it the property is
        workspace-global and appears on every list. A name already used in that scope,
        an explicitly requested slug already taken, or a slug that a shared property
        already owns all return 409 naming the definition to use instead. The property's
        display format is resolved from `type` automatically — pass `role_id` only to
        override it. For `select_str` and `multiselect_str` types you may pre-seed the
        choices via `options`.

        Args:
          name: Human-readable name, unique within the scope the definition is created in. A
              name already taken in that scope returns 409; the message names the existing
              definition's id, slug and type so you can write to it instead.

          type: Storage type for a property definition. Determines which per-type table holds
              the values, and which display formats the property can take.

          list_id: Scopes the definition to one list/app. Omit it only for a property that
              genuinely belongs to the whole workspace: a definition created without `list_id`
              is workspace-global and surfaces on every list of this object type.

          options: Only honored when `type` is `select_str` or `multiselect_str`.

          required: When true, records must carry a non-empty value for this property on create.
              Defaults to false.

          role_id: Optional display format for the property, drawn from the workspace's property
              roles. Omit it and the canonical role for `type` is applied (plain text, plain
              number, checkbox). Supply it only to pick a narrower format such as email, URL
              or currency; the role's data type must match `type`.

          slug: URL-safe identifier. When omitted it defaults to a slugified `name` and is
              disambiguated with a numeric suffix on conflict. When supplied explicitly it is
              treated as part of your write contract and is never silently renamed — a
              collision returns 409 instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/{object_type}/properties", team_id=team_id, object_type=object_type),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "icon": icon,
                    "list_id": list_id,
                    "options": options,
                    "required": required,
                    "role_id": role_id,
                    "slug": slug,
                },
                property_create_params.PropertyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyDefinition,
        )

    async def update(
        self,
        property_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        type: Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ],
        enabled: bool | Omit = omit,
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        required: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyDefinition:
        """Patches the editable fields (`name`, `icon`, `enabled`) of a property
        definition.

        `type` and scoping fields are immutable; `type` must be supplied in
        the body so the server knows which per-type table to write.

        Args:
          type: Storage type for a property definition. Determines which per-type table holds
              the values, and which display formats the property can take.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._patch(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
            ),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "enabled": enabled,
                    "icon": icon,
                    "list_id": list_id,
                    "name": name,
                    "required": required,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyDefinition,
        )

    async def list(
        self,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
        include_options: Union[bool, Literal["true", "false", "0", "1"]] | Omit = omit,
        list_id: str | Omit = omit,
        term: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyListResponse:
        """
        Get metadata properties by object type

        Args:
          include_options: When false, return property definitions without hydrating select/multiselect
              option rows. Defaults to true server-side (parseIncludeOptions). Accepts boolean
              or query-string forms (true/false/0/1). Uses anyOf (not oneOf) so qs/AJV
              boolean-vs-string ambiguity does not 400 when Speakeasy SDKs send
              include_options=true.

          list_id: Scope properties to a specific list/app. Scoping is strict: the response carries
              only that list's definitions, not the workspace-global ones that also apply to
              its records. Call once with `list_id` and once without to see everything a write
              could resolve against.

          term: Case-insensitive substring match on the property name. Use this to find an
              existing property before creating a new one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            path_template("/v2/prism/{team_id}/{object_type}/properties", team_id=team_id, object_type=object_type),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "autofill": autofill,
                        "include_options": include_options,
                        "list_id": list_id,
                        "term": term,
                    },
                    property_list_params.PropertyListParams,
                ),
            ),
            cast_to=PropertyListResponse,
        )

    async def delete(
        self,
        property_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_site",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        type: Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ],
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes the property definition and any of its options.

        Fails with 409
        `property_in_use` if records still reference the property.

        Args:
          type: Storage type of this property definition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_id:
            raise ValueError(f"Expected a non-empty value for `property_id` but received {property_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "list_id": list_id,
                    },
                    property_delete_params.PropertyDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def list_all(
        self,
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
        include_options: Union[bool, Literal["true", "false", "0", "1"]] | Omit = omit,
        list_id: str | Omit = omit,
        term: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyListAllResponse:
        """
        Get metadata properties

        Args:
          include_options: When false, return property definitions without hydrating select/multiselect
              option rows. Defaults to true server-side (parseIncludeOptions). Accepts boolean
              or query-string forms (true/false/0/1). Uses anyOf (not oneOf) so qs/AJV
              boolean-vs-string ambiguity does not 400 when Speakeasy SDKs send
              include_options=true.

          list_id: Scope properties to a specific list/app. Scoping is strict: the response carries
              only that list's definitions, not the workspace-global ones that also apply to
              its records. Call once with `list_id` and once without to see everything a write
              could resolve against.

          term: Case-insensitive substring match on the property name. Use this to find an
              existing property before creating a new one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._get(
            path_template("/v2/prism/{team_id}/properties", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "autofill": autofill,
                        "include_options": include_options,
                        "list_id": list_id,
                        "term": term,
                    },
                    property_list_all_params.PropertyListAllParams,
                ),
            ),
            cast_to=PropertyListAllResponse,
        )


class PropertiesResourceWithRawResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.create = to_raw_response_wrapper(
            properties.create,
        )
        self.update = to_raw_response_wrapper(
            properties.update,
        )
        self.list = to_raw_response_wrapper(
            properties.list,
        )
        self.delete = to_raw_response_wrapper(
            properties.delete,
        )
        self.list_all = to_raw_response_wrapper(
            properties.list_all,
        )

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        return OptionsResourceWithRawResponse(self._properties.options)


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.create = async_to_raw_response_wrapper(
            properties.create,
        )
        self.update = async_to_raw_response_wrapper(
            properties.update,
        )
        self.list = async_to_raw_response_wrapper(
            properties.list,
        )
        self.delete = async_to_raw_response_wrapper(
            properties.delete,
        )
        self.list_all = async_to_raw_response_wrapper(
            properties.list_all,
        )

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        return AsyncOptionsResourceWithRawResponse(self._properties.options)


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.create = to_streamed_response_wrapper(
            properties.create,
        )
        self.update = to_streamed_response_wrapper(
            properties.update,
        )
        self.list = to_streamed_response_wrapper(
            properties.list,
        )
        self.delete = to_streamed_response_wrapper(
            properties.delete,
        )
        self.list_all = to_streamed_response_wrapper(
            properties.list_all,
        )

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        return OptionsResourceWithStreamingResponse(self._properties.options)


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.create = async_to_streamed_response_wrapper(
            properties.create,
        )
        self.update = async_to_streamed_response_wrapper(
            properties.update,
        )
        self.list = async_to_streamed_response_wrapper(
            properties.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            properties.delete,
        )
        self.list_all = async_to_streamed_response_wrapper(
            properties.list_all,
        )

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        return AsyncOptionsResourceWithStreamingResponse(self._properties.options)
