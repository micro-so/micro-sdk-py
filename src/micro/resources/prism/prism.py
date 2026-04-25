# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from .grant import (
    GrantResource,
    AsyncGrantResource,
    GrantResourceWithRawResponse,
    AsyncGrantResourceWithRawResponse,
    GrantResourceWithStreamingResponse,
    AsyncGrantResourceWithStreamingResponse,
)
from .query import (
    QueryResource,
    AsyncQueryResource,
    QueryResourceWithRawResponse,
    AsyncQueryResourceWithRawResponse,
    QueryResourceWithStreamingResponse,
    AsyncQueryResourceWithStreamingResponse,
)
from ...types import ObjectType, prism_patch_object_params, prism_create_object_params, prism_import_objects_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.object_type import ObjectType
from ...types.prism_import_objects_response import PrismImportObjectsResponse
from ...types.prism_object_properties_param import PrismObjectPropertiesParam
from ...types.prism_duplicate_object_response import PrismDuplicateObjectResponse

__all__ = ["PrismResource", "AsyncPrismResource"]


class PrismResource(SyncAPIResource):
    """
    The Prism query engine provides generic read/write access to any object type using a single unified API surface.
    """

    @cached_property
    def grant(self) -> GrantResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return GrantResource(self._client)

    @cached_property
    def query(self) -> QueryResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return QueryResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return MetadataResource(self._client)

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

    def create_object(
        self,
        object_type: ObjectType,
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
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v2/prism/{team_id}/{object_type}", team_id=team_id, object_type=object_type),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                prism_create_object_params.PrismCreateObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_object(
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def duplicate_object(
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
    ) -> PrismDuplicateObjectResponse:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}/duplicate",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismDuplicateObjectResponse,
        )

    def import_objects(
        self,
        object_type: Literal["identity", "organization", "contact", "action", "document", "deal"],
        *,
        team_id: str | None = None,
        objects: Iterable[PrismObjectPropertiesParam],
        options: prism_import_objects_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismImportObjectsResponse:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            path_template("/v2/prism/{team_id}/{object_type}/import", team_id=team_id, object_type=object_type),
            body=maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                prism_import_objects_params.PrismImportObjectsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismImportObjectsResponse,
        )

    def patch_object(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        object_type: ObjectType,
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
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                prism_patch_object_params.PrismPatchObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def restore_object(
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}/restore",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPrismResource(AsyncAPIResource):
    """
    The Prism query engine provides generic read/write access to any object type using a single unified API surface.
    """

    @cached_property
    def grant(self) -> AsyncGrantResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncGrantResource(self._client)

    @cached_property
    def query(self) -> AsyncQueryResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncQueryResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncMetadataResource(self._client)

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

    async def create_object(
        self,
        object_type: ObjectType,
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
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v2/prism/{team_id}/{object_type}", team_id=team_id, object_type=object_type),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                prism_create_object_params.PrismCreateObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_object(
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def duplicate_object(
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
    ) -> PrismDuplicateObjectResponse:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}/duplicate",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismDuplicateObjectResponse,
        )

    async def import_objects(
        self,
        object_type: Literal["identity", "organization", "contact", "action", "document", "deal"],
        *,
        team_id: str | None = None,
        objects: Iterable[PrismObjectPropertiesParam],
        options: prism_import_objects_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrismImportObjectsResponse:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            path_template("/v2/prism/{team_id}/{object_type}/import", team_id=team_id, object_type=object_type),
            body=await async_maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                prism_import_objects_params.PrismImportObjectsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrismImportObjectsResponse,
        )

    async def patch_object(
        self,
        object_id: str,
        *,
        team_id: str | None = None,
        object_type: ObjectType,
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
    ) -> None:
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                prism_patch_object_params.PrismPatchObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def restore_object(
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
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v2/prism/{team_id}/{object_type}/{object_id}/restore",
                team_id=team_id,
                object_type=object_type,
                object_id=object_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PrismResourceWithRawResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

        self.create_object = to_raw_response_wrapper(
            prism.create_object,
        )
        self.delete_object = to_raw_response_wrapper(
            prism.delete_object,
        )
        self.duplicate_object = to_raw_response_wrapper(
            prism.duplicate_object,
        )
        self.import_objects = to_raw_response_wrapper(
            prism.import_objects,
        )
        self.patch_object = to_raw_response_wrapper(
            prism.patch_object,
        )
        self.restore_object = to_raw_response_wrapper(
            prism.restore_object,
        )

    @cached_property
    def grant(self) -> GrantResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return GrantResourceWithRawResponse(self._prism.grant)

    @cached_property
    def query(self) -> QueryResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return QueryResourceWithRawResponse(self._prism.query)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return MetadataResourceWithRawResponse(self._prism.metadata)


class AsyncPrismResourceWithRawResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

        self.create_object = async_to_raw_response_wrapper(
            prism.create_object,
        )
        self.delete_object = async_to_raw_response_wrapper(
            prism.delete_object,
        )
        self.duplicate_object = async_to_raw_response_wrapper(
            prism.duplicate_object,
        )
        self.import_objects = async_to_raw_response_wrapper(
            prism.import_objects,
        )
        self.patch_object = async_to_raw_response_wrapper(
            prism.patch_object,
        )
        self.restore_object = async_to_raw_response_wrapper(
            prism.restore_object,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncGrantResourceWithRawResponse(self._prism.grant)

    @cached_property
    def query(self) -> AsyncQueryResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncQueryResourceWithRawResponse(self._prism.query)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncMetadataResourceWithRawResponse(self._prism.metadata)


class PrismResourceWithStreamingResponse:
    def __init__(self, prism: PrismResource) -> None:
        self._prism = prism

        self.create_object = to_streamed_response_wrapper(
            prism.create_object,
        )
        self.delete_object = to_streamed_response_wrapper(
            prism.delete_object,
        )
        self.duplicate_object = to_streamed_response_wrapper(
            prism.duplicate_object,
        )
        self.import_objects = to_streamed_response_wrapper(
            prism.import_objects,
        )
        self.patch_object = to_streamed_response_wrapper(
            prism.patch_object,
        )
        self.restore_object = to_streamed_response_wrapper(
            prism.restore_object,
        )

    @cached_property
    def grant(self) -> GrantResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return GrantResourceWithStreamingResponse(self._prism.grant)

    @cached_property
    def query(self) -> QueryResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return QueryResourceWithStreamingResponse(self._prism.query)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return MetadataResourceWithStreamingResponse(self._prism.metadata)


class AsyncPrismResourceWithStreamingResponse:
    def __init__(self, prism: AsyncPrismResource) -> None:
        self._prism = prism

        self.create_object = async_to_streamed_response_wrapper(
            prism.create_object,
        )
        self.delete_object = async_to_streamed_response_wrapper(
            prism.delete_object,
        )
        self.duplicate_object = async_to_streamed_response_wrapper(
            prism.duplicate_object,
        )
        self.import_objects = async_to_streamed_response_wrapper(
            prism.import_objects,
        )
        self.patch_object = async_to_streamed_response_wrapper(
            prism.patch_object,
        )
        self.restore_object = async_to_streamed_response_wrapper(
            prism.restore_object,
        )

    @cached_property
    def grant(self) -> AsyncGrantResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncGrantResourceWithStreamingResponse(self._prism.grant)

    @cached_property
    def query(self) -> AsyncQueryResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncQueryResourceWithStreamingResponse(self._prism.query)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        return AsyncMetadataResourceWithStreamingResponse(self._prism.metadata)
