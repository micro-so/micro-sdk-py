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
from .....types.prism.objects import (
    event_get_params,
    event_find_params,
    event_list_params,
    event_count_params,
    event_query_params,
)
from .....types.prism.objects.event_get_response import EventGetResponse
from .....types.prism.objects.event_find_response import EventFindResponse
from .....types.prism.objects.event_list_response import EventListResponse
from .....types.prism.objects.event_count_response import EventCountResponse
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

    def list(
        self,
        *,
        team_id: str | None = None,
        cursor: str | Omit = omit,
        deleted: bool | Omit = omit,
        include_total: bool | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        select: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventListResponse:
        """Convenience list endpoint.

        Equivalent to
        `POST /v2/prism/{teamId}/{objectType}/query` with an empty body, plus
        query-string sugar for the common cases. Any unrecognized query parameter is
        interpreted as an equality filter on a property of that name; pass arrays for
        `in`. Values are received as strings, so non-string property filters via this
        endpoint may not work — use the `query` endpoint for typed comparisons or
        anything beyond simple equality.

        Args:
          cursor: Opaque cursor from a previous response's `next_cursor`. Pass it back unchanged
              to fetch the next page.

          deleted: Include soft-deleted records. Pass the literal string `true`.

          include_total: When set to `true`, the response includes a `total` field with the unpaginated
              row count. Costs an extra pass; prefer `GET .../count` for the unfiltered total.

          limit: Maximum number of rows to return. Capped server-side at 50.

          list_id: Scope properties to a specific list/app.

          select: Comma-separated property slugs to return. Use dot notation for relationships.
              `id` is always returned at the top level. Defaults to all properties.

          sort:
              Comma-separated list of slugs. Prefix with `-` for descending. Example:
              `sort=-updated_at,name`.

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
            path_template("/v2/prism/{team_id}/event", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "deleted": deleted,
                        "include_total": include_total,
                        "limit": limit,
                        "list_id": list_id,
                        "select": select,
                        "sort": sort,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=EventListResponse,
        )

    def count(
        self,
        *,
        team_id: str | None = None,
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventCountResponse:
        """
        Returns the total number of records of this object type that the caller can see.
        Avoids the page-overshoot anti-pattern — clients no longer need to keep paging
        until `has_more` flips false to discover the total. Currently does not apply
        query filters; for a filtered total, pass `include_total: true` in a POST
        `/query` body.

        Args:
          list_id: Scope the count to a specific list/app.

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
            path_template("/v2/prism/{team_id}/event/count", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"list_id": list_id}, event_count_params.EventCountParams),
            ),
            cast_to=EventCountResponse,
        )

    def find(
        self,
        value: str,
        *,
        team_id: str | None = None,
        slug: str,
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventFindResponse:
        """Returns the single record whose property `{slug}` equals `{value}`.

        404 if
        nothing matches; 409 if more than one record matches.

        Args:
          list_id: Scope the lookup to a specific list/app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not value:
            raise ValueError(f"Expected a non-empty value for `value` but received {value!r}")
        return self._get(
            path_template("/v2/prism/{team_id}/event/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"list_id": list_id}, event_find_params.EventFindParams),
            ),
            cast_to=EventFindResponse,
        )

    def get(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        select: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetResponse:
        """Get object

        Args:
          select: Comma-separated property slugs to return.

        Use dot notation for relationships.
              `id` is always returned at the top level. Defaults to all properties.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"select": select}, event_get_params.EventGetParams),
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
        cursor: str | Omit = omit,
        deleted: bool | Omit = omit,
        include_total: bool | Omit = omit,
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
          cursor: Alternative location for the opaque cursor (a sibling of `query`). Use whichever
              feels more natural; if both are present, `query.cursor` wins.

          include_total: When true, the response includes a `total` field with the unpaginated row count.
              Costs an additional pass over the result set — for unfiltered totals prefer
              `GET /v2/prism/{teamId}/{objectType}/count` instead.

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
            path_template("/v2/prism/{team_id}/event/query", team_id=team_id),
            body=maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "cursor": cursor,
                    "deleted": deleted,
                    "include_total": include_total,
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

    async def list(
        self,
        *,
        team_id: str | None = None,
        cursor: str | Omit = omit,
        deleted: bool | Omit = omit,
        include_total: bool | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        select: str | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventListResponse:
        """Convenience list endpoint.

        Equivalent to
        `POST /v2/prism/{teamId}/{objectType}/query` with an empty body, plus
        query-string sugar for the common cases. Any unrecognized query parameter is
        interpreted as an equality filter on a property of that name; pass arrays for
        `in`. Values are received as strings, so non-string property filters via this
        endpoint may not work — use the `query` endpoint for typed comparisons or
        anything beyond simple equality.

        Args:
          cursor: Opaque cursor from a previous response's `next_cursor`. Pass it back unchanged
              to fetch the next page.

          deleted: Include soft-deleted records. Pass the literal string `true`.

          include_total: When set to `true`, the response includes a `total` field with the unpaginated
              row count. Costs an extra pass; prefer `GET .../count` for the unfiltered total.

          limit: Maximum number of rows to return. Capped server-side at 50.

          list_id: Scope properties to a specific list/app.

          select: Comma-separated property slugs to return. Use dot notation for relationships.
              `id` is always returned at the top level. Defaults to all properties.

          sort:
              Comma-separated list of slugs. Prefix with `-` for descending. Example:
              `sort=-updated_at,name`.

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
            path_template("/v2/prism/{team_id}/event", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "deleted": deleted,
                        "include_total": include_total,
                        "limit": limit,
                        "list_id": list_id,
                        "select": select,
                        "sort": sort,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=EventListResponse,
        )

    async def count(
        self,
        *,
        team_id: str | None = None,
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventCountResponse:
        """
        Returns the total number of records of this object type that the caller can see.
        Avoids the page-overshoot anti-pattern — clients no longer need to keep paging
        until `has_more` flips false to discover the total. Currently does not apply
        query filters; for a filtered total, pass `include_total: true` in a POST
        `/query` body.

        Args:
          list_id: Scope the count to a specific list/app.

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
            path_template("/v2/prism/{team_id}/event/count", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"list_id": list_id}, event_count_params.EventCountParams),
            ),
            cast_to=EventCountResponse,
        )

    async def find(
        self,
        value: str,
        *,
        team_id: str | None = None,
        slug: str,
        list_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventFindResponse:
        """Returns the single record whose property `{slug}` equals `{value}`.

        404 if
        nothing matches; 409 if more than one record matches.

        Args:
          list_id: Scope the lookup to a specific list/app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        if not value:
            raise ValueError(f"Expected a non-empty value for `value` but received {value!r}")
        return await self._get(
            path_template("/v2/prism/{team_id}/event/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"list_id": list_id}, event_find_params.EventFindParams),
            ),
            cast_to=EventFindResponse,
        )

    async def get(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        select: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetResponse:
        """Get object

        Args:
          select: Comma-separated property slugs to return.

        Use dot notation for relationships.
              `id` is always returned at the top level. Defaults to all properties.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"select": select}, event_get_params.EventGetParams),
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
        cursor: str | Omit = omit,
        deleted: bool | Omit = omit,
        include_total: bool | Omit = omit,
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
          cursor: Alternative location for the opaque cursor (a sibling of `query`). Use whichever
              feels more natural; if both are present, `query.cursor` wins.

          include_total: When true, the response includes a `total` field with the unpaginated row count.
              Costs an additional pass over the result set — for unfiltered totals prefer
              `GET /v2/prism/{teamId}/{objectType}/count` instead.

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
            path_template("/v2/prism/{team_id}/event/query", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "cursor": cursor,
                    "deleted": deleted,
                    "include_total": include_total,
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

        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.count = to_raw_response_wrapper(
            events.count,
        )
        self.find = to_raw_response_wrapper(
            events.find,
        )
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

        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.count = async_to_raw_response_wrapper(
            events.count,
        )
        self.find = async_to_raw_response_wrapper(
            events.find,
        )
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

        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.count = to_streamed_response_wrapper(
            events.count,
        )
        self.find = to_streamed_response_wrapper(
            events.find,
        )
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

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.count = async_to_streamed_response_wrapper(
            events.count,
        )
        self.find = async_to_streamed_response_wrapper(
            events.find,
        )
        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
        self.query = async_to_streamed_response_wrapper(
            events.query,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithStreamingResponse:
        return AsyncGrantResourceWithStreamingResponse(self._events.grant)
