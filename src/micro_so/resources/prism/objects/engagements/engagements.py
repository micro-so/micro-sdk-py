# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

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
    engagement_get_params,
    engagement_find_params,
    engagement_list_params,
    engagement_count_params,
    engagement_query_params,
    engagement_create_params,
    engagement_update_params,
    engagement_upsert_params,
    engagement_bulk_create_params,
    engagement_bulk_delete_params,
    engagement_bulk_update_params,
)
from .....types.prism_object_properties_param import PrismObjectPropertiesParam
from .....types.prism.objects.engagement_get_response import EngagementGetResponse
from .....types.prism.objects.engagement_find_response import EngagementFindResponse
from .....types.prism.objects.engagement_list_response import EngagementListResponse
from .....types.prism.objects.engagement_count_response import EngagementCountResponse
from .....types.prism.objects.engagement_query_response import EngagementQueryResponse
from .....types.prism.objects.engagement_create_response import EngagementCreateResponse
from .....types.prism.objects.engagement_update_response import EngagementUpdateResponse
from .....types.prism.objects.engagement_upsert_response import EngagementUpsertResponse
from .....types.prism.objects.engagement_restore_response import EngagementRestoreResponse
from .....types.prism.objects.engagement_duplicate_response import EngagementDuplicateResponse
from .....types.prism.objects.engagement_bulk_create_response import EngagementBulkCreateResponse
from .....types.prism.objects.engagement_bulk_delete_response import EngagementBulkDeleteResponse
from .....types.prism.objects.engagement_bulk_update_response import EngagementBulkUpdateResponse

__all__ = ["EngagementsResource", "AsyncEngagementsResource"]


