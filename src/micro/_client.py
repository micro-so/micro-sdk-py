# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import MicroError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import deals, prism, events, actions, contacts, documents, identities, organizations
    from .resources.deals import DealsResource, AsyncDealsResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.actions import ActionsResource, AsyncActionsResource
    from .resources.contacts import ContactsResource, AsyncContactsResource
    from .resources.documents import DocumentsResource, AsyncDocumentsResource
    from .resources.identities import IdentitiesResource, AsyncIdentitiesResource
    from .resources.prism.prism import PrismResource, AsyncPrismResource
    from .resources.organizations import OrganizationsResource, AsyncOrganizationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Micro", "AsyncMicro", "Client", "AsyncClient"]


class Micro(SyncAPIClient):
    # client options
    api_key: str
    team_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        team_id: str,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Micro client instance.

        This automatically infers the `api_key` argument from the `MICRO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MICRO_API_KEY")
        if api_key is None:
            raise MicroError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MICRO_API_KEY environment variable"
            )
        self.api_key = api_key

        self.team_id = team_id

        if base_url is None:
            base_url = os.environ.get("MICRO_BASE_URL")
        if base_url is None:
            base_url = f"https://developers.micro.so"

        custom_headers_env = os.environ.get("MICRO_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def prism(self) -> PrismResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        from .resources.prism import PrismResource

        return PrismResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        """Contacts represent individual people in Micro.

        Each contact can have a name, email, phone, title, and custom properties, and can be linked to an organization.
        """
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        """Organizations represent companies or teams in Micro.

        Contacts and deals can be associated with an organization.
        """
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def identities(self) -> IdentitiesResource:
        """
        Identities link multiple contacts together as the same real-world person, deduplicating people who appear in different contexts.
        """
        from .resources.identities import IdentitiesResource

        return IdentitiesResource(self)

    @cached_property
    def deals(self) -> DealsResource:
        """
        Deals track opportunities moving through a pipeline — fundraising rounds, sales opportunities, hiring candidates, or any custom workflow.
        """
        from .resources.deals import DealsResource

        return DealsResource(self)

    @cached_property
    def actions(self) -> ActionsResource:
        """
        Actions are tasks and to-dos that can be assigned to contacts, organizations, or deals, with a status, due date, and priority.
        """
        from .resources.actions import ActionsResource

        return ActionsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """
        Events are calendar items — meetings, calls, and appointments — automatically captured from your connected calendar accounts.
        """
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def documents(self) -> DocumentsResource:
        """
        Documents are rich-text notes attached to contacts, organizations, or deals, used for meeting notes, research, or context.
        """
        from .resources.documents import DocumentsResource

        return DocumentsResource(self)

    @cached_property
    def with_raw_response(self) -> MicroWithRawResponse:
        return MicroWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MicroWithStreamedResponse:
        return MicroWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        team_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            team_id=team_id or self.team_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_team_id_path_param(self) -> str:
        return self.team_id

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMicro(AsyncAPIClient):
    # client options
    api_key: str
    team_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        team_id: str,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMicro client instance.

        This automatically infers the `api_key` argument from the `MICRO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MICRO_API_KEY")
        if api_key is None:
            raise MicroError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MICRO_API_KEY environment variable"
            )
        self.api_key = api_key

        self.team_id = team_id

        if base_url is None:
            base_url = os.environ.get("MICRO_BASE_URL")
        if base_url is None:
            base_url = f"https://developers.micro.so"

        custom_headers_env = os.environ.get("MICRO_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def prism(self) -> AsyncPrismResource:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        from .resources.prism import AsyncPrismResource

        return AsyncPrismResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """Contacts represent individual people in Micro.

        Each contact can have a name, email, phone, title, and custom properties, and can be linked to an organization.
        """
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        """Organizations represent companies or teams in Micro.

        Contacts and deals can be associated with an organization.
        """
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def identities(self) -> AsyncIdentitiesResource:
        """
        Identities link multiple contacts together as the same real-world person, deduplicating people who appear in different contexts.
        """
        from .resources.identities import AsyncIdentitiesResource

        return AsyncIdentitiesResource(self)

    @cached_property
    def deals(self) -> AsyncDealsResource:
        """
        Deals track opportunities moving through a pipeline — fundraising rounds, sales opportunities, hiring candidates, or any custom workflow.
        """
        from .resources.deals import AsyncDealsResource

        return AsyncDealsResource(self)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Actions are tasks and to-dos that can be assigned to contacts, organizations, or deals, with a status, due date, and priority.
        """
        from .resources.actions import AsyncActionsResource

        return AsyncActionsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """
        Events are calendar items — meetings, calls, and appointments — automatically captured from your connected calendar accounts.
        """
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        """
        Documents are rich-text notes attached to contacts, organizations, or deals, used for meeting notes, research, or context.
        """
        from .resources.documents import AsyncDocumentsResource

        return AsyncDocumentsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMicroWithRawResponse:
        return AsyncMicroWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMicroWithStreamedResponse:
        return AsyncMicroWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        team_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            team_id=team_id or self.team_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_team_id_path_param(self) -> str:
        return self.team_id

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MicroWithRawResponse:
    _client: Micro

    def __init__(self, client: Micro) -> None:
        self._client = client

    @cached_property
    def prism(self) -> prism.PrismResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        from .resources.prism import PrismResourceWithRawResponse

        return PrismResourceWithRawResponse(self._client.prism)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        """Contacts represent individual people in Micro.

        Each contact can have a name, email, phone, title, and custom properties, and can be linked to an organization.
        """
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        """Organizations represent companies or teams in Micro.

        Contacts and deals can be associated with an organization.
        """
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def identities(self) -> identities.IdentitiesResourceWithRawResponse:
        """
        Identities link multiple contacts together as the same real-world person, deduplicating people who appear in different contexts.
        """
        from .resources.identities import IdentitiesResourceWithRawResponse

        return IdentitiesResourceWithRawResponse(self._client.identities)

    @cached_property
    def deals(self) -> deals.DealsResourceWithRawResponse:
        """
        Deals track opportunities moving through a pipeline — fundraising rounds, sales opportunities, hiring candidates, or any custom workflow.
        """
        from .resources.deals import DealsResourceWithRawResponse

        return DealsResourceWithRawResponse(self._client.deals)

    @cached_property
    def actions(self) -> actions.ActionsResourceWithRawResponse:
        """
        Actions are tasks and to-dos that can be assigned to contacts, organizations, or deals, with a status, due date, and priority.
        """
        from .resources.actions import ActionsResourceWithRawResponse

        return ActionsResourceWithRawResponse(self._client.actions)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        """
        Events are calendar items — meetings, calls, and appointments — automatically captured from your connected calendar accounts.
        """
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithRawResponse:
        """
        Documents are rich-text notes attached to contacts, organizations, or deals, used for meeting notes, research, or context.
        """
        from .resources.documents import DocumentsResourceWithRawResponse

        return DocumentsResourceWithRawResponse(self._client.documents)


class AsyncMicroWithRawResponse:
    _client: AsyncMicro

    def __init__(self, client: AsyncMicro) -> None:
        self._client = client

    @cached_property
    def prism(self) -> prism.AsyncPrismResourceWithRawResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        from .resources.prism import AsyncPrismResourceWithRawResponse

        return AsyncPrismResourceWithRawResponse(self._client.prism)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        """Contacts represent individual people in Micro.

        Each contact can have a name, email, phone, title, and custom properties, and can be linked to an organization.
        """
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        """Organizations represent companies or teams in Micro.

        Contacts and deals can be associated with an organization.
        """
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def identities(self) -> identities.AsyncIdentitiesResourceWithRawResponse:
        """
        Identities link multiple contacts together as the same real-world person, deduplicating people who appear in different contexts.
        """
        from .resources.identities import AsyncIdentitiesResourceWithRawResponse

        return AsyncIdentitiesResourceWithRawResponse(self._client.identities)

    @cached_property
    def deals(self) -> deals.AsyncDealsResourceWithRawResponse:
        """
        Deals track opportunities moving through a pipeline — fundraising rounds, sales opportunities, hiring candidates, or any custom workflow.
        """
        from .resources.deals import AsyncDealsResourceWithRawResponse

        return AsyncDealsResourceWithRawResponse(self._client.deals)

    @cached_property
    def actions(self) -> actions.AsyncActionsResourceWithRawResponse:
        """
        Actions are tasks and to-dos that can be assigned to contacts, organizations, or deals, with a status, due date, and priority.
        """
        from .resources.actions import AsyncActionsResourceWithRawResponse

        return AsyncActionsResourceWithRawResponse(self._client.actions)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        """
        Events are calendar items — meetings, calls, and appointments — automatically captured from your connected calendar accounts.
        """
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithRawResponse:
        """
        Documents are rich-text notes attached to contacts, organizations, or deals, used for meeting notes, research, or context.
        """
        from .resources.documents import AsyncDocumentsResourceWithRawResponse

        return AsyncDocumentsResourceWithRawResponse(self._client.documents)


class MicroWithStreamedResponse:
    _client: Micro

    def __init__(self, client: Micro) -> None:
        self._client = client

    @cached_property
    def prism(self) -> prism.PrismResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        from .resources.prism import PrismResourceWithStreamingResponse

        return PrismResourceWithStreamingResponse(self._client.prism)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        """Contacts represent individual people in Micro.

        Each contact can have a name, email, phone, title, and custom properties, and can be linked to an organization.
        """
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        """Organizations represent companies or teams in Micro.

        Contacts and deals can be associated with an organization.
        """
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def identities(self) -> identities.IdentitiesResourceWithStreamingResponse:
        """
        Identities link multiple contacts together as the same real-world person, deduplicating people who appear in different contexts.
        """
        from .resources.identities import IdentitiesResourceWithStreamingResponse

        return IdentitiesResourceWithStreamingResponse(self._client.identities)

    @cached_property
    def deals(self) -> deals.DealsResourceWithStreamingResponse:
        """
        Deals track opportunities moving through a pipeline — fundraising rounds, sales opportunities, hiring candidates, or any custom workflow.
        """
        from .resources.deals import DealsResourceWithStreamingResponse

        return DealsResourceWithStreamingResponse(self._client.deals)

    @cached_property
    def actions(self) -> actions.ActionsResourceWithStreamingResponse:
        """
        Actions are tasks and to-dos that can be assigned to contacts, organizations, or deals, with a status, due date, and priority.
        """
        from .resources.actions import ActionsResourceWithStreamingResponse

        return ActionsResourceWithStreamingResponse(self._client.actions)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        """
        Events are calendar items — meetings, calls, and appointments — automatically captured from your connected calendar accounts.
        """
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithStreamingResponse:
        """
        Documents are rich-text notes attached to contacts, organizations, or deals, used for meeting notes, research, or context.
        """
        from .resources.documents import DocumentsResourceWithStreamingResponse

        return DocumentsResourceWithStreamingResponse(self._client.documents)


class AsyncMicroWithStreamedResponse:
    _client: AsyncMicro

    def __init__(self, client: AsyncMicro) -> None:
        self._client = client

    @cached_property
    def prism(self) -> prism.AsyncPrismResourceWithStreamingResponse:
        """
        The Prism query engine provides generic read/write access to any object type using a single unified API surface.
        """
        from .resources.prism import AsyncPrismResourceWithStreamingResponse

        return AsyncPrismResourceWithStreamingResponse(self._client.prism)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        """Contacts represent individual people in Micro.

        Each contact can have a name, email, phone, title, and custom properties, and can be linked to an organization.
        """
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        """Organizations represent companies or teams in Micro.

        Contacts and deals can be associated with an organization.
        """
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def identities(self) -> identities.AsyncIdentitiesResourceWithStreamingResponse:
        """
        Identities link multiple contacts together as the same real-world person, deduplicating people who appear in different contexts.
        """
        from .resources.identities import AsyncIdentitiesResourceWithStreamingResponse

        return AsyncIdentitiesResourceWithStreamingResponse(self._client.identities)

    @cached_property
    def deals(self) -> deals.AsyncDealsResourceWithStreamingResponse:
        """
        Deals track opportunities moving through a pipeline — fundraising rounds, sales opportunities, hiring candidates, or any custom workflow.
        """
        from .resources.deals import AsyncDealsResourceWithStreamingResponse

        return AsyncDealsResourceWithStreamingResponse(self._client.deals)

    @cached_property
    def actions(self) -> actions.AsyncActionsResourceWithStreamingResponse:
        """
        Actions are tasks and to-dos that can be assigned to contacts, organizations, or deals, with a status, due date, and priority.
        """
        from .resources.actions import AsyncActionsResourceWithStreamingResponse

        return AsyncActionsResourceWithStreamingResponse(self._client.actions)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        """
        Events are calendar items — meetings, calls, and appointments — automatically captured from your connected calendar accounts.
        """
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithStreamingResponse:
        """
        Documents are rich-text notes attached to contacts, organizations, or deals, used for meeting notes, research, or context.
        """
        from .resources.documents import AsyncDocumentsResourceWithStreamingResponse

        return AsyncDocumentsResourceWithStreamingResponse(self._client.documents)


Client = Micro

AsyncClient = AsyncMicro
