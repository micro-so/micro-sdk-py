# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .import_jobs import (
    ImportJobsResource,
    AsyncImportJobsResource,
    ImportJobsResourceWithRawResponse,
    AsyncImportJobsResourceWithRawResponse,
    ImportJobsResourceWithStreamingResponse,
    AsyncImportJobsResourceWithStreamingResponse,
)
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
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def import_jobs(self) -> ImportJobsResource:
        return ImportJobsResource(self._client)

    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrismResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return PrismResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrismResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return PrismResourceWithStreamingResponse(self)


class AsyncPrismResource(AsyncAPIResource):
    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def import_jobs(self) -> AsyncImportJobsResource:
        return AsyncImportJobsResource(self._client)

    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrismResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPrismResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrismResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncPrismResourceWithStreamingResponse(self)


class PrismResourceWithRawResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._prism.properties)

    @cached_property
    def import_jobs(self) -> ImportJobsResourceWithRawResponse:
        return ImportJobsResourceWithRawResponse(self._prism.import_jobs)

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._prism.objects)


class AsyncPrismResourceWithRawResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._prism.properties)

    @cached_property
    def import_jobs(self) -> AsyncImportJobsResourceWithRawResponse:
        return AsyncImportJobsResourceWithRawResponse(self._prism.import_jobs)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._prism.objects)


class PrismResourceWithStreamingResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._prism.properties)

    @cached_property
    def import_jobs(self) -> ImportJobsResourceWithStreamingResponse:
        return ImportJobsResourceWithStreamingResponse(self._prism.import_jobs)

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._prism.objects)


class AsyncPrismResourceWithStreamingResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._prism.properties)

    @cached_property
    def import_jobs(self) -> AsyncImportJobsResourceWithStreamingResponse:
        return AsyncImportJobsResourceWithStreamingResponse(self._prism.import_jobs)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._prism.objects)
