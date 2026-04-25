# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ...types import ObjectType
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.prism import grant_update_grant_params
from ..._base_client import make_request_options
from ...types.object_type import ObjectType

__all__ = ["GrantResource", "AsyncGrantResource"]


class GrantResource(SyncAPIResource):
    """
    The Prism query engine provides generic read/write access to any object type using a single unified API surface.
    """

    @cached_property
    def with_raw_response(self) -> GrantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return GrantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GrantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return GrantResourceWithStreamingResponse(self)

    def retrieve_grant(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        object_type: ObjectType,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/v2/prism/grant/{team_id}/{object_type}/{object_id}",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_grant(
        self,
        object_id: str,
        *,
        path_team_id: str | None = None,
        object_type: ObjectType,
        team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        body_team_id: Dict[str, Literal["a", "r", "w"]] | Omit = omit,
        user_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template(
                "/v2/prism/grant/{path_team_id}/{object_type}/{object_id}",
                path_team_id=path_team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            body=maybe_transform(
                {
                    "team_group_id": team_group_id,
                    "body_team_id": body_team_id,
                    "user_id": user_id,
                },
                grant_update_grant_params.GrantUpdateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGrantResource(AsyncAPIResource):
    """
    The Prism query engine provides generic read/write access to any object type using a single unified API surface.
    """

    @cached_property
    def with_raw_response(self) -> AsyncGrantResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGrantResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGrantResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return AsyncGrantResourceWithStreamingResponse(self)

    async def retrieve_grant(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        object_type: ObjectType,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v2/prism/grant/{team_id}/{object_type}/{object_id}",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_grant(
        self,
        object_id: str,
        *,
        path_team_id: str | None = None,
        object_type: ObjectType,
        team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        body_team_id: Dict[str, Literal["a", "r", "w"]] | Omit = omit,
        user_id: Iterable[Dict[str, Literal["a", "r", "w"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/v2/prism/grant/{path_team_id}/{object_type}/{object_id}",
                path_team_id=path_team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            body=await async_maybe_transform(
                {
                    "team_group_id": team_group_id,
                    "body_team_id": body_team_id,
                    "user_id": user_id,
                },
                grant_update_grant_params.GrantUpdateGrantParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GrantResourceWithRawResponse:
    def __init__(self, grant: GrantResource) -> None:
        self._grant = grant

        self.retrieve_grant = to_raw_response_wrapper(
            grant.retrieve_grant,
        )
        self.update_grant = to_raw_response_wrapper(
            grant.update_grant,
        )


class AsyncGrantResourceWithRawResponse:
    def __init__(self, grant: AsyncGrantResource) -> None:
        self._grant = grant

        self.retrieve_grant = async_to_raw_response_wrapper(
            grant.retrieve_grant,
        )
        self.update_grant = async_to_raw_response_wrapper(
            grant.update_grant,
        )


class GrantResourceWithStreamingResponse:
    def __init__(self, grant: GrantResource) -> None:
        self._grant = grant

        self.retrieve_grant = to_streamed_response_wrapper(
            grant.retrieve_grant,
        )
        self.update_grant = to_streamed_response_wrapper(
            grant.update_grant,
        )


class AsyncGrantResourceWithStreamingResponse:
    def __init__(self, grant: AsyncGrantResource) -> None:
        self._grant = grant

        self.retrieve_grant = async_to_streamed_response_wrapper(
            grant.retrieve_grant,
        )
        self.update_grant = async_to_streamed_response_wrapper(
            grant.update_grant,
        )
