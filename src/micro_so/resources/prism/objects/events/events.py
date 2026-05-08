# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from .grant import (
    GrantResource,
    AsyncGrantResource,
    GrantResourceWithRawResponse,
    AsyncGrantResourceWithRawResponse,
    GrantResourceWithStreamingResponse,
    AsyncGrantResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.prism.objects import event_query_params
from .....types.prism.objects.event_get_response import EventGetResponse
from .....types.prism.objects.event_query_response import EventQueryResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def grant(self) -> GrantResource:
        return GrantResource(self._client)

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def get(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetResponse:
        """
        Get object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/v2/prism/{team_id}/event/{event_id}", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventGetResponse,
        )

    def query(
        self,
        *,
        team_id: str | None = None,
        query: event_query_params.Query,
        id: Union[str, SequenceNotStr[str]] | Omit = omit,
        boxes: SequenceNotStr[str] | Omit = omit,
        deleted: bool | Omit = omit,
        sources: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueryResponse:
        """
        Query

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._post(
            path_template("/v2/prism/query/{team_id}/event", team_id=team_id),
            body=maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                event_query_params.EventQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueryResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def grant(self) -> AsyncGrantResource:
        return AsyncGrantResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def get(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetResponse:
        """
        Get object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/v2/prism/{team_id}/event/{event_id}", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventGetResponse,
        )

    async def query(
        self,
        *,
        team_id: str | None = None,
        query: event_query_params.Query,
        id: Union[str, SequenceNotStr[str]] | Omit = omit,
        boxes: SequenceNotStr[str] | Omit = omit,
        deleted: bool | Omit = omit,
        sources: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueryResponse:
        """
        Query

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return await self._post(
            path_template("/v2/prism/query/{team_id}/event", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                event_query_params.EventQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueryResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get = to_raw_response_wrapper(
            events.get,
        )
        self.query = to_raw_response_wrapper(
            events.query,
        )

    @cached_property
    def grant(self) -> GrantResourceWithRawResponse:
        return GrantResourceWithRawResponse(self._events.grant)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get = async_to_raw_response_wrapper(
            events.get,
        )
        self.query = async_to_raw_response_wrapper(
            events.query,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithRawResponse:
        return AsyncGrantResourceWithRawResponse(self._events.grant)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.get = to_streamed_response_wrapper(
            events.get,
        )
        self.query = to_streamed_response_wrapper(
            events.query,
        )

    @cached_property
    def grant(self) -> GrantResourceWithStreamingResponse:
        return GrantResourceWithStreamingResponse(self._events.grant)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
        self.query = async_to_streamed_response_wrapper(
            events.query,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithStreamingResponse:
        return AsyncGrantResourceWithStreamingResponse(self._events.grant)
