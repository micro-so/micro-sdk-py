# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.webhooks import delivery_list_params
from ...types.webhook_delivery_detail import WebhookDeliveryDetail
from ...types.webhooks.delivery_list_response import DeliveryListResponse

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)

    def list(
        self,
        webhook_id: str,
        *,
        team_id: str | None = None,
        after: Union[str, datetime] | Omit = omit,
        before: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["success", "failed"] | Omit = omit,
        type: Literal["delivery", "verification", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        An endpoint's deliveries, newest first, with optional status / type / time-range
        filters and cursor pagination.

        Args:
          after: Only deliveries at or after this ISO-8601 timestamp.

          before: Only deliveries at or before this ISO-8601 timestamp.

          cursor: Opaque cursor from a previous response's `next_cursor`.

          limit: Page size (1–100, default 25).

          status: Filter by outcome.

          type: Filter by run type. Defaults to `delivery` (event deliveries). Pass `all` to
              include verification handshakes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            path_template("/v2/webhooks/{team_id}/{webhook_id}/deliveries", team_id=team_id, webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "type": type,
                    },
                    delivery_list_params.DeliveryListParams,
                ),
            ),
            cast_to=DeliveryListResponse,
        )

    def get(
        self,
        delivery_id: str,
        *,
        team_id: str | None = None,
        webhook_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeliveryDetail:
        """
        A single delivery plus its full attempt timeline (including async retries).

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
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            path_template(
                "/v2/webhooks/{team_id}/{webhook_id}/deliveries/{delivery_id}",
                team_id=team_id,
                webhook_id=webhook_id,
                delivery_id=delivery_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeliveryDetail,
        )


class AsyncDeliveriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)

    async def list(
        self,
        webhook_id: str,
        *,
        team_id: str | None = None,
        after: Union[str, datetime] | Omit = omit,
        before: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["success", "failed"] | Omit = omit,
        type: Literal["delivery", "verification", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        An endpoint's deliveries, newest first, with optional status / type / time-range
        filters and cursor pagination.

        Args:
          after: Only deliveries at or after this ISO-8601 timestamp.

          before: Only deliveries at or before this ISO-8601 timestamp.

          cursor: Opaque cursor from a previous response's `next_cursor`.

          limit: Page size (1–100, default 25).

          status: Filter by outcome.

          type: Filter by run type. Defaults to `delivery` (event deliveries). Pass `all` to
              include verification handshakes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if team_id is None:
            team_id = self._client._get_team_id_path_param()
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            path_template("/v2/webhooks/{team_id}/{webhook_id}/deliveries", team_id=team_id, webhook_id=webhook_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "type": type,
                    },
                    delivery_list_params.DeliveryListParams,
                ),
            ),
            cast_to=DeliveryListResponse,
        )

    async def get(
        self,
        delivery_id: str,
        *,
        team_id: str | None = None,
        webhook_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeliveryDetail:
        """
        A single delivery plus its full attempt timeline (including async retries).

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
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            path_template(
                "/v2/webhooks/{team_id}/{webhook_id}/deliveries/{delivery_id}",
                team_id=team_id,
                webhook_id=webhook_id,
                delivery_id=delivery_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeliveryDetail,
        )


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = to_raw_response_wrapper(
            deliveries.list,
        )
        self.get = to_raw_response_wrapper(
            deliveries.get,
        )


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = async_to_raw_response_wrapper(
            deliveries.list,
        )
        self.get = async_to_raw_response_wrapper(
            deliveries.get,
        )


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = to_streamed_response_wrapper(
            deliveries.list,
        )
        self.get = to_streamed_response_wrapper(
            deliveries.get,
        )


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.list = async_to_streamed_response_wrapper(
            deliveries.list,
        )
        self.get = async_to_streamed_response_wrapper(
            deliveries.get,
        )
