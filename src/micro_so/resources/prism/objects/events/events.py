# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union

import httpx

from .grant import (
    GrantResource,
    AsyncGrantResource,
    GrantResourceWithRawResponse,
    AsyncGrantResourceWithRawResponse,
    GrantResourceWithStreamingResponse,
    AsyncGrantResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
    event_create_params,
    event_update_params,
    event_upsert_params,
)
from .....types.prism.objects.event_get_response import EventGetResponse
from .....types.prism.objects.event_find_response import EventFindResponse
from .....types.prism.objects.event_list_response import EventListResponse
from .....types.prism.objects.event_count_response import EventCountResponse
from .....types.prism.objects.event_query_response import EventQueryResponse
from .....types.prism.objects.event_create_response import EventCreateResponse
from .....types.prism.objects.event_update_response import EventUpdateResponse
from .....types.prism.objects.event_upsert_response import EventUpsertResponse
from .....types.prism.objects.event_restore_response import EventRestoreResponse
from .....types.prism.objects.event_duplicate_response import EventDuplicateResponse

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

    def create(
        self,
        *,
        team_id: str | None = None,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventCreateResponse:
        """Create object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null. For select/multiselect properties, values may be option slugs
              or option UUIDs on write; option slugs are returned on read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/event", team_id=team_id),
            body=maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventCreateResponse,
        )

    def update(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventUpdateResponse:
        """Patch object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null. For select/multiselect properties, values may be option slugs
              or option UUIDs on write; option slugs are returned on read.

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
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "If-Match": if_match,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v2/prism/{team_id}/event/{event_id}", team_id=team_id, event_id=event_id),
            body=maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventUpdateResponse,
        )

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

    def delete(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete object

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return self._delete(
            path_template("/v2/prism/{team_id}/event/{event_id}", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    def duplicate(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDuplicateResponse:
        """
        Duplicate object

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/event/{event_id}/duplicate", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDuplicateResponse,
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
        idempotency_key: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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

    def restore(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventRestoreResponse:
        """
        Restore object

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/event/{event_id}/restore", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventRestoreResponse,
        )

    def upsert(
        self,
        value: str,
        *,
        team_id: str | None = None,
        slug: str,
        list_id: str | Omit = omit,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventUpsertResponse:
        """Idempotent create-or-update keyed on `{slug}={value}`.

        If exactly one record
        matches, it is patched and 200 is returned. If none match, a new record is
        created (with the lookup property set if absent) and 201 is returned. If
        multiple records match, 409 is returned and you should patch by id instead.

        Args:
          list_id: Scope the upsert to a specific list/app. Required to match or write list-scoped
              properties, including `app_stage`.

          default: Properties keyed by property slug. Values can be strings, numbers, booleans,
              arrays, or null. For select/multiselect properties, values may be option slugs
              or option UUIDs on write; option slugs are returned on read.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._put(
            path_template("/v2/prism/{team_id}/event/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            body=maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                event_upsert_params.EventUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"list_id": list_id}, event_upsert_params.EventUpsertParams),
            ),
            cast_to=EventUpsertResponse,
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

    async def create(
        self,
        *,
        team_id: str | None = None,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventCreateResponse:
        """Create object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null. For select/multiselect properties, values may be option slugs
              or option UUIDs on write; option slugs are returned on read.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/event", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventCreateResponse,
        )

    async def update(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventUpdateResponse:
        """Patch object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null. For select/multiselect properties, values may be option slugs
              or option UUIDs on write; option slugs are returned on read.

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
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "If-Match": if_match,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v2/prism/{team_id}/event/{event_id}", team_id=team_id, event_id=event_id),
            body=await async_maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventUpdateResponse,
        )

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

    async def delete(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete object

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/prism/{team_id}/event/{event_id}", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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

    async def duplicate(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDuplicateResponse:
        """
        Duplicate object

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/event/{event_id}/duplicate", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDuplicateResponse,
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
        idempotency_key: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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

    async def restore(
        self,
        event_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventRestoreResponse:
        """
        Restore object

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/event/{event_id}/restore", team_id=team_id, event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventRestoreResponse,
        )

    async def upsert(
        self,
        value: str,
        *,
        team_id: str | None = None,
        slug: str,
        list_id: str | Omit = omit,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventUpsertResponse:
        """Idempotent create-or-update keyed on `{slug}={value}`.

        If exactly one record
        matches, it is patched and 200 is returned. If none match, a new record is
        created (with the lookup property set if absent) and 201 is returned. If
        multiple records match, 409 is returned and you should patch by id instead.

        Args:
          list_id: Scope the upsert to a specific list/app. Required to match or write list-scoped
              properties, including `app_stage`.

          default: Properties keyed by property slug. Values can be strings, numbers, booleans,
              arrays, or null. For select/multiselect properties, values may be option slugs
              or option UUIDs on write; option slugs are returned on read.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._put(
            path_template("/v2/prism/{team_id}/event/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            body=await async_maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                event_upsert_params.EventUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"list_id": list_id}, event_upsert_params.EventUpsertParams),
            ),
            cast_to=EventUpsertResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )
        self.update = to_raw_response_wrapper(
            events.update,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.delete = to_raw_response_wrapper(
            events.delete,
        )
        self.count = to_raw_response_wrapper(
            events.count,
        )
        self.duplicate = to_raw_response_wrapper(
            events.duplicate,
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
        self.restore = to_raw_response_wrapper(
            events.restore,
        )
        self.upsert = to_raw_response_wrapper(
            events.upsert,
        )

    @cached_property
    def grant(self) -> GrantResourceWithRawResponse:
        return GrantResourceWithRawResponse(self._events.grant)


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )
        self.update = async_to_raw_response_wrapper(
            events.update,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.delete = async_to_raw_response_wrapper(
            events.delete,
        )
        self.count = async_to_raw_response_wrapper(
            events.count,
        )
        self.duplicate = async_to_raw_response_wrapper(
            events.duplicate,
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
        self.restore = async_to_raw_response_wrapper(
            events.restore,
        )
        self.upsert = async_to_raw_response_wrapper(
            events.upsert,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithRawResponse:
        return AsyncGrantResourceWithRawResponse(self._events.grant)


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )
        self.update = to_streamed_response_wrapper(
            events.update,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.delete = to_streamed_response_wrapper(
            events.delete,
        )
        self.count = to_streamed_response_wrapper(
            events.count,
        )
        self.duplicate = to_streamed_response_wrapper(
            events.duplicate,
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
        self.restore = to_streamed_response_wrapper(
            events.restore,
        )
        self.upsert = to_streamed_response_wrapper(
            events.upsert,
        )

    @cached_property
    def grant(self) -> GrantResourceWithStreamingResponse:
        return GrantResourceWithStreamingResponse(self._events.grant)


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
        self.update = async_to_streamed_response_wrapper(
            events.update,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            events.delete,
        )
        self.count = async_to_streamed_response_wrapper(
            events.count,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            events.duplicate,
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
        self.restore = async_to_streamed_response_wrapper(
            events.restore,
        )
        self.upsert = async_to_streamed_response_wrapper(
            events.upsert,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithStreamingResponse:
        return AsyncGrantResourceWithStreamingResponse(self._events.grant)
