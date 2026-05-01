# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .objects.objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)

__all__ = ["PrismResource", "AsyncPrismResource"]


class PrismResource(SyncAPIResource):
    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

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
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

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
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._prism.metadata)

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._prism.objects)


class AsyncPrismResourceWithRawResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._prism.metadata)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._prism.objects)


class PrismResourceWithStreamingResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._prism.metadata)

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._prism.objects)


class AsyncPrismResourceWithStreamingResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._prism.metadata)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._prism.objects)
