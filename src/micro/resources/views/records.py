# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.views import record_list_params, record_reorder_params
from ..._base_client import make_request_options
from ...types.views.record_list_response import RecordListResponse

__all__ = ["RecordsResource", "AsyncRecordsResource"]


class RecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return RecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return RecordsResourceWithStreamingResponse(self)

    def list(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordListResponse:
        """
        List records selected by a view (filters and sorts applied; pinned record_order
        overlaid first)

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._get(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    record_list_params.RecordListParams,
                ),
            ),
            cast_to=RecordListResponse,
        )

    def pin(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Pin a record to the view (append to record_order)

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records/{object_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def reorder(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        object_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Bulk reorder pinned records

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            body=maybe_transform({"object_ids": object_ids}, record_reorder_params.RecordReorderParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unpin(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unpin a record from the view

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records/{object_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return AsyncRecordsResourceWithStreamingResponse(self)

    async def list(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordListResponse:
        """
        List records selected by a view (filters and sorts applied; pinned record_order
        overlaid first)

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._get(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    record_list_params.RecordListParams,
                ),
            ),
            cast_to=RecordListResponse,
        )

    async def pin(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Pin a record to the view (append to record_order)

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records/{object_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def reorder(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        object_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Bulk reorder pinned records

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            body=await async_maybe_transform({"object_ids": object_ids}, record_reorder_params.RecordReorderParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unpin(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Unpin a record from the view

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}/records/{object_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RecordsResourceWithRawResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.list = to_raw_response_wrapper(
            records.list,
        )
        self.pin = to_raw_response_wrapper(
            records.pin,
        )
        self.reorder = to_raw_response_wrapper(
            records.reorder,
        )
        self.unpin = to_raw_response_wrapper(
            records.unpin,
        )


class AsyncRecordsResourceWithRawResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.list = async_to_raw_response_wrapper(
            records.list,
        )
        self.pin = async_to_raw_response_wrapper(
            records.pin,
        )
        self.reorder = async_to_raw_response_wrapper(
            records.reorder,
        )
        self.unpin = async_to_raw_response_wrapper(
            records.unpin,
        )


class RecordsResourceWithStreamingResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.list = to_streamed_response_wrapper(
            records.list,
        )
        self.pin = to_streamed_response_wrapper(
            records.pin,
        )
        self.reorder = to_streamed_response_wrapper(
            records.reorder,
        )
        self.unpin = to_streamed_response_wrapper(
            records.unpin,
        )


class AsyncRecordsResourceWithStreamingResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.list = async_to_streamed_response_wrapper(
            records.list,
        )
        self.pin = async_to_streamed_response_wrapper(
            records.pin,
        )
        self.reorder = async_to_streamed_response_wrapper(
            records.reorder,
        )
        self.unpin = async_to_streamed_response_wrapper(
            records.unpin,
        )
