# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.prism.import_get_response import ImportGetResponse

__all__ = ["ImportsResource", "AsyncImportsResource"]


class ImportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return ImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return ImportsResourceWithStreamingResponse(self)

    def get(
        self,
        job_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportGetResponse:
        """Poll the status of an async import.

        Sync imports complete in the original
        response and don't appear here. Async jobs are retained for 7 days. Returns 404
        once the job has expired.

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
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/v2/prism/{team_id}/imports/{job_id}", team_id=team_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportGetResponse,
        )


class AsyncImportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncImportsResourceWithStreamingResponse(self)

    async def get(
        self,
        job_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportGetResponse:
        """Poll the status of an async import.

        Sync imports complete in the original
        response and don't appear here. Async jobs are retained for 7 days. Returns 404
        once the job has expired.

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
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/v2/prism/{team_id}/imports/{job_id}", team_id=team_id, job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportGetResponse,
        )


class ImportsResourceWithRawResponse:
    def __init__(self, imports: ImportsResource) -> None:
        self._imports = imports

        self.get = to_raw_response_wrapper(
            imports.get,
        )


class AsyncImportsResourceWithRawResponse:
    def __init__(self, imports: AsyncImportsResource) -> None:
        self._imports = imports

        self.get = async_to_raw_response_wrapper(
            imports.get,
        )


class ImportsResourceWithStreamingResponse:
    def __init__(self, imports: ImportsResource) -> None:
        self._imports = imports

        self.get = to_streamed_response_wrapper(
            imports.get,
        )


class AsyncImportsResourceWithStreamingResponse:
    def __init__(self, imports: AsyncImportsResource) -> None:
        self._imports = imports

        self.get = async_to_streamed_response_wrapper(
            imports.get,
        )
