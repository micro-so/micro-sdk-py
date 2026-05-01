# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.prism.objects import organization_query_params
from ....types.prism.objects.organization_query_response import OrganizationQueryResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        team_id: str | None = None,
        query: organization_query_params.Query,
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
    ) -> OrganizationQueryResponse:
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
            path_template("/v2/prism/query/{team_id}/organization", team_id=team_id),
            body=maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                organization_query_params.OrganizationQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationQueryResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        team_id: str | None = None,
        query: organization_query_params.Query,
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
    ) -> OrganizationQueryResponse:
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
            path_template("/v2/prism/query/{team_id}/organization", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                organization_query_params.OrganizationQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationQueryResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.query = to_raw_response_wrapper(
            organizations.query,
        )


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.query = async_to_raw_response_wrapper(
            organizations.query,
        )


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.query = to_streamed_response_wrapper(
            organizations.query,
        )


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.query = async_to_streamed_response_wrapper(
            organizations.query,
        )
