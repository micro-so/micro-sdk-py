# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

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
from ...._base_client import make_request_options
from ....types.prism.properties import option_create_params, option_delete_params, option_update_params
from ....types.prism.properties.property_option import PropertyOption

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)

    def create(
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
            "agent_artifact",
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
            "multiref_agent_artifact",
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
        value: str,
        color_scheme: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        option_group: Optional[str] | Omit = omit,
        slug: str | Omit = omit,
        sort_index: Optional[int] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyOption:
        """
        Adds a single option to a `select_str` or `multiselect_str` property definition.
        Body must include `type` so the server knows which per-type option table to
        write.

        Args:
          type: Storage type for a property definition. Determines which per-type table holds
              the values, and which display formats the property can take.

          value: Display value for the option.

          list_id: Scope the option to a specific list/app.

          slug: URL-safe identifier. Defaults to a slugified `value`.

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
        return self._post(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}/options",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
            ),
            body=maybe_transform(
                {
                    "type": type,
                    "value": value,
                    "color_scheme": color_scheme,
                    "description": description,
                    "icon": icon,
                    "list_id": list_id,
                    "option_group": option_group,
                    "slug": slug,
                    "sort_index": sort_index,
                },
                option_create_params.OptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyOption,
        )

    def update(
        self,
        option_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_artifact",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        property_id: str,
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
            "multiref_agent_artifact",
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
        color_scheme: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        option_group: Optional[str] | Omit = omit,
        slug: str | Omit = omit,
        sort_index: Optional[int] | Omit = omit,
        value: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyOption:
        """Update a property option

        Args:
          type: Storage type for a property definition.

        Determines which per-type table holds
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
        if not option_id:
            raise ValueError(f"Expected a non-empty value for `option_id` but received {option_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._patch(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}/options/{option_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
                option_id=option_id,
            ),
            body=maybe_transform(
                {
                    "type": type,
                    "color_scheme": color_scheme,
                    "description": description,
                    "enabled": enabled,
                    "icon": icon,
                    "list_id": list_id,
                    "option_group": option_group,
                    "slug": slug,
                    "sort_index": sort_index,
                    "value": value,
                },
                option_update_params.OptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyOption,
        )

    def delete(
        self,
        option_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_artifact",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        property_id: str,
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
            "multiref_agent_artifact",
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
        """Delete a property option

        Args:
          type: Storage type for a property definition.

        Determines which per-type table holds
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
        if not option_id:
            raise ValueError(f"Expected a non-empty value for `option_id` but received {option_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}/options/{option_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
                option_id=option_id,
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
                    option_delete_params.OptionDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncOptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)

    async def create(
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
            "agent_artifact",
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
            "multiref_agent_artifact",
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
        value: str,
        color_scheme: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        option_group: Optional[str] | Omit = omit,
        slug: str | Omit = omit,
        sort_index: Optional[int] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyOption:
        """
        Adds a single option to a `select_str` or `multiselect_str` property definition.
        Body must include `type` so the server knows which per-type option table to
        write.

        Args:
          type: Storage type for a property definition. Determines which per-type table holds
              the values, and which display formats the property can take.

          value: Display value for the option.

          list_id: Scope the option to a specific list/app.

          slug: URL-safe identifier. Defaults to a slugified `value`.

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
        return await self._post(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}/options",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
            ),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "value": value,
                    "color_scheme": color_scheme,
                    "description": description,
                    "icon": icon,
                    "list_id": list_id,
                    "option_group": option_group,
                    "slug": slug,
                    "sort_index": sort_index,
                },
                option_create_params.OptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyOption,
        )

    async def update(
        self,
        option_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_artifact",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        property_id: str,
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
            "multiref_agent_artifact",
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
        color_scheme: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        icon: Optional[str] | Omit = omit,
        list_id: Optional[str] | Omit = omit,
        option_group: Optional[str] | Omit = omit,
        slug: str | Omit = omit,
        sort_index: Optional[int] | Omit = omit,
        value: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyOption:
        """Update a property option

        Args:
          type: Storage type for a property definition.

        Determines which per-type table holds
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
        if not option_id:
            raise ValueError(f"Expected a non-empty value for `option_id` but received {option_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._patch(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}/options/{option_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
                option_id=option_id,
            ),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "color_scheme": color_scheme,
                    "description": description,
                    "enabled": enabled,
                    "icon": icon,
                    "list_id": list_id,
                    "option_group": option_group,
                    "slug": slug,
                    "sort_index": sort_index,
                    "value": value,
                },
                option_update_params.OptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PropertyOption,
        )

    async def delete(
        self,
        option_id: str,
        *,
        team_id: str | None = None,
        object_type: Literal[
            "comment",
            "deal",
            "engagement",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "agent_artifact",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        property_id: str,
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
            "multiref_agent_artifact",
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
        """Delete a property option

        Args:
          type: Storage type for a property definition.

        Determines which per-type table holds
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
        if not option_id:
            raise ValueError(f"Expected a non-empty value for `option_id` but received {option_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/{object_type}/properties/{property_id}/options/{option_id}",
                team_id=team_id,
                object_type=object_type,
                property_id=property_id,
                option_id=option_id,
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
                    option_delete_params.OptionDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.create = to_raw_response_wrapper(
            options.create,
        )
        self.update = to_raw_response_wrapper(
            options.update,
        )
        self.delete = to_raw_response_wrapper(
            options.delete,
        )


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.create = async_to_raw_response_wrapper(
            options.create,
        )
        self.update = async_to_raw_response_wrapper(
            options.update,
        )
        self.delete = async_to_raw_response_wrapper(
            options.delete,
        )


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.create = to_streamed_response_wrapper(
            options.create,
        )
        self.update = to_streamed_response_wrapper(
            options.update,
        )
        self.delete = to_streamed_response_wrapper(
            options.delete,
        )


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.create = async_to_streamed_response_wrapper(
            options.create,
        )
        self.update = async_to_streamed_response_wrapper(
            options.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            options.delete,
        )
