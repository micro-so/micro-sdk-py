# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.prism.objects.deals import grant_update_params
from .....types.prism.objects.deals.grant_get_response import GrantGetResponse
from .....types.prism.objects.deals.grant_update_response import GrantUpdateResponse

__all__ = ["GrantResource", "AsyncGrantResource"]


class GrantResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GrantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return GrantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GrantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return GrantResourceWithStreamingResponse(self)

    def update(
        self,
        deal_id: str,
        *,
        path_team_id: str | None = None,
        team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        body_team_id: Dict[str, Literal["a", "r", "w"]] | Omit = omit,
        user_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantUpdateResponse:
        """
        Update grant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._put(
            path_template("/v2/prism/grant/{path_team_id}/deal/{deal_id}", path_team_id=path_team_id, deal_id=deal_id),
            body=maybe_transform(
                {
                    "team_group_id": team_group_id,
                    "body_team_id": body_team_id,
                    "user_id": user_id,
                },
                grant_update_params.GrantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantUpdateResponse,
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
    ) -> GrantGetResponse:
        """
        Get grant

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
            path_template("/v2/prism/grant/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantGetResponse,
        )


class AsyncGrantResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGrantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGrantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGrantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncGrantResourceWithStreamingResponse(self)

    async def update(
        self,
        deal_id: str,
        *,
        path_team_id: str | None = None,
        team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        body_team_id: Dict[str, Literal["a", "r", "w"]] | Omit = omit,
        user_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GrantUpdateResponse:
        """
        Update grant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._put(
            path_template("/v2/prism/grant/{path_team_id}/deal/{deal_id}", path_team_id=path_team_id, deal_id=deal_id),
            body=await async_maybe_transform(
                {
                    "team_group_id": team_group_id,
                    "body_team_id": body_team_id,
                    "user_id": user_id,
                },
                grant_update_params.GrantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantUpdateResponse,
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
    ) -> GrantGetResponse:
        """
        Get grant

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
            path_template("/v2/prism/grant/{team_id}/deal/{deal_id}", team_id=team_id, deal_id=deal_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GrantGetResponse,
        )


class GrantResourceWithRawResponse:
    def __init__(self, grant: GrantResource) -> None:
        self._grant = grant

        self.update = to_raw_response_wrapper(
            grant.update,
        )
        self.get = to_raw_response_wrapper(
            grant.get,
        )


class AsyncGrantResourceWithRawResponse:
    def __init__(self, grant: AsyncGrantResource) -> None:
        self._grant = grant

        self.update = async_to_raw_response_wrapper(
            grant.update,
        )
        self.get = async_to_raw_response_wrapper(
            grant.get,
        )


class GrantResourceWithStreamingResponse:
    def __init__(self, grant: GrantResource) -> None:
        self._grant = grant

        self.update = to_streamed_response_wrapper(
            grant.update,
        )
        self.get = to_streamed_response_wrapper(
            grant.get,
        )


class AsyncGrantResourceWithStreamingResponse:
    def __init__(self, grant: AsyncGrantResource) -> None:
        self._grant = grant

        self.update = async_to_streamed_response_wrapper(
            grant.update,
        )
        self.get = async_to_streamed_response_wrapper(
            grant.get,
        )
