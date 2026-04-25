# Prism

Types:

```python
from micro.types import (
    ObjectType,
    PrismObjectProperties,
    PrismDuplicateObjectResponse,
    PrismImportObjectsResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/{objectType}">client.prism.<a href="./src/micro/resources/prism/prism.py">create_object</a>(object_type, \*, team_id, \*\*<a href="src/micro/types/prism_create_object_params.py">params</a>) -> None</code>
- <code title="delete /v2/prism/{teamId}/{objectType}/{objectId}">client.prism.<a href="./src/micro/resources/prism/prism.py">delete_object</a>(object_id, \*, team_id, object_type) -> None</code>
- <code title="post /v2/prism/{teamId}/{objectType}/{objectId}/duplicate">client.prism.<a href="./src/micro/resources/prism/prism.py">duplicate_object</a>(object_id, \*, team_id, object_type) -> <a href="./src/micro/types/prism_duplicate_object_response.py">PrismDuplicateObjectResponse</a></code>
- <code title="post /v2/prism/{teamId}/{objectType}/import">client.prism.<a href="./src/micro/resources/prism/prism.py">import_objects</a>(object_type, \*, team_id, \*\*<a href="src/micro/types/prism_import_objects_params.py">params</a>) -> <a href="./src/micro/types/prism_import_objects_response.py">PrismImportObjectsResponse</a></code>
- <code title="patch /v2/prism/{teamId}/{objectType}/{objectId}">client.prism.<a href="./src/micro/resources/prism/prism.py">patch_object</a>(object_id, \*, team_id, object_type, \*\*<a href="src/micro/types/prism_patch_object_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/{teamId}/{objectType}/{objectId}/restore">client.prism.<a href="./src/micro/resources/prism/prism.py">restore_object</a>(object_id, \*, team_id, object_type) -> None</code>

## Grant

Methods:

- <code title="get /v2/prism/grant/{teamId}/{objectType}/{objectId}">client.prism.grant.<a href="./src/micro/resources/prism/grant.py">retrieve_grant</a>(object_id, \*, team_id, object_type) -> None</code>
- <code title="put /v2/prism/grant/{teamId}/{objectType}/{objectId}">client.prism.grant.<a href="./src/micro/resources/prism/grant.py">update_grant</a>(object_id, \*, path_team_id, object_type, \*\*<a href="src/micro/types/prism/grant_update_grant_params.py">params</a>) -> None</code>

## Query

Types:

```python
from micro.types.prism import QueryExecuteResponse
```

Methods:

- <code title="post /v2/prism/query/{teamId}/{objectType}">client.prism.query.<a href="./src/micro/resources/prism/query.py">execute</a>(object_type, \*, team_id, \*\*<a href="src/micro/types/prism/query_execute_params.py">params</a>) -> <a href="./src/micro/types/prism/query_execute_response.py">QueryExecuteResponse</a></code>

## Metadata

Methods:

- <code title="get /v2/prism/metadata/properties/{teamId}/{objectType}">client.prism.metadata.<a href="./src/micro/resources/prism/metadata.py">properties</a>(object_type, \*, team_id, \*\*<a href="src/micro/types/prism/metadata_properties_params.py">params</a>) -> None</code>

# Contacts

Types:

```python
from micro.types import Contact, ContactCreateResponse, ContactListResponse, ContactImportResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/contact">client.contacts.<a href="./src/micro/resources/contacts.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/contact_create_params.py">params</a>) -> <a href="./src/micro/types/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/contact/{contactId}">client.contacts.<a href="./src/micro/resources/contacts.py">update</a>(contact_id, \*, team_id, \*\*<a href="src/micro/types/contact_update_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/query/{teamId}/contact">client.contacts.<a href="./src/micro/resources/contacts.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/contact_list_params.py">params</a>) -> <a href="./src/micro/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/contact/{contactId}">client.contacts.<a href="./src/micro/resources/contacts.py">delete</a>(contact_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/contact/import">client.contacts.<a href="./src/micro/resources/contacts.py">import\_</a>(\*, team_id, \*\*<a href="src/micro/types/contact_import_params.py">params</a>) -> <a href="./src/micro/types/contact_import_response.py">ContactImportResponse</a></code>

# Organizations

Types:

