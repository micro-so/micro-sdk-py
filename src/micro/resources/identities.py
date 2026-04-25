# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import identity_list_params, identity_create_params, identity_import_params, identity_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.identity_list_response import IdentityListResponse
from ..types.identity_create_response import IdentityCreateResponse
from ..types.identity_import_response import IdentityImportResponse
from ..types.prism_object_properties_param import PrismObjectPropertiesParam

__all__ = ["IdentitiesResource", "AsyncIdentitiesResource"]


class IdentitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return IdentitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return IdentitiesResourceWithStreamingResponse(self)

    def create(
        self,
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
    ) -> IdentityCreateResponse:
        """Create Identity

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
        return self._post(
            path_template("/v2/prism/{team_id}/identity", team_id=team_id),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                identity_create_params.IdentityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityCreateResponse,
        )

    def update(
        self,
        identity_id: str,
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
        """Update Identity

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
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/v2/prism/{team_id}/identity/{identity_id}", team_id=team_id, identity_id=identity_id),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                identity_update_params.IdentityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        team_id: str | None = None,
        query: identity_list_params.Query,
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
    ) -> IdentityListResponse:
        """
        List Identitys

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
            path_template("/v2/prism/query/{team_id}/identity", team_id=team_id),
            body=maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                identity_list_params.IdentityListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityListResponse,
        )

    def delete(
        self,
        identity_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Identity

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
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v2/prism/{team_id}/identity/{identity_id}", team_id=team_id, identity_id=identity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def import_(
        self,
        *,
        team_id: str | None = None,
        objects: Iterable[PrismObjectPropertiesParam],
        options: identity_import_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityImportResponse:
        """
        Import Identitys

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
        return self._post(
            path_template("/v2/prism/{team_id}/identity/import", team_id=team_id),
            body=maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                identity_import_params.IdentityImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityImportResponse,
        )


class AsyncIdentitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return AsyncIdentitiesResourceWithStreamingResponse(self)

    async def create(
        self,
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
    ) -> IdentityCreateResponse:
        """Create Identity

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
        return await self._post(
            path_template("/v2/prism/{team_id}/identity", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                identity_create_params.IdentityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityCreateResponse,
        )

    async def update(
        self,
        identity_id: str,
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
        """Update Identity

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
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/v2/prism/{team_id}/identity/{identity_id}", team_id=team_id, identity_id=identity_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                identity_update_params.IdentityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        team_id: str | None = None,
        query: identity_list_params.Query,
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
    ) -> IdentityListResponse:
        """
        List Identitys

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
            path_template("/v2/prism/query/{team_id}/identity", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                identity_list_params.IdentityListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityListResponse,
        )

    async def delete(
        self,
        identity_id: str,
        *,
        team_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Identity

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
        if not identity_id:
            raise ValueError(f"Expected a non-empty value for `identity_id` but received {identity_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v2/prism/{team_id}/identity/{identity_id}", team_id=team_id, identity_id=identity_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def import_(
        self,
        *,
        team_id: str | None = None,
        objects: Iterable[PrismObjectPropertiesParam],
        options: identity_import_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IdentityImportResponse:
        """
        Import Identitys

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
        return await self._post(
            path_template("/v2/prism/{team_id}/identity/import", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                identity_import_params.IdentityImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityImportResponse,
        )


class IdentitiesResourceWithRawResponse:
    def __init__(self, identities: IdentitiesResource) -> None:
        self._identities = identities

        self.create = to_raw_response_wrapper(
            identities.create,
        )
        self.update = to_raw_response_wrapper(
            identities.update,
        )
        self.list = to_raw_response_wrapper(
            identities.list,
        )
        self.delete = to_raw_response_wrapper(
            identities.delete,
        )
        self.import_ = to_raw_response_wrapper(
            identities.import_,
        )


class AsyncIdentitiesResourceWithRawResponse:
    def __init__(self, identities: AsyncIdentitiesResource) -> None:
        self._identities = identities

        self.create = async_to_raw_response_wrapper(
            identities.create,
        )
        self.update = async_to_raw_response_wrapper(
            identities.update,
        )
        self.list = async_to_raw_response_wrapper(
            identities.list,
        )
        self.delete = async_to_raw_response_wrapper(
            identities.delete,
        )
        self.import_ = async_to_raw_response_wrapper(
            identities.import_,
        )


class IdentitiesResourceWithStreamingResponse:
    def __init__(self, identities: IdentitiesResource) -> None:
        self._identities = identities

        self.create = to_streamed_response_wrapper(
            identities.create,
        )
        self.update = to_streamed_response_wrapper(
            identities.update,
        )
        self.list = to_streamed_response_wrapper(
            identities.list,
        )
        self.delete = to_streamed_response_wrapper(
            identities.delete,
        )
        self.import_ = to_streamed_response_wrapper(
            identities.import_,
        )


class AsyncIdentitiesResourceWithStreamingResponse:
    def __init__(self, identities: AsyncIdentitiesResource) -> None:
        self._identities = identities

        self.create = async_to_streamed_response_wrapper(
            identities.create,
        )
        self.update = async_to_streamed_response_wrapper(
            identities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            identities.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            identities.delete,
        )
        self.import_ = async_to_streamed_response_wrapper(
            identities.import_,
        )
