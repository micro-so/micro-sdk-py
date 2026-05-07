# Prism

Types:

```python
from micro.types import PrismObjectProperties
```

## Metadata

Types:

```python
from micro.types.prism import MetadataListResponse
```

Methods:

- <code title="get /v2/prism/metadata/properties/{teamId}/{objectType}">client.prism.metadata.<a href="./src/micro/resources/prism/metadata.py">list</a>(object_type, \*, team_id, \*\*<a href="src/micro/types/prism/metadata_list_params.py">params</a>) -> <a href="./src/micro/types/prism/metadata_list_response.py">MetadataListResponse</a></code>

## Objects

### Contacts

Types:

```python
from micro.types.prism.objects import (
    Contact,
    ContactCreateResponse,
    ContactBulkCreateResponse,
    ContactQueryResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/contact">client.prism.objects.contacts.<a href="./src/micro/resources/prism/objects/contacts.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/contact_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/contact/import">client.prism.objects.contacts.<a href="./src/micro/resources/prism/objects/contacts.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/contact_bulk_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/contact_bulk_create_response.py">ContactBulkCreateResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/contact">client.prism.objects.contacts.<a href="./src/micro/resources/prism/objects/contacts.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/contact_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/contact_query_response.py">ContactQueryResponse</a></code>

### Organizations

Types:

```python
from micro.types.prism.objects import (
    Organization,
    OrganizationCreateResponse,
    OrganizationBulkCreateResponse,
    OrganizationQueryResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/organization">client.prism.objects.organizations.<a href="./src/micro/resources/prism/objects/organizations.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/organization_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/organization/import">client.prism.objects.organizations.<a href="./src/micro/resources/prism/objects/organizations.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/organization_bulk_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/organization_bulk_create_response.py">OrganizationBulkCreateResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/organization">client.prism.objects.organizations.<a href="./src/micro/resources/prism/objects/organizations.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/organization_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/organization_query_response.py">OrganizationQueryResponse</a></code>

### Identities

Types:

```python
from micro.types.prism.objects import (
    Identity,
    IdentityCreateResponse,
    IdentityUpdateResponse,
    IdentityBulkCreateResponse,
    IdentityDuplicateResponse,
    IdentityGetResponse,
    IdentityQueryResponse,
    IdentityRestoreResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/identity">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/identity_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/identity_create_response.py">IdentityCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/identity/{identityId}">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">update</a>(identity_id, \*, team_id, \*\*<a href="src/micro/types/prism/objects/identity_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/identity_update_response.py">IdentityUpdateResponse</a></code>
- <code title="delete /v2/prism/{teamId}/identity/{identityId}">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">delete</a>(identity_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/identity/import">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/identity_bulk_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/identity_bulk_create_response.py">IdentityBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/{identityId}/duplicate">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">duplicate</a>(identity_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/identity_duplicate_response.py">IdentityDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/identity/{identityId}">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">get</a>(identity_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/identity_get_response.py">IdentityGetResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/identity">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/identity_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/identity_query_response.py">IdentityQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/{identityId}/restore">client.prism.objects.identities.<a href="./src/micro/resources/prism/objects/identities.py">restore</a>(identity_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/identity_restore_response.py">IdentityRestoreResponse</a></code>

### Deals

Types:

```python
from micro.types.prism.objects import (
    Deal,
    DealCreateResponse,
    DealUpdateResponse,
    DealBulkCreateResponse,
    DealDuplicateResponse,
    DealGetResponse,
    DealQueryResponse,
    DealRestoreResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/deal">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/deal_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/deal_create_response.py">DealCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/deal/{dealId}">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">update</a>(deal_id, \*, team_id, \*\*<a href="src/micro/types/prism/objects/deal_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/deal_update_response.py">DealUpdateResponse</a></code>
- <code title="delete /v2/prism/{teamId}/deal/{dealId}">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">delete</a>(deal_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/deal/import">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/deal_bulk_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/deal_bulk_create_response.py">DealBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/{dealId}/duplicate">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">duplicate</a>(deal_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/deal_duplicate_response.py">DealDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/deal/{dealId}">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">get</a>(deal_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/deal_get_response.py">DealGetResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/deal">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/deal_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/deal_query_response.py">DealQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/{dealId}/restore">client.prism.objects.deals.<a href="./src/micro/resources/prism/objects/deals/deals.py">restore</a>(deal_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/deal_restore_response.py">DealRestoreResponse</a></code>

#### Grant

Types:

```python
from micro.types.prism.objects.deals import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/grant/{teamId}/deal/{dealId}">client.prism.objects.deals.grant.<a href="./src/micro/resources/prism/objects/deals/grant.py">update</a>(deal_id, \*, path_team_id, \*\*<a href="src/micro/types/prism/objects/deals/grant_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/deals/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/grant/{teamId}/deal/{dealId}">client.prism.objects.deals.grant.<a href="./src/micro/resources/prism/objects/deals/grant.py">get</a>(deal_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/deals/grant_get_response.py">GrantGetResponse</a></code>

### Actions

Types:

```python
from micro.types.prism.objects import (
    Action,
    ActionCreateResponse,
    ActionUpdateResponse,
    ActionBulkCreateResponse,
    ActionDuplicateResponse,
    ActionGetResponse,
    ActionQueryResponse,
    ActionRestoreResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/action">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/action_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/action_create_response.py">ActionCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/action/{actionId}">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">update</a>(action_id, \*, team_id, \*\*<a href="src/micro/types/prism/objects/action_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/action_update_response.py">ActionUpdateResponse</a></code>
- <code title="delete /v2/prism/{teamId}/action/{actionId}">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">delete</a>(action_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/action/import">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/action_bulk_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/action_bulk_create_response.py">ActionBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/{actionId}/duplicate">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">duplicate</a>(action_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/action_duplicate_response.py">ActionDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/action/{actionId}">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">get</a>(action_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/action_get_response.py">ActionGetResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/action">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/action_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/action_query_response.py">ActionQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/{actionId}/restore">client.prism.objects.actions.<a href="./src/micro/resources/prism/objects/actions/actions.py">restore</a>(action_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/action_restore_response.py">ActionRestoreResponse</a></code>

#### Grant

Types:

```python
from micro.types.prism.objects.actions import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/grant/{teamId}/action/{actionId}">client.prism.objects.actions.grant.<a href="./src/micro/resources/prism/objects/actions/grant.py">update</a>(action_id, \*, path_team_id, \*\*<a href="src/micro/types/prism/objects/actions/grant_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/actions/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/grant/{teamId}/action/{actionId}">client.prism.objects.actions.grant.<a href="./src/micro/resources/prism/objects/actions/grant.py">get</a>(action_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/actions/grant_get_response.py">GrantGetResponse</a></code>

### Documents

Types:

```python
from micro.types.prism.objects import (
    Document,
    DocumentCreateResponse,
    DocumentUpdateResponse,
    DocumentBulkCreateResponse,
    DocumentDuplicateResponse,
    DocumentGetResponse,
    DocumentQueryResponse,
    DocumentRestoreResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/document">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/document_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/document/{documentId}">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">update</a>(document_id, \*, team_id, \*\*<a href="src/micro/types/prism/objects/document_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="delete /v2/prism/{teamId}/document/{documentId}">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">delete</a>(document_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/document/import">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/document_bulk_create_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/document_bulk_create_response.py">DocumentBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/{documentId}/duplicate">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">duplicate</a>(document_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/document_duplicate_response.py">DocumentDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/document/{documentId}">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">get</a>(document_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/document_get_response.py">DocumentGetResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/document">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/document_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/document_query_response.py">DocumentQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/{documentId}/restore">client.prism.objects.documents.<a href="./src/micro/resources/prism/objects/documents/documents.py">restore</a>(document_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/document_restore_response.py">DocumentRestoreResponse</a></code>

#### Grant

Types:

```python
from micro.types.prism.objects.documents import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/grant/{teamId}/document/{documentId}">client.prism.objects.documents.grant.<a href="./src/micro/resources/prism/objects/documents/grant.py">update</a>(document_id, \*, path_team_id, \*\*<a href="src/micro/types/prism/objects/documents/grant_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/documents/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/grant/{teamId}/document/{documentId}">client.prism.objects.documents.grant.<a href="./src/micro/resources/prism/objects/documents/grant.py">get</a>(document_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/documents/grant_get_response.py">GrantGetResponse</a></code>

### Events

Types:

```python
from micro.types.prism.objects import Event, EventGetResponse, EventQueryResponse
```

Methods:

- <code title="get /v2/prism/{teamId}/event/{eventId}">client.prism.objects.events.<a href="./src/micro/resources/prism/objects/events/events.py">get</a>(event_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/event_get_response.py">EventGetResponse</a></code>
- <code title="post /v2/prism/query/{teamId}/event">client.prism.objects.events.<a href="./src/micro/resources/prism/objects/events/events.py">query</a>(\*, team_id, \*\*<a href="src/micro/types/prism/objects/event_query_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/event_query_response.py">EventQueryResponse</a></code>

#### Grant

Types:

```python
from micro.types.prism.objects.events import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/grant/{teamId}/event/{eventId}">client.prism.objects.events.grant.<a href="./src/micro/resources/prism/objects/events/grant.py">update</a>(event_id, \*, path_team_id, \*\*<a href="src/micro/types/prism/objects/events/grant_update_params.py">params</a>) -> <a href="./src/micro/types/prism/objects/events/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/grant/{teamId}/event/{eventId}">client.prism.objects.events.grant.<a href="./src/micro/resources/prism/objects/events/grant.py">get</a>(event_id, \*, team_id) -> <a href="./src/micro/types/prism/objects/events/grant_get_response.py">GrantGetResponse</a></code>

# Views

Types:

```python
from micro.types import ViewCreateResponse, ViewUpdateResponse, ViewGetResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/view/{viewObjectType}">client.views.<a href="./src/micro/resources/views/views.py">create</a>(view_object_type, \*, path_team_id, \*\*<a href="src/micro/types/view_create_params.py">params</a>) -> <a href="./src/micro/types/view_create_response.py">ViewCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/view/{viewObjectType}/{viewId}">client.views.<a href="./src/micro/resources/views/views.py">update</a>(view_id, \*, path_team_id, view_object_type, \*\*<a href="src/micro/types/view_update_params.py">params</a>) -> <a href="./src/micro/types/view_update_response.py">ViewUpdateResponse</a></code>
- <code title="delete /v2/prism/{teamId}/view/{viewObjectType}/{viewId}">client.views.<a href="./src/micro/resources/views/views.py">delete</a>(view_id, \*, team_id, view_object_type) -> None</code>
- <code title="get /v2/prism/{teamId}/view/{viewObjectType}/{viewId}">client.views.<a href="./src/micro/resources/views/views.py">get</a>(view_id, \*, team_id, view_object_type) -> <a href="./src/micro/types/view_get_response.py">ViewGetResponse</a></code>

## Records

Types:

```python
from micro.types.views import RecordListResponse
```

Methods:

- <code title="get /v2/prism/{teamId}/view/{viewObjectType}/{viewId}/records">client.views.records.<a href="./src/micro/resources/views/records.py">list</a>(view_id, \*, team_id, view_object_type, \*\*<a href="src/micro/types/views/record_list_params.py">params</a>) -> <a href="./src/micro/types/views/record_list_response.py">RecordListResponse</a></code>
- <code title="post /v2/prism/{teamId}/view/{viewObjectType}/{viewId}/records/{objectId}">client.views.records.<a href="./src/micro/resources/views/records.py">pin</a>(object_id, \*, team_id, view_object_type, view_id) -> None</code>
- <code title="patch /v2/prism/{teamId}/view/{viewObjectType}/{viewId}/records">client.views.records.<a href="./src/micro/resources/views/records.py">reorder</a>(view_id, \*, team_id, view_object_type, \*\*<a href="src/micro/types/views/record_reorder_params.py">params</a>) -> None</code>
- <code title="delete /v2/prism/{teamId}/view/{viewObjectType}/{viewId}/records/{objectId}">client.views.records.<a href="./src/micro/resources/views/records.py">unpin</a>(object_id, \*, team_id, view_object_type, view_id) -> None</code>
