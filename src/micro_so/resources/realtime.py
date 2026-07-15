# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.realtime_create_ticket_response import RealtimeCreateTicketResponse

__all__ = ["RealtimeResource", "AsyncRealtimeResource"]


class RealtimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return RealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return RealtimeResourceWithStreamingResponse(self)

    def create_ticket(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeCreateTicketResponse:
        """
        Exchange your API key (or session) for a short-lived ticket that authenticates a
        connection to the realtime object-change stream. Open a WebSocket to the push
        endpoint with the returned ticket as the `token` query parameter. The ticket is
        single-purpose and expires quickly; call this again to obtain a fresh one before
        reconnecting.
        """
        return self._post(
            "/v2/realtime/ticket",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateTicketResponse,
        )


class AsyncRealtimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRealtimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRealtimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncRealtimeResourceWithStreamingResponse(self)

    async def create_ticket(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RealtimeCreateTicketResponse:
        """
        Exchange your API key (or session) for a short-lived ticket that authenticates a
        connection to the realtime object-change stream. Open a WebSocket to the push
        endpoint with the returned ticket as the `token` query parameter. The ticket is
        single-purpose and expires quickly; call this again to obtain a fresh one before
        reconnecting.
        """
        return await self._post(
            "/v2/realtime/ticket",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RealtimeCreateTicketResponse,
        )


class RealtimeResourceWithRawResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.create_ticket = to_raw_response_wrapper(
            realtime.create_ticket,
        )


class AsyncRealtimeResourceWithRawResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.create_ticket = async_to_raw_response_wrapper(
            realtime.create_ticket,
        )


class RealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: RealtimeResource) -> None:
        self._realtime = realtime

        self.create_ticket = to_streamed_response_wrapper(
            realtime.create_ticket,
        )


class AsyncRealtimeResourceWithStreamingResponse:
    def __init__(self, realtime: AsyncRealtimeResource) -> None:
        self._realtime = realtime

        self.create_ticket = async_to_streamed_response_wrapper(
            realtime.create_ticket,
        )
