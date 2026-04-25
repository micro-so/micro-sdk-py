# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import (
    organization_list_params,
    organization_create_params,
    organization_import_params,
    organization_update_params,
)
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
from ..types.organization_list_response import OrganizationListResponse
from ..types.organization_create_response import OrganizationCreateResponse
from ..types.organization_import_response import OrganizationImportResponse
from ..types.prism_object_properties_param import PrismObjectPropertiesParam

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

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
    ) -> OrganizationCreateResponse:
        """Create Organization

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
            path_template("/v2/prism/{team_id}/organization", team_id=team_id),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationCreateResponse,
        )

    def update(
        self,
        organization_id: str,
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
        """Update Organization

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template(
                "/v2/prism/{team_id}/organization/{organization_id}", team_id=team_id, organization_id=organization_id
            ),
            body=maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                organization_update_params.OrganizationUpdateParams,
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
        query: organization_list_params.Query,
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
    ) -> OrganizationListResponse:
        """
        List Organizations

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
            path_template("/v2/prism/query/{team_id}/organization", team_id=team_id),
            body=maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                organization_list_params.OrganizationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListResponse,
        )

    def delete(
        self,
        organization_id: str,
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
        Delete Organization

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/organization/{organization_id}", team_id=team_id, organization_id=organization_id
            ),
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
        options: organization_import_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationImportResponse:
        """
        Import Organizations

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
            path_template("/v2/prism/{team_id}/organization/import", team_id=team_id),
            body=maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                organization_import_params.OrganizationImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationImportResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/micro-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/micro-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

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
    ) -> OrganizationCreateResponse:
        """Create Organization

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
            path_template("/v2/prism/{team_id}/organization", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationCreateResponse,
        )

    async def update(
        self,
        organization_id: str,
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
        """Update Organization

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template(
                "/v2/prism/{team_id}/organization/{organization_id}", team_id=team_id, organization_id=organization_id
            ),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "crm": crm,
                    "default": default,
                    "extended": extended,
                },
                organization_update_params.OrganizationUpdateParams,
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
        query: organization_list_params.Query,
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
    ) -> OrganizationListResponse:
        """
        List Organizations

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
            path_template("/v2/prism/query/{team_id}/organization", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "id": id,
                    "boxes": boxes,
                    "deleted": deleted,
                    "sources": sources,
                },
                organization_list_params.OrganizationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationListResponse,
        )

    async def delete(
        self,
        organization_id: str,
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
        Delete Organization

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/organization/{organization_id}", team_id=team_id, organization_id=organization_id
            ),
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
        options: organization_import_params.Options | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationImportResponse:
        """
        Import Organizations

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
            path_template("/v2/prism/{team_id}/organization/import", team_id=team_id),
            body=await async_maybe_transform(
                {
                    "objects": objects,
                    "options": options,
                },
                organization_import_params.OrganizationImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationImportResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = to_raw_response_wrapper(
            organizations.delete,
        )
        self.import_ = to_raw_response_wrapper(
            organizations.import_,
        )


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            organizations.delete,
        )
        self.import_ = async_to_raw_response_wrapper(
            organizations.import_,
        )


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = to_streamed_response_wrapper(
            organizations.delete,
        )
        self.import_ = to_streamed_response_wrapper(
            organizations.import_,
        )


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            organizations.delete,
        )
        self.import_ = async_to_streamed_response_wrapper(
            organizations.import_,
        )
