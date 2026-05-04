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
from .....types.prism.objects import deal_query_params, deal_create_params, deal_update_params, deal_bulk_create_params
from .....types.prism_object_properties import PrismObjectProperties
from .....types.prism_object_properties_param import PrismObjectPropertiesParam
from .....types.prism.objects.deal_query_response import DealQueryResponse
from .....types.prism.objects.deal_duplicate_response import DealDuplicateResponse
from .....types.prism.objects.deal_bulk_create_response import DealBulkCreateResponse

__all__ = ["DealsResource", "AsyncDealsResource"]


class DealsResource(SyncAPIResource):
    @cached_property
    def grant(self) -> GrantResource:
        return GrantResource(self._client)

    @cached_property
    def with_raw_response(self) -> DealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return DealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return DealsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        team_id: str | None = None,
        id: str | Omit = omit,
        crm: object | Omit = omit,
        default: Dict[str, object] | Omit = omit,
        extended: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
        """Create object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null.

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
            path_template("/v2/prism/{team_id}/deal", team_id=team_id),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                deal_create_params.DealCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )

    def update(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        id: str | Omit = omit,
        crm: object | Omit = omit,
        default: Dict[str, object] | Omit = omit,
        extended: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
        """Patch object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._patch(
            path_template("/v2/prism/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                deal_update_params.DealUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )

    def delete(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/prism/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
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
        options: deal_bulk_create_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealBulkCreateResponse:
        """Import multiple objects in batch.

        Properties are keyed by slug. Automatically
        routes based on size: <100 records sync (immediate response), >=100 records
        async (S3/Lambda with WebSocket progress)

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
        return self._post(
            path_template("/v2/prism/{team_id}/deal/import", team_id=team_id),
            body=maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                deal_bulk_create_params.DealBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealBulkCreateResponse,
        )

    def duplicate(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealDuplicateResponse:
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._post(
            path_template("/v2/prism/{team_id}/deal/{deal_id}/duplicate", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealDuplicateResponse,
        )

    def get(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._get(
            path_template("/v2/prism/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )

    def query(
        self,
        *,
        team_id: str | None = None,
        query: deal_query_params.Query,
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
    ) -> DealQueryResponse:
        """
        Query v2

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
            path_template("/v2/prism/query/{team_id}/deal", team_id=team_id),
            body=maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                deal_query_params.DealQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealQueryResponse,
        )

    def restore(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._post(
            path_template("/v2/prism/{team_id}/deal/{deal_id}/restore", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )


class AsyncDealsResource(AsyncAPIResource):
    @cached_property
    def grant(self) -> AsyncGrantResource:
        return AsyncGrantResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncDealsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        team_id: str | None = None,
        id: str | Omit = omit,
        crm: object | Omit = omit,
        default: Dict[str, object] | Omit = omit,
        extended: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
        """Create object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null.

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
            path_template("/v2/prism/{team_id}/deal", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                deal_create_params.DealCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )

    async def update(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        id: str | Omit = omit,
        crm: object | Omit = omit,
        default: Dict[str, object] | Omit = omit,
        extended: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
        """Patch object

        Args:
          default: Properties keyed by property slug.

        Values can be strings, numbers, booleans,
              arrays, or null.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._patch(
            path_template("/v2/prism/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                deal_update_params.DealUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )

    async def delete(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/prism/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
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
        options: deal_bulk_create_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealBulkCreateResponse:
        """Import multiple objects in batch.

        Properties are keyed by slug. Automatically
        routes based on size: <100 records sync (immediate response), >=100 records
        async (S3/Lambda with WebSocket progress)

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
        return await self._post(
            path_template("/v2/prism/{team_id}/deal/import", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                deal_bulk_create_params.DealBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealBulkCreateResponse,
        )

    async def duplicate(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealDuplicateResponse:
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._post(
            path_template("/v2/prism/{team_id}/deal/{deal_id}/duplicate", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealDuplicateResponse,
        )

    async def get(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._get(
            path_template("/v2/prism/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )

    async def query(
        self,
        *,
        team_id: str | None = None,
        query: deal_query_params.Query,
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
    ) -> DealQueryResponse:
        """
        Query v2

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
            path_template("/v2/prism/query/{team_id}/deal", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                deal_query_params.DealQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealQueryResponse,
        )

    async def restore(
        self,
        deal_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismObjectProperties:
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
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._post(
            path_template("/v2/prism/{team_id}/deal/{deal_id}/restore", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismObjectProperties,
        )


class DealsResourceWithRawResponse:
    def __init__(self, deals: DealsResource) -> None:
        self._deals = deals

        self.create = to_raw_response_wrapper(
            deals.create,
        )
        self.update = to_raw_response_wrapper(
            deals.update,
        )
        self.delete = to_raw_response_wrapper(
            deals.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            deals.bulk_create,
        )
        self.duplicate = to_raw_response_wrapper(
            deals.duplicate,
        )
        self.get = to_raw_response_wrapper(
            deals.get,
        )
        self.query = to_raw_response_wrapper(
            deals.query,
        )
        self.restore = to_raw_response_wrapper(
            deals.restore,
        )

    @cached_property
    def grant(self) -> GrantResourceWithRawResponse:
        return GrantResourceWithRawResponse(self._deals.grant)


class AsyncDealsResourceWithRawResponse:
    def __init__(self, deals: AsyncDealsResource) -> None:
        self._deals = deals

        self.create = async_to_raw_response_wrapper(
            deals.create,
        )
        self.update = async_to_raw_response_wrapper(
            deals.update,
        )
        self.delete = async_to_raw_response_wrapper(
            deals.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            deals.bulk_create,
        )
        self.duplicate = async_to_raw_response_wrapper(
            deals.duplicate,
        )
        self.get = async_to_raw_response_wrapper(
            deals.get,
        )
        self.query = async_to_raw_response_wrapper(
            deals.query,
        )
        self.restore = async_to_raw_response_wrapper(
            deals.restore,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithRawResponse:
        return AsyncGrantResourceWithRawResponse(self._deals.grant)


class DealsResourceWithStreamingResponse:
    def __init__(self, deals: DealsResource) -> None:
        self._deals = deals

        self.create = to_streamed_response_wrapper(
            deals.create,
        )
        self.update = to_streamed_response_wrapper(
            deals.update,
        )
        self.delete = to_streamed_response_wrapper(
            deals.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            deals.bulk_create,
        )
        self.duplicate = to_streamed_response_wrapper(
            deals.duplicate,
        )
        self.get = to_streamed_response_wrapper(
            deals.get,
        )
        self.query = to_streamed_response_wrapper(
            deals.query,
        )
        self.restore = to_streamed_response_wrapper(
            deals.restore,
        )

    @cached_property
    def grant(self) -> GrantResourceWithStreamingResponse:
        return GrantResourceWithStreamingResponse(self._deals.grant)


class AsyncDealsResourceWithStreamingResponse:
    def __init__(self, deals: AsyncDealsResource) -> None:
        self._deals = deals

        self.create = async_to_streamed_response_wrapper(
            deals.create,
        )
        self.update = async_to_streamed_response_wrapper(
            deals.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            deals.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            deals.bulk_create,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            deals.duplicate,
        )
        self.get = async_to_streamed_response_wrapper(
            deals.get,
        )
        self.query = async_to_streamed_response_wrapper(
            deals.query,
        )
        self.restore = async_to_streamed_response_wrapper(
            deals.restore,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithStreamingResponse:
        return AsyncGrantResourceWithStreamingResponse(self._deals.grant)