```python
from micro.types import (
    Organization,
    OrganizationCreateResponse,
    OrganizationListResponse,
    OrganizationImportResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/organization">client.organizations.<a href="./src/micro/resources/organizations.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/organization_create_params.py">params</a>) -> <a href="./src/micro/types/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/organization/{organizationId}">client.organizations.<a href="./src/micro/resources/organizations.py">update</a>(organization_id, \*, team_id, \*\*<a href="src/micro/types/organization_update_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/query/{teamId}/organization">client.organizations.<a href="./src/micro/resources/organizations.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/organization_list_params.py">params</a>) -> <a href="./src/micro/types/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/organization/{organizationId}">client.organizations.<a href="./src/micro/resources/organizations.py">delete</a>(organization_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/organization/import">client.organizations.<a href="./src/micro/resources/organizations.py">import\_</a>(\*, team_id, \*\*<a href="src/micro/types/organization_import_params.py">params</a>) -> <a href="./src/micro/types/organization_import_response.py">OrganizationImportResponse</a></code>

# Identities

Types:

```python
from micro.types import (
    Identity,
    IdentityCreateResponse,
    IdentityListResponse,
    IdentityImportResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/identity">client.identities.<a href="./src/micro/resources/identities.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/identity_create_params.py">params</a>) -> <a href="./src/micro/types/identity_create_response.py">IdentityCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/identity/{identityId}">client.identities.<a href="./src/micro/resources/identities.py">update</a>(identity_id, \*, team_id, \*\*<a href="src/micro/types/identity_update_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/query/{teamId}/identity">client.identities.<a href="./src/micro/resources/identities.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/identity_list_params.py">params</a>) -> <a href="./src/micro/types/identity_list_response.py">IdentityListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/identity/{identityId}">client.identities.<a href="./src/micro/resources/identities.py">delete</a>(identity_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/identity/import">client.identities.<a href="./src/micro/resources/identities.py">import\_</a>(\*, team_id, \*\*<a href="src/micro/types/identity_import_params.py">params</a>) -> <a href="./src/micro/types/identity_import_response.py">IdentityImportResponse</a></code>

# Deals

Types:

```python
from micro.types import Deal, DealCreateResponse, DealListResponse, DealImportResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/deal">client.deals.<a href="./src/micro/resources/deals.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/deal_create_params.py">params</a>) -> <a href="./src/micro/types/deal_create_response.py">DealCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/deal/{dealId}">client.deals.<a href="./src/micro/resources/deals.py">update</a>(deal_id, \*, team_id, \*\*<a href="src/micro/types/deal_update_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/query/{teamId}/deal">client.deals.<a href="./src/micro/resources/deals.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/deal_list_params.py">params</a>) -> <a href="./src/micro/types/deal_list_response.py">DealListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/deal/{dealId}">client.deals.<a href="./src/micro/resources/deals.py">delete</a>(deal_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/deal/import">client.deals.<a href="./src/micro/resources/deals.py">import\_</a>(\*, team_id, \*\*<a href="src/micro/types/deal_import_params.py">params</a>) -> <a href="./src/micro/types/deal_import_response.py">DealImportResponse</a></code>

# Actions

Types:

```python
from micro.types import Action, ActionCreateResponse, ActionListResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/action">client.actions.<a href="./src/micro/resources/actions.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/action_create_params.py">params</a>) -> <a href="./src/micro/types/action_create_response.py">ActionCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/action/{actionId}">client.actions.<a href="./src/micro/resources/actions.py">update</a>(action_id, \*, team_id, \*\*<a href="src/micro/types/action_update_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/query/{teamId}/action">client.actions.<a href="./src/micro/resources/actions.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/action_list_params.py">params</a>) -> <a href="./src/micro/types/action_list_response.py">ActionListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/action/{actionId}">client.actions.<a href="./src/micro/resources/actions.py">delete</a>(action_id, \*, team_id) -> None</code>

# Events

Types:

```python
from micro.types import Event, EventListResponse
```

Methods:

- <code title="post /v2/prism/query/{teamId}/event">client.events.<a href="./src/micro/resources/events.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/event_list_params.py">params</a>) -> <a href="./src/micro/types/event_list_response.py">EventListResponse</a></code>

# Documents

Types:

```python
from micro.types import Document, DocumentCreateResponse, DocumentListResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/document">client.documents.<a href="./src/micro/resources/documents.py">create</a>(\*, team_id, \*\*<a href="src/micro/types/document_create_params.py">params</a>) -> <a href="./src/micro/types/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/document/{documentId}">client.documents.<a href="./src/micro/resources/documents.py">update</a>(document_id, \*, team_id, \*\*<a href="src/micro/types/document_update_params.py">params</a>) -> None</code>
- <code title="post /v2/prism/query/{teamId}/document">client.documents.<a href="./src/micro/resources/documents.py">list</a>(\*, team_id, \*\*<a href="src/micro/types/document_list_params.py">params</a>) -> <a href="./src/micro/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/document/{documentId}">client.documents.<a href="./src/micro/resources/documents.py">delete</a>(document_id, \*, team_id) -> None</code>
