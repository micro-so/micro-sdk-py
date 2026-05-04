# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import view_create_params, view_update_params
from .records import (
    RecordsResource,
    AsyncRecordsResource,
    RecordsResourceWithRawResponse,
    AsyncRecordsResourceWithRawResponse,
    RecordsResourceWithStreamingResponse,
    AsyncRecordsResourceWithStreamingResponse,
)
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
from ..._base_client import make_request_options
from ...types.view_get_response import ViewGetResponse
from ...types.view_create_response import ViewCreateResponse
from ...types.view_update_response import ViewUpdateResponse

__all__ = ["ViewsResource", "AsyncViewsResource"]


class ViewsResource(SyncAPIResource):
    @cached_property
    def records(self) -> RecordsResource:
        return RecordsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return ViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return ViewsResourceWithStreamingResponse(self)

    def create(
        self,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        *,
        path_team_id: str | None = None,
        name: str,
        view_type: str,
        id: str | Omit = omit,
        aggregation_prop_def_id: Optional[str] | Omit = omit,
        aggregation_type: Optional[str] | Omit = omit,
        column_layout: Optional[Dict[str, object]] | Omit = omit,
        combinator: Literal["AND", "OR"] | Omit = omit,
        created_at: str | Omit = omit,
        crm_id: Optional[str] | Omit = omit,
        filter: Iterable[Dict[str, object]] | Omit = omit,
        group_by: Optional[str] | Omit = omit,
        group_hidden_option_ids: Union[Iterable[object], object, None] | Omit = omit,
        group_hide_empty: Optional[bool] | Omit = omit,
        group_sort: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        select: SequenceNotStr[str] | Omit = omit,
        sort: Iterable[Dict[str, object]] | Omit = omit,
        sort_order: Optional[int] | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        updated_at: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewCreateResponse:
        """
        Create a view bundle (view + select/filter/sort)

        Args:
          filter: Each entry is { slug: { comparator: value } }

          group_by: Property slug to group by

          select: Property slugs (dot-paths permitted for refs)

          sort: Each entry is { slug: 'asc' | 'desc' }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        return self._post(
            path_template(
                "/v2/prism/{path_team_id}/view/{view_object_type}",
                path_team_id=path_team_id,
                view_object_type=view_object_type,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "view_type": view_type,
                    "id": id,
                    "aggregation_prop_def_id": aggregation_prop_def_id,
                    "aggregation_type": aggregation_type,
                    "column_layout": column_layout,
                    "combinator": combinator,
                    "created_at": created_at,
                    "crm_id": crm_id,
                    "filter": filter,
                    "group_by": group_by,
                    "group_hidden_option_ids": group_hidden_option_ids,
                    "group_hide_empty": group_hide_empty,
                    "group_sort": group_sort,
                    "icon": icon,
                    "select": select,
                    "sort": sort,
                    "sort_order": sort_order,
                    "body_team_id": body_team_id,
                    "updated_at": updated_at,
                    "user_id": user_id,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewCreateResponse,
        )

    def update(
        self,
        view_id: str,
        *,
        path_team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        aggregation_prop_def_id: Optional[str] | Omit = omit,
        aggregation_type: Optional[str] | Omit = omit,
        column_layout: Optional[Dict[str, object]] | Omit = omit,
        combinator: Literal["AND", "OR"] | Omit = omit,
        crm_id: Optional[str] | Omit = omit,
        filter: Iterable[Dict[str, object]] | Omit = omit,
        group_by: Optional[str] | Omit = omit,
        group_hidden_option_ids: Union[Iterable[object], object, None] | Omit = omit,
        group_hide_empty: Optional[bool] | Omit = omit,
        group_sort: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        select: SequenceNotStr[str] | Omit = omit,
        sort: Iterable[Dict[str, object]] | Omit = omit,
        sort_order: Optional[int] | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        view_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewUpdateResponse:
        """
        Update a view bundle (select/filter/sort arrays are replaced wholesale when
        supplied)

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._patch(
            path_template(
                "/v2/prism/{path_team_id}/view/{view_object_type}/{view_id}",
                path_team_id=path_team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            body=maybe_transform(
                {
                    "aggregation_prop_def_id": aggregation_prop_def_id,
                    "aggregation_type": aggregation_type,
                    "column_layout": column_layout,
                    "combinator": combinator,
                    "crm_id": crm_id,
                    "filter": filter,
                    "group_by": group_by,
                    "group_hidden_option_ids": group_hidden_option_ids,
                    "group_hide_empty": group_hide_empty,
                    "group_sort": group_sort,
                    "icon": icon,
                    "name": name,
                    "select": select,
                    "sort": sort,
                    "sort_order": sort_order,
                    "body_team_id": body_team_id,
                    "user_id": user_id,
                    "view_type": view_type,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewUpdateResponse,
        )

    def delete(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a view bundle

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
        return self._delete(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewGetResponse:
        """
        Read a view bundle

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
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewGetResponse,
        )


class AsyncViewsResource(AsyncAPIResource):
    @cached_property
    def records(self) -> AsyncRecordsResource:
        return AsyncRecordsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncViewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncViewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/micro-so/micro-sdk-py#with_streaming_response
        """
        return AsyncViewsResourceWithStreamingResponse(self)

    async def create(
        self,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        *,
        path_team_id: str | None = None,
        name: str,
        view_type: str,
        id: str | Omit = omit,
        aggregation_prop_def_id: Optional[str] | Omit = omit,
        aggregation_type: Optional[str] | Omit = omit,
        column_layout: Optional[Dict[str, object]] | Omit = omit,
        combinator: Literal["AND", "OR"] | Omit = omit,
        created_at: str | Omit = omit,
        crm_id: Optional[str] | Omit = omit,
        filter: Iterable[Dict[str, object]] | Omit = omit,
        group_by: Optional[str] | Omit = omit,
        group_hidden_option_ids: Union[Iterable[object], object, None] | Omit = omit,
        group_hide_empty: Optional[bool] | Omit = omit,
        group_sort: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        select: SequenceNotStr[str] | Omit = omit,
        sort: Iterable[Dict[str, object]] | Omit = omit,
        sort_order: Optional[int] | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        updated_at: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewCreateResponse:
        """
        Create a view bundle (view + select/filter/sort)

        Args:
          filter: Each entry is { slug: { comparator: value } }

          group_by: Property slug to group by

          select: Property slugs (dot-paths permitted for refs)

          sort: Each entry is { slug: 'asc' | 'desc' }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if path_team_id is None:
            path_team_id = self._client._get_team_id_path_param()
        if not path_team_id:
            raise ValueError(f"Expected a non-empty value for `path_team_id` but received {path_team_id!r}")
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        return await self._post(
            path_template(
                "/v2/prism/{path_team_id}/view/{view_object_type}",
                path_team_id=path_team_id,
                view_object_type=view_object_type,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "view_type": view_type,
                    "id": id,
                    "aggregation_prop_def_id": aggregation_prop_def_id,
                    "aggregation_type": aggregation_type,
                    "column_layout": column_layout,
                    "combinator": combinator,
                    "created_at": created_at,
                    "crm_id": crm_id,
                    "filter": filter,
                    "group_by": group_by,
                    "group_hidden_option_ids": group_hidden_option_ids,
                    "group_hide_empty": group_hide_empty,
                    "group_sort": group_sort,
                    "icon": icon,
                    "select": select,
                    "sort": sort,
                    "sort_order": sort_order,
                    "body_team_id": body_team_id,
                    "updated_at": updated_at,
                    "user_id": user_id,
                },
                view_create_params.ViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewCreateResponse,
        )

    async def update(
        self,
        view_id: str,
        *,
        path_team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        aggregation_prop_def_id: Optional[str] | Omit = omit,
        aggregation_type: Optional[str] | Omit = omit,
        column_layout: Optional[Dict[str, object]] | Omit = omit,
        combinator: Literal["AND", "OR"] | Omit = omit,
        crm_id: Optional[str] | Omit = omit,
        filter: Iterable[Dict[str, object]] | Omit = omit,
        group_by: Optional[str] | Omit = omit,
        group_hidden_option_ids: Union[Iterable[object], object, None] | Omit = omit,
        group_hide_empty: Optional[bool] | Omit = omit,
        group_sort: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        select: SequenceNotStr[str] | Omit = omit,
        sort: Iterable[Dict[str, object]] | Omit = omit,
        sort_order: Optional[int] | Omit = omit,
        body_team_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        view_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewUpdateResponse:
        """
        Update a view bundle (select/filter/sort arrays are replaced wholesale when
        supplied)

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
        if not view_object_type:
            raise ValueError(f"Expected a non-empty value for `view_object_type` but received {view_object_type!r}")
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._patch(
            path_template(
                "/v2/prism/{path_team_id}/view/{view_object_type}/{view_id}",
                path_team_id=path_team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            body=await async_maybe_transform(
                {
                    "aggregation_prop_def_id": aggregation_prop_def_id,
                    "aggregation_type": aggregation_type,
                    "column_layout": column_layout,
                    "combinator": combinator,
                    "crm_id": crm_id,
                    "filter": filter,
                    "group_by": group_by,
                    "group_hidden_option_ids": group_hidden_option_ids,
                    "group_hide_empty": group_hide_empty,
                    "group_sort": group_sort,
                    "icon": icon,
                    "name": name,
                    "select": select,
                    "sort": sort,
                    "sort_order": sort_order,
                    "body_team_id": body_team_id,
                    "user_id": user_id,
                    "view_type": view_type,
                },
                view_update_params.ViewUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewUpdateResponse,
        )

    async def delete(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a view bundle

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
        return await self._delete(
            path_template(
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        view_id: str,
        *,
        team_id: str | None = None,
        view_object_type: Literal["action", "deal", "document", "event", "identity", "organization"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ViewGetResponse:
        """
        Read a view bundle

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
                "/v2/prism/{team_id}/view/{view_object_type}/{view_id}",
                team_id=team_id,
                view_object_type=view_object_type,
                view_id=view_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewGetResponse,
        )


class ViewsResourceWithRawResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_raw_response_wrapper(
            views.create,
        )
        self.update = to_raw_response_wrapper(
            views.update,
        )
        self.delete = to_raw_response_wrapper(
            views.delete,
        )
        self.get = to_raw_response_wrapper(
            views.get,
        )

    @cached_property
    def records(self) -> RecordsResourceWithRawResponse:
        return RecordsResourceWithRawResponse(self._views.records)


class AsyncViewsResourceWithRawResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_raw_response_wrapper(
            views.create,
        )
        self.update = async_to_raw_response_wrapper(
            views.update,
        )
        self.delete = async_to_raw_response_wrapper(
            views.delete,
        )
        self.get = async_to_raw_response_wrapper(
            views.get,
        )

    @cached_property
    def records(self) -> AsyncRecordsResourceWithRawResponse:
        return AsyncRecordsResourceWithRawResponse(self._views.records)


class ViewsResourceWithStreamingResponse:
    def __init__(self, views: ViewsResource) -> None:
        self._views = views

        self.create = to_streamed_response_wrapper(
            views.create,
        )
        self.update = to_streamed_response_wrapper(
            views.update,
        )
        self.delete = to_streamed_response_wrapper(
            views.delete,
        )
        self.get = to_streamed_response_wrapper(
            views.get,
        )

    @cached_property
    def records(self) -> RecordsResourceWithStreamingResponse:
        return RecordsResourceWithStreamingResponse(self._views.records)


class AsyncViewsResourceWithStreamingResponse:
    def __init__(self, views: AsyncViewsResource) -> None:
        self._views = views

        self.create = async_to_streamed_response_wrapper(
            views.create,
        )
        self.update = async_to_streamed_response_wrapper(
            views.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            views.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            views.get,
        )

    @cached_property
    def records(self) -> AsyncRecordsResourceWithStreamingResponse:
        return AsyncRecordsResourceWithStreamingResponse(self._views.records)
