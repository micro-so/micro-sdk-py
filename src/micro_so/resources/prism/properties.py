# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.prism import property_list_params, property_list_all_params
from ..._base_client import make_request_options
from ...types.prism.property_list_response import PropertyListResponse
from ...types.prism.property_list_all_response import PropertyListAllResponse

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
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

    def list(
        self,
        object_type: Literal[
            "deal",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
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
          list_id: Scope properties to a specific list/app.

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
                        "list_id": list_id,
                        "term": term,
                    },
                    property_list_params.PropertyListParams,
                ),
            ),
            cast_to=PropertyListResponse,
        )

    def list_all(
        self,
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
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
          list_id: Scope properties to a specific list/app.

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

    async def list(
        self,
        object_type: Literal[
            "deal",
            "identity",
            "ai_chat_thread",
            "ai_chat_message",
            "document",
            "action",
            "event",
            "organization",
            "contact",
        ],
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
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
          list_id: Scope properties to a specific list/app.

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
                        "list_id": list_id,
                        "term": term,
                    },
                    property_list_params.PropertyListParams,
                ),
            ),
            cast_to=PropertyListResponse,
        )

    async def list_all(
        self,
        *,
        team_id: str | None = None,
        autofill: bool | Omit = omit,
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
          list_id: Scope properties to a specific list/app.

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

        self.list = to_raw_response_wrapper(
            properties.list,
        )
        self.list_all = to_raw_response_wrapper(
            properties.list_all,
        )


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.list = async_to_raw_response_wrapper(
            properties.list,
        )
        self.list_all = async_to_raw_response_wrapper(
            properties.list_all,
        )


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.list = to_streamed_response_wrapper(
            properties.list,
        )
        self.list_all = to_streamed_response_wrapper(
            properties.list_all,
        )


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.list = async_to_streamed_response_wrapper(
            properties.list,
        )
        self.list_all = async_to_streamed_response_wrapper(
            properties.list_all,
        )