class EngagementsResource(SyncAPIResource):
    @cached_property
    def grant(self) -> GrantResource:
        return GrantResource(self._client)

    @cached_property
    def with_raw_response(self) -> EngagementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return EngagementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EngagementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return EngagementsResourceWithStreamingResponse(self)

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
    ) -> EngagementCreateResponse:
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
            path_template("/v2/prism/{team_id}/engagement", team_id=team_id),
            body=maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                engagement_create_params.EngagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementCreateResponse,
        )

    def update(
        self,
        engagement_id: str,
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
    ) -> EngagementUpdateResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
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
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}", team_id=team_id, engagement_id=engagement_id
            ),
            body=maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                engagement_update_params.EngagementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementUpdateResponse,
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
    ) -> EngagementListResponse:
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
            path_template("/v2/prism/{team_id}/engagement", team_id=team_id),
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
                    engagement_list_params.EngagementListParams,
                ),
            ),
            cast_to=EngagementListResponse,
        )

    def delete(
        self,
        engagement_id: str,
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk_create(
        self,
        *,
        team_id: str | None = None,
        objects: Iterable[PrismObjectPropertiesParam],
        options: engagement_bulk_create_params.Options | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementBulkCreateResponse:
        """Import multiple objects in batch.

        Properties are keyed by slug. Automatically
        routes based on size: small batches complete synchronously and return 200 with
        the final `ImportJob`; large batches start an async job, return 202 with
        `status: processing` and a `Location` header, and can be polled via
        `GET /v2/prism/{teamId}/imports/{jobId}`.

        Args:
          objects: Array of objects to import with property values keyed by slug

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
            path_template("/v2/prism/{team_id}/engagement/import", team_id=team_id),
            body=maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                engagement_bulk_create_params.EngagementBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementBulkCreateResponse,
        )

    def bulk_delete(
        self,
        *,
        team_id: str | None = None,
        ids: SequenceNotStr[str],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementBulkDeleteResponse:
        """Soft-delete up to 100 records in a single call.

        Same partial-success contract as
        batch/update.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/engagement/batch/delete", team_id=team_id),
            body=maybe_transform({"ids": ids}, engagement_bulk_delete_params.EngagementBulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementBulkDeleteResponse,
        )

    def bulk_update(
        self,
        *,
        team_id: str | None = None,
        items: Iterable[engagement_bulk_update_params.Item],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementBulkUpdateResponse:
        """Patch up to 100 records in a single call.

        Each item is attempted independently —
        failures don't abort the batch. Inspect `results[].status` per item.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/engagement/batch/update", team_id=team_id),
            body=maybe_transform({"items": items}, engagement_bulk_update_params.EngagementBulkUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementBulkUpdateResponse,
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
    ) -> EngagementCountResponse:
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
            path_template("/v2/prism/{team_id}/engagement/count", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"list_id": list_id}, engagement_count_params.EngagementCountParams),
            ),
            cast_to=EngagementCountResponse,
        )

    def duplicate(
        self,
        engagement_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementDuplicateResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}/duplicate", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementDuplicateResponse,
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
    ) -> EngagementFindResponse:
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
            path_template("/v2/prism/{team_id}/engagement/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"list_id": list_id}, engagement_find_params.EngagementFindParams),
            ),
            cast_to=EngagementFindResponse,
        )

    def get(
        self,
        engagement_id: str,
        *,
        team_id: str | None = None,
        select: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementGetResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        return self._get(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"select": select}, engagement_get_params.EngagementGetParams),
            ),
            cast_to=EngagementGetResponse,
        )

    def query(
        self,
        *,
        team_id: str | None = None,
        query: engagement_query_params.Query,
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
    ) -> EngagementQueryResponse:
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
            path_template("/v2/prism/{team_id}/engagement/query", team_id=team_id),
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
                engagement_query_params.EngagementQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementQueryResponse,
        )

    def restore(
        self,
        engagement_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementRestoreResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}/restore", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementRestoreResponse,
        )

    def upsert(
        self,
        value: str,
        *,
        team_id: str | None = None,
        slug: str,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementUpsertResponse:
        """Idempotent create-or-update keyed on `{slug}={value}`.

        If exactly one record
        matches, it is patched and 200 is returned. If none match, a new record is
        created (with the lookup property set if absent) and 201 is returned. If
        multiple records match, 409 is returned and you should patch by id instead.

        Args:
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
            path_template("/v2/prism/{team_id}/engagement/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            body=maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                engagement_upsert_params.EngagementUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementUpsertResponse,
        )


class AsyncEngagementsResource(AsyncAPIResource):
    @cached_property
    def grant(self) -> AsyncGrantResource:
        return AsyncGrantResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEngagementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncEngagementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEngagementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncEngagementsResourceWithStreamingResponse(self)

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
    ) -> EngagementCreateResponse:
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
            path_template("/v2/prism/{team_id}/engagement", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                engagement_create_params.EngagementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementCreateResponse,
        )

    async def update(
        self,
        engagement_id: str,
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
    ) -> EngagementUpdateResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
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
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}", team_id=team_id, engagement_id=engagement_id
            ),
            body=await async_maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                engagement_update_params.EngagementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementUpdateResponse,
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
    ) -> EngagementListResponse:
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
            path_template("/v2/prism/{team_id}/engagement", team_id=team_id),
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
                    engagement_list_params.EngagementListParams,
                ),
            ),
            cast_to=EngagementListResponse,
        )

    async def delete(
        self,
        engagement_id: str,
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk_create(
        self,
        *,
        team_id: str | None = None,
        objects: Iterable[PrismObjectPropertiesParam],
        options: engagement_bulk_create_params.Options | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementBulkCreateResponse:
        """Import multiple objects in batch.

        Properties are keyed by slug. Automatically
        routes based on size: small batches complete synchronously and return 200 with
        the final `ImportJob`; large batches start an async job, return 202 with
        `status: processing` and a `Location` header, and can be polled via
        `GET /v2/prism/{teamId}/imports/{jobId}`.

        Args:
          objects: Array of objects to import with property values keyed by slug

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
            path_template("/v2/prism/{team_id}/engagement/import", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                engagement_bulk_create_params.EngagementBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementBulkCreateResponse,
        )

    async def bulk_delete(
        self,
        *,
        team_id: str | None = None,
        ids: SequenceNotStr[str],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementBulkDeleteResponse:
        """Soft-delete up to 100 records in a single call.

        Same partial-success contract as
        batch/update.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/engagement/batch/delete", team_id=team_id),
            body=await async_maybe_transform({"ids": ids}, engagement_bulk_delete_params.EngagementBulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementBulkDeleteResponse,
        )

    async def bulk_update(
        self,
        *,
        team_id: str | None = None,
        items: Iterable[engagement_bulk_update_params.Item],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementBulkUpdateResponse:
        """Patch up to 100 records in a single call.

        Each item is attempted independently —
        failures don't abort the batch. Inspect `results[].status` per item.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/engagement/batch/update", team_id=team_id),
            body=await async_maybe_transform(
                {"items": items}, engagement_bulk_update_params.EngagementBulkUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementBulkUpdateResponse,
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
    ) -> EngagementCountResponse:
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
            path_template("/v2/prism/{team_id}/engagement/count", team_id=team_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"list_id": list_id}, engagement_count_params.EngagementCountParams),
            ),
            cast_to=EngagementCountResponse,
        )

    async def duplicate(
        self,
        engagement_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementDuplicateResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}/duplicate", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementDuplicateResponse,
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
    ) -> EngagementFindResponse:
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
            path_template("/v2/prism/{team_id}/engagement/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"list_id": list_id}, engagement_find_params.EngagementFindParams),
            ),
            cast_to=EngagementFindResponse,
        )

    async def get(
        self,
        engagement_id: str,
        *,
        team_id: str | None = None,
        select: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementGetResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        return await self._get(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"select": select}, engagement_get_params.EngagementGetParams),
            ),
            cast_to=EngagementGetResponse,
        )

    async def query(
        self,
        *,
        team_id: str | None = None,
        query: engagement_query_params.Query,
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
    ) -> EngagementQueryResponse:
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
            path_template("/v2/prism/{team_id}/engagement/query", team_id=team_id),
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
                engagement_query_params.EngagementQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementQueryResponse,
        )

    async def restore(
        self,
        engagement_id: str,
        *,
        team_id: str | None = None,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementRestoreResponse:
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
        if not engagement_id:
            raise ValueError(f"Expected a non-empty value for `engagement_id` but received {engagement_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v2/prism/{team_id}/engagement/{engagement_id}/restore", team_id=team_id, engagement_id=engagement_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementRestoreResponse,
        )

    async def upsert(
        self,
        value: str,
        *,
        team_id: str | None = None,
        slug: str,
        default: Dict[str, object] | Omit = omit,
        list: object | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EngagementUpsertResponse:
        """Idempotent create-or-update keyed on `{slug}={value}`.

        If exactly one record
        matches, it is patched and 200 is returned. If none match, a new record is
        created (with the lookup property set if absent) and 201 is returned. If
        multiple records match, 409 is returned and you should patch by id instead.

        Args:
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
            path_template("/v2/prism/{team_id}/engagement/by/{slug}/{value}", team_id=team_id, slug=slug, value=value),
            body=await async_maybe_transform(
                {
                    "default": default,
                    "list": list,
                },
                engagement_upsert_params.EngagementUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngagementUpsertResponse,
        )


class EngagementsResourceWithRawResponse:
    def __init__(self, engagements: EngagementsResource) -> None:
        self._engagements = engagements

        self.create = to_raw_response_wrapper(
            engagements.create,
        )
        self.update = to_raw_response_wrapper(
            engagements.update,
        )
        self.list = to_raw_response_wrapper(
            engagements.list,
        )
        self.delete = to_raw_response_wrapper(
            engagements.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            engagements.bulk_create,
        )
        self.bulk_delete = to_raw_response_wrapper(
            engagements.bulk_delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            engagements.bulk_update,
        )
        self.count = to_raw_response_wrapper(
            engagements.count,
        )
        self.duplicate = to_raw_response_wrapper(
            engagements.duplicate,
        )
        self.find = to_raw_response_wrapper(
            engagements.find,
        )
        self.get = to_raw_response_wrapper(
            engagements.get,
        )
        self.query = to_raw_response_wrapper(
            engagements.query,
        )
        self.restore = to_raw_response_wrapper(
            engagements.restore,
        )
        self.upsert = to_raw_response_wrapper(
            engagements.upsert,
        )

    @cached_property
    def grant(self) -> GrantResourceWithRawResponse:
        return GrantResourceWithRawResponse(self._engagements.grant)


class AsyncEngagementsResourceWithRawResponse:
    def __init__(self, engagements: AsyncEngagementsResource) -> None:
        self._engagements = engagements

        self.create = async_to_raw_response_wrapper(
            engagements.create,
        )
        self.update = async_to_raw_response_wrapper(
            engagements.update,
        )
        self.list = async_to_raw_response_wrapper(
            engagements.list,
        )
        self.delete = async_to_raw_response_wrapper(
            engagements.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            engagements.bulk_create,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            engagements.bulk_delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            engagements.bulk_update,
        )
        self.count = async_to_raw_response_wrapper(
            engagements.count,
        )
        self.duplicate = async_to_raw_response_wrapper(
            engagements.duplicate,
        )
        self.find = async_to_raw_response_wrapper(
            engagements.find,
        )
        self.get = async_to_raw_response_wrapper(
            engagements.get,
        )
        self.query = async_to_raw_response_wrapper(
            engagements.query,
        )
        self.restore = async_to_raw_response_wrapper(
            engagements.restore,
        )
        self.upsert = async_to_raw_response_wrapper(
            engagements.upsert,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithRawResponse:
        return AsyncGrantResourceWithRawResponse(self._engagements.grant)


class EngagementsResourceWithStreamingResponse:
    def __init__(self, engagements: EngagementsResource) -> None:
        self._engagements = engagements

        self.create = to_streamed_response_wrapper(
            engagements.create,
        )
        self.update = to_streamed_response_wrapper(
            engagements.update,
        )
        self.list = to_streamed_response_wrapper(
            engagements.list,
        )
        self.delete = to_streamed_response_wrapper(
            engagements.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            engagements.bulk_create,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            engagements.bulk_delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            engagements.bulk_update,
        )
        self.count = to_streamed_response_wrapper(
            engagements.count,
        )
        self.duplicate = to_streamed_response_wrapper(
            engagements.duplicate,
        )
        self.find = to_streamed_response_wrapper(
            engagements.find,
        )
        self.get = to_streamed_response_wrapper(
            engagements.get,
        )
        self.query = to_streamed_response_wrapper(
            engagements.query,
        )
        self.restore = to_streamed_response_wrapper(
            engagements.restore,
        )
        self.upsert = to_streamed_response_wrapper(
            engagements.upsert,
        )

    @cached_property
    def grant(self) -> GrantResourceWithStreamingResponse:
        return GrantResourceWithStreamingResponse(self._engagements.grant)


class AsyncEngagementsResourceWithStreamingResponse:
    def __init__(self, engagements: AsyncEngagementsResource) -> None:
        self._engagements = engagements

        self.create = async_to_streamed_response_wrapper(
            engagements.create,
        )
        self.update = async_to_streamed_response_wrapper(
            engagements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            engagements.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            engagements.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            engagements.bulk_create,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            engagements.bulk_delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            engagements.bulk_update,
        )
        self.count = async_to_streamed_response_wrapper(
            engagements.count,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            engagements.duplicate,
        )
        self.find = async_to_streamed_response_wrapper(
            engagements.find,
        )
        self.get = async_to_streamed_response_wrapper(
            engagements.get,
        )
        self.query = async_to_streamed_response_wrapper(
            engagements.query,
        )
        self.restore = async_to_streamed_response_wrapper(
            engagements.restore,
        )
        self.upsert = async_to_streamed_response_wrapper(
            engagements.upsert,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithStreamingResponse:
        return AsyncGrantResourceWithStreamingResponse(self._engagements.grant)
