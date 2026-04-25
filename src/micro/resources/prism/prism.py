# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PrismResource", "AsyncPrismResource"]


class PrismResource(SyncAPIResource):
    @cached_property
    def query(self) -> QueryResource:
        return QueryResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrismResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return PrismResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrismResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return PrismResourceWithStreamingResponse(self)


class AsyncPrismResource(AsyncAPIResource):
    @cached_property
    def query(self) -> AsyncQueryResource:
        return AsyncQueryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrismResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrismResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrismResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return AsyncPrismResourceWithStreamingResponse(self)


class PrismResourceWithRawResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self._prism.query)


class AsyncPrismResourceWithRawResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self._prism.query)


class PrismResourceWithStreamingResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self._prism.query)


class AsyncPrismResourceWithStreamingResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self._prism.query)
