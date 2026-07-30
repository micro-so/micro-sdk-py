# Prism

Types:

```python
from micro_so.types import PrismObjectProperties
```

## Properties

Types:

```python
from micro_so.types.prism import (
    PropertyDefinition,
    PropertyDefinitionCreate,
    PropertyDefinitionPatch,
    PropertyListResponse,
    PropertyListAllResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/{objectType}/properties">client.prism.properties.<a href="./src/micro_so/resources/prism/properties/properties.py">create</a>(object_type, \*, team_id, \*\*<a href="src/micro_so/types/prism/property_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/property_definition.py">PropertyDefinition</a></code>
- <code title="patch /v2/prism/{teamId}/{objectType}/properties/{propertyId}">client.prism.properties.<a href="./src/micro_so/resources/prism/properties/properties.py">update</a>(property_id, \*, team_id, object_type, \*\*<a href="src/micro_so/types/prism/property_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/property_definition.py">PropertyDefinition</a></code>
- <code title="get /v2/prism/{teamId}/{objectType}/properties">client.prism.properties.<a href="./src/micro_so/resources/prism/properties/properties.py">list</a>(object_type, \*, team_id, \*\*<a href="src/micro_so/types/prism/property_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/property_list_response.py">PropertyListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/{objectType}/properties/{propertyId}">client.prism.properties.<a href="./src/micro_so/resources/prism/properties/properties.py">delete</a>(property_id, \*, team_id, object_type, \*\*<a href="src/micro_so/types/prism/property_delete_params.py">params</a>) -> None</code>
- <code title="get /v2/prism/{teamId}/properties">client.prism.properties.<a href="./src/micro_so/resources/prism/properties/properties.py">list_all</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/property_list_all_params.py">params</a>) -> <a href="./src/micro_so/types/prism/property_list_all_response.py">PropertyListAllResponse</a></code>

### Options

Types:

```python
from micro_so.types.prism.properties import (
    PropertyOption,
    PropertyOptionCreate,
    PropertyOptionPatch,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/{objectType}/properties/{propertyId}/options">client.prism.properties.options.<a href="./src/micro_so/resources/prism/properties/options.py">create</a>(property_id, \*, team_id, object_type, \*\*<a href="src/micro_so/types/prism/properties/option_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/properties/property_option.py">PropertyOption</a></code>
- <code title="patch /v2/prism/{teamId}/{objectType}/properties/{propertyId}/options/{optionId}">client.prism.properties.options.<a href="./src/micro_so/resources/prism/properties/options.py">update</a>(option_id, \*, team_id, object_type, property_id, \*\*<a href="src/micro_so/types/prism/properties/option_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/properties/property_option.py">PropertyOption</a></code>
- <code title="delete /v2/prism/{teamId}/{objectType}/properties/{propertyId}/options/{optionId}">client.prism.properties.options.<a href="./src/micro_so/resources/prism/properties/options.py">delete</a>(option_id, \*, team_id, object_type, property_id, \*\*<a href="src/micro_so/types/prism/properties/option_delete_params.py">params</a>) -> None</code>

## Imports

Types:

```python
from micro_so.types.prism import ImportGetResponse
```

Methods:

- <code title="get /v2/prism/{teamId}/imports/{jobId}">client.prism.imports.<a href="./src/micro_so/resources/prism/imports.py">get</a>(job_id, \*, team_id) -> <a href="./src/micro_so/types/prism/import_get_response.py">ImportGetResponse</a></code>

## Objects

### Contacts

Types:

```python
from micro_so.types.prism.objects import (
    Contact,
    ContactCreateResponse,
    ContactUpdateResponse,
    ContactListResponse,
    ContactBulkCreateResponse,
    ContactBulkDeleteResponse,
    ContactBulkUpdateResponse,
    ContactCountResponse,
    ContactDuplicateResponse,
    ContactFindResponse,
    ContactGetResponse,
    ContactQueryResponse,
    ContactRestoreResponse,
    ContactUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/contact">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/contact/{contactId}">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">update</a>(contact_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_update_response.py">ContactUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/contact">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/contact/{contactId}">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">delete</a>(contact_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/contact/import">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_bulk_create_response.py">ContactBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/contact/batch/delete">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_bulk_delete_response.py">ContactBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/contact/batch/update">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_bulk_update_response.py">ContactBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/contact/count">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_count_response.py">ContactCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/contact/{contactId}/duplicate">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">duplicate</a>(contact_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/contact_duplicate_response.py">ContactDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/contact/by/{slug}/{value}">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/contact_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_find_response.py">ContactFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/contact/{contactId}">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">get</a>(contact_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_get_response.py">ContactGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/contact/query">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/contact_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_query_response.py">ContactQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/contact/{contactId}/restore">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">restore</a>(contact_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/contact_restore_response.py">ContactRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/contact/by/{slug}/{value}">client.prism.objects.contacts.<a href="./src/micro_so/resources/prism/objects/contacts.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/contact_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/contact_upsert_response.py">ContactUpsertResponse</a></code>

### Organizations

Types:

```python
from micro_so.types.prism.objects import (
    Organization,
    OrganizationCreateResponse,
    OrganizationUpdateResponse,
    OrganizationListResponse,
    OrganizationBulkCreateResponse,
    OrganizationBulkDeleteResponse,
    OrganizationBulkUpdateResponse,
    OrganizationCountResponse,
    OrganizationDuplicateResponse,
    OrganizationFindResponse,
    OrganizationGetResponse,
    OrganizationQueryResponse,
    OrganizationRestoreResponse,
    OrganizationUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/organization">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/organization/{organizationId}">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">update</a>(organization_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_update_response.py">OrganizationUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/organization">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_list_response.py">OrganizationListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/organization/{organizationId}">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">delete</a>(organization_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/organization/import">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_bulk_create_response.py">OrganizationBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/organization/batch/delete">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_bulk_delete_response.py">OrganizationBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/organization/batch/update">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_bulk_update_response.py">OrganizationBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/organization/count">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_count_response.py">OrganizationCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/organization/{organizationId}/duplicate">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">duplicate</a>(organization_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/organization_duplicate_response.py">OrganizationDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/organization/by/{slug}/{value}">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/organization_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_find_response.py">OrganizationFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/organization/{organizationId}">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">get</a>(organization_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_get_response.py">OrganizationGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/organization/query">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/organization_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_query_response.py">OrganizationQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/organization/{organizationId}/restore">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">restore</a>(organization_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/organization_restore_response.py">OrganizationRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/organization/by/{slug}/{value}">client.prism.objects.organizations.<a href="./src/micro_so/resources/prism/objects/organizations.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/organization_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/organization_upsert_response.py">OrganizationUpsertResponse</a></code>

### Identities

Types:

```python
from micro_so.types.prism.objects import (
    Identity,
    IdentityCreateResponse,
    IdentityUpdateResponse,
    IdentityListResponse,
    IdentityBulkCreateResponse,
    IdentityBulkDeleteResponse,
    IdentityBulkUpdateResponse,
    IdentityCountResponse,
    IdentityDuplicateResponse,
    IdentityFindResponse,
    IdentityGetResponse,
    IdentityQueryResponse,
    IdentityRestoreResponse,
    IdentityUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/identity">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_create_response.py">IdentityCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/identity/{identityId}">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">update</a>(identity_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_update_response.py">IdentityUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/identity">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_list_response.py">IdentityListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/identity/{identityId}">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">delete</a>(identity_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/identity/import">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_bulk_create_response.py">IdentityBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/batch/delete">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_bulk_delete_response.py">IdentityBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/batch/update">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_bulk_update_response.py">IdentityBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/identity/count">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_count_response.py">IdentityCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/{identityId}/duplicate">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">duplicate</a>(identity_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/identity_duplicate_response.py">IdentityDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/identity/by/{slug}/{value}">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/identity_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_find_response.py">IdentityFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/identity/{identityId}">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">get</a>(identity_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_get_response.py">IdentityGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/query">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/identity_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_query_response.py">IdentityQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/identity/{identityId}/restore">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">restore</a>(identity_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/identity_restore_response.py">IdentityRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/identity/by/{slug}/{value}">client.prism.objects.identities.<a href="./src/micro_so/resources/prism/objects/identities.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/identity_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/identity_upsert_response.py">IdentityUpsertResponse</a></code>

### Deals

Types:

```python
from micro_so.types.prism.objects import (
    Deal,
    DealCreateResponse,
    DealUpdateResponse,
    DealListResponse,
    DealBulkCreateResponse,
    DealBulkDeleteResponse,
    DealBulkUpdateResponse,
    DealCountResponse,
    DealDuplicateResponse,
    DealFindResponse,
    DealGetResponse,
    DealQueryResponse,
    DealRestoreResponse,
    DealUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/deal">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_create_response.py">DealCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/deal/{dealId}">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">update</a>(deal_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_update_response.py">DealUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/deal">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_list_response.py">DealListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/deal/{dealId}">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">delete</a>(deal_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/deal/import">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_bulk_create_response.py">DealBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/batch/delete">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_bulk_delete_response.py">DealBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/batch/update">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_bulk_update_response.py">DealBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/deal/count">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_count_response.py">DealCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/{dealId}/duplicate">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">duplicate</a>(deal_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/deal_duplicate_response.py">DealDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/deal/by/{slug}/{value}">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/deal_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_find_response.py">DealFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/deal/{dealId}">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">get</a>(deal_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_get_response.py">DealGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/query">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/deal_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_query_response.py">DealQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/deal/{dealId}/restore">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">restore</a>(deal_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/deal_restore_response.py">DealRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/deal/by/{slug}/{value}">client.prism.objects.deals.<a href="./src/micro_so/resources/prism/objects/deals/deals.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/deal_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deal_upsert_response.py">DealUpsertResponse</a></code>

#### Grant

Types:

```python
from micro_so.types.prism.objects.deals import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/{teamId}/deal/{dealId}/grant">client.prism.objects.deals.grant.<a href="./src/micro_so/resources/prism/objects/deals/grant.py">update</a>(deal_id, \*, path_team_id, \*\*<a href="src/micro_so/types/prism/objects/deals/grant_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/deals/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/deal/{dealId}/grant">client.prism.objects.deals.grant.<a href="./src/micro_so/resources/prism/objects/deals/grant.py">get</a>(deal_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/deals/grant_get_response.py">GrantGetResponse</a></code>

### Actions

Types:

```python
from micro_so.types.prism.objects import (
    Action,
    ActionCreateResponse,
    ActionUpdateResponse,
    ActionListResponse,
    ActionBulkCreateResponse,
    ActionBulkDeleteResponse,
    ActionBulkUpdateResponse,
    ActionCountResponse,
    ActionDuplicateResponse,
    ActionFindResponse,
    ActionGetResponse,
    ActionQueryResponse,
    ActionRestoreResponse,
    ActionUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/action">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_create_response.py">ActionCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/action/{actionId}">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">update</a>(action_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_update_response.py">ActionUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/action">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_list_response.py">ActionListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/action/{actionId}">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">delete</a>(action_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/action/import">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_bulk_create_response.py">ActionBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/batch/delete">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_bulk_delete_response.py">ActionBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/batch/update">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_bulk_update_response.py">ActionBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/action/count">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_count_response.py">ActionCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/{actionId}/duplicate">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">duplicate</a>(action_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/action_duplicate_response.py">ActionDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/action/by/{slug}/{value}">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/action_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_find_response.py">ActionFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/action/{actionId}">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">get</a>(action_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_get_response.py">ActionGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/query">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/action_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_query_response.py">ActionQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/action/{actionId}/restore">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">restore</a>(action_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/action_restore_response.py">ActionRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/action/by/{slug}/{value}">client.prism.objects.actions.<a href="./src/micro_so/resources/prism/objects/actions/actions.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/action_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/action_upsert_response.py">ActionUpsertResponse</a></code>

#### Grant

Types:

```python
from micro_so.types.prism.objects.actions import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/{teamId}/action/{actionId}/grant">client.prism.objects.actions.grant.<a href="./src/micro_so/resources/prism/objects/actions/grant.py">update</a>(action_id, \*, path_team_id, \*\*<a href="src/micro_so/types/prism/objects/actions/grant_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/actions/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/action/{actionId}/grant">client.prism.objects.actions.grant.<a href="./src/micro_so/resources/prism/objects/actions/grant.py">get</a>(action_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/actions/grant_get_response.py">GrantGetResponse</a></code>

### Documents

Types:

```python
from micro_so.types.prism.objects import (
    Document,
    DocumentCreateResponse,
    DocumentUpdateResponse,
    DocumentListResponse,
    DocumentBulkCreateResponse,
    DocumentBulkDeleteResponse,
    DocumentBulkUpdateResponse,
    DocumentCountResponse,
    DocumentDuplicateResponse,
    DocumentFindResponse,
    DocumentGetResponse,
    DocumentQueryResponse,
    DocumentRestoreResponse,
    DocumentUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/document">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/document/{documentId}">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">update</a>(document_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/document">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/document/{documentId}">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">delete</a>(document_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/document/import">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_bulk_create_response.py">DocumentBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/batch/delete">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_bulk_delete_response.py">DocumentBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/batch/update">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_bulk_update_response.py">DocumentBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/document/count">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_count_response.py">DocumentCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/{documentId}/duplicate">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">duplicate</a>(document_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/document_duplicate_response.py">DocumentDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/document/by/{slug}/{value}">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/document_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_find_response.py">DocumentFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/document/{documentId}">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">get</a>(document_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_get_response.py">DocumentGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/query">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/document_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_query_response.py">DocumentQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/document/{documentId}/restore">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">restore</a>(document_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/document_restore_response.py">DocumentRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/document/by/{slug}/{value}">client.prism.objects.documents.<a href="./src/micro_so/resources/prism/objects/documents/documents.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/document_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/document_upsert_response.py">DocumentUpsertResponse</a></code>

#### Grant

Types:

```python
from micro_so.types.prism.objects.documents import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/{teamId}/document/{documentId}/grant">client.prism.objects.documents.grant.<a href="./src/micro_so/resources/prism/objects/documents/grant.py">update</a>(document_id, \*, path_team_id, \*\*<a href="src/micro_so/types/prism/objects/documents/grant_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/documents/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/document/{documentId}/grant">client.prism.objects.documents.grant.<a href="./src/micro_so/resources/prism/objects/documents/grant.py">get</a>(document_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/documents/grant_get_response.py">GrantGetResponse</a></code>

### Events

Types:

```python
from micro_so.types.prism.objects import (
    Event,
    EventCreateResponse,
    EventUpdateResponse,
    EventListResponse,
    EventCountResponse,
    EventDuplicateResponse,
    EventFindResponse,
    EventGetResponse,
    EventQueryResponse,
    EventRestoreResponse,
    EventUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/event">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/event_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_create_response.py">EventCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/event/{eventId}">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">update</a>(event_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/event_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_update_response.py">EventUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/event">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/event_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_list_response.py">EventListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/event/{eventId}">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">delete</a>(event_id, \*, team_id) -> None</code>
- <code title="get /v2/prism/{teamId}/event/count">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/event_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_count_response.py">EventCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/event/{eventId}/duplicate">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">duplicate</a>(event_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/event_duplicate_response.py">EventDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/event/by/{slug}/{value}">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/event_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_find_response.py">EventFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/event/{eventId}">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">get</a>(event_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/event_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_get_response.py">EventGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/event/query">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/event_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_query_response.py">EventQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/event/{eventId}/restore">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">restore</a>(event_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/event_restore_response.py">EventRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/event/by/{slug}/{value}">client.prism.objects.events.<a href="./src/micro_so/resources/prism/objects/events/events.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/event_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/event_upsert_response.py">EventUpsertResponse</a></code>

#### Grant

Types:

```python
from micro_so.types.prism.objects.events import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/{teamId}/event/{eventId}/grant">client.prism.objects.events.grant.<a href="./src/micro_so/resources/prism/objects/events/grant.py">update</a>(event_id, \*, path_team_id, \*\*<a href="src/micro_so/types/prism/objects/events/grant_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/events/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/event/{eventId}/grant">client.prism.objects.events.grant.<a href="./src/micro_so/resources/prism/objects/events/grant.py">get</a>(event_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/events/grant_get_response.py">GrantGetResponse</a></code>

### Engagements

Types:

```python
from micro_so.types.prism.objects import (
    Engagement,
    EngagementCreateResponse,
    EngagementUpdateResponse,
    EngagementListResponse,
    EngagementBulkCreateResponse,
    EngagementBulkDeleteResponse,
    EngagementBulkUpdateResponse,
    EngagementCountResponse,
    EngagementDuplicateResponse,
    EngagementFindResponse,
    EngagementGetResponse,
    EngagementQueryResponse,
    EngagementRestoreResponse,
    EngagementUpsertResponse,
)
```

Methods:

- <code title="post /v2/prism/{teamId}/engagement">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_create_response.py">EngagementCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/engagement/{engagementId}">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">update</a>(engagement_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_update_response.py">EngagementUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/engagement">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">list</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_list_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_list_response.py">EngagementListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/engagement/{engagementId}">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">delete</a>(engagement_id, \*, team_id) -> None</code>
- <code title="post /v2/prism/{teamId}/engagement/import">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">bulk_create</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_bulk_create_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_bulk_create_response.py">EngagementBulkCreateResponse</a></code>
- <code title="post /v2/prism/{teamId}/engagement/batch/delete">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">bulk_delete</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_bulk_delete_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_bulk_delete_response.py">EngagementBulkDeleteResponse</a></code>
- <code title="post /v2/prism/{teamId}/engagement/batch/update">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">bulk_update</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_bulk_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_bulk_update_response.py">EngagementBulkUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/engagement/count">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">count</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_count_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_count_response.py">EngagementCountResponse</a></code>
- <code title="post /v2/prism/{teamId}/engagement/{engagementId}/duplicate">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">duplicate</a>(engagement_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/engagement_duplicate_response.py">EngagementDuplicateResponse</a></code>
- <code title="get /v2/prism/{teamId}/engagement/by/{slug}/{value}">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">find</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/engagement_find_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_find_response.py">EngagementFindResponse</a></code>
- <code title="get /v2/prism/{teamId}/engagement/{engagementId}">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">get</a>(engagement_id, \*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_get_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_get_response.py">EngagementGetResponse</a></code>
- <code title="post /v2/prism/{teamId}/engagement/query">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">query</a>(\*, team_id, \*\*<a href="src/micro_so/types/prism/objects/engagement_query_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_query_response.py">EngagementQueryResponse</a></code>
- <code title="post /v2/prism/{teamId}/engagement/{engagementId}/restore">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">restore</a>(engagement_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/engagement_restore_response.py">EngagementRestoreResponse</a></code>
- <code title="put /v2/prism/{teamId}/engagement/by/{slug}/{value}">client.prism.objects.engagements.<a href="./src/micro_so/resources/prism/objects/engagements/engagements.py">upsert</a>(value, \*, team_id, slug, \*\*<a href="src/micro_so/types/prism/objects/engagement_upsert_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagement_upsert_response.py">EngagementUpsertResponse</a></code>

#### Grant

Types:

```python
from micro_so.types.prism.objects.engagements import GrantUpdateResponse, GrantGetResponse
```

Methods:

- <code title="put /v2/prism/{teamId}/engagement/{engagementId}/grant">client.prism.objects.engagements.grant.<a href="./src/micro_so/resources/prism/objects/engagements/grant.py">update</a>(engagement_id, \*, path_team_id, \*\*<a href="src/micro_so/types/prism/objects/engagements/grant_update_params.py">params</a>) -> <a href="./src/micro_so/types/prism/objects/engagements/grant_update_response.py">GrantUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/engagement/{engagementId}/grant">client.prism.objects.engagements.grant.<a href="./src/micro_so/resources/prism/objects/engagements/grant.py">get</a>(engagement_id, \*, team_id) -> <a href="./src/micro_so/types/prism/objects/engagements/grant_get_response.py">GrantGetResponse</a></code>

# Views

Types:

```python
from micro_so.types import ViewCreateResponse, ViewUpdateResponse, ViewListResponse, ViewGetResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/{objectType}/views">client.views.<a href="./src/micro_so/resources/views/views.py">create</a>(object_type, \*, path_team_id, \*\*<a href="src/micro_so/types/view_create_params.py">params</a>) -> <a href="./src/micro_so/types/view_create_response.py">ViewCreateResponse</a></code>
- <code title="patch /v2/prism/{teamId}/{objectType}/views/{viewId}">client.views.<a href="./src/micro_so/resources/views/views.py">update</a>(view_id, \*, path_team_id, object_type, \*\*<a href="src/micro_so/types/view_update_params.py">params</a>) -> <a href="./src/micro_so/types/view_update_response.py">ViewUpdateResponse</a></code>
- <code title="get /v2/prism/{teamId}/{objectType}/views">client.views.<a href="./src/micro_so/resources/views/views.py">list</a>(object_type, \*, team_id, \*\*<a href="src/micro_so/types/view_list_params.py">params</a>) -> <a href="./src/micro_so/types/view_list_response.py">ViewListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/{objectType}/views/{viewId}">client.views.<a href="./src/micro_so/resources/views/views.py">delete</a>(view_id, \*, team_id, object_type) -> None</code>
- <code title="get /v2/prism/{teamId}/{objectType}/views/{viewId}">client.views.<a href="./src/micro_so/resources/views/views.py">get</a>(view_id, \*, team_id, object_type, \*\*<a href="src/micro_so/types/view_get_params.py">params</a>) -> <a href="./src/micro_so/types/view_get_response.py">ViewGetResponse</a></code>

## Records

Types:

```python
from micro_so.types.views import RecordListResponse
```

Methods:

- <code title="get /v2/prism/{teamId}/{objectType}/views/{viewId}/records">client.views.records.<a href="./src/micro_so/resources/views/records.py">list</a>(view_id, \*, team_id, object_type, \*\*<a href="src/micro_so/types/views/record_list_params.py">params</a>) -> <a href="./src/micro_so/types/views/record_list_response.py">RecordListResponse</a></code>
- <code title="post /v2/prism/{teamId}/{objectType}/views/{viewId}/records/{objectId}">client.views.records.<a href="./src/micro_so/resources/views/records.py">pin</a>(object_id, \*, team_id, object_type, view_id) -> None</code>
- <code title="patch /v2/prism/{teamId}/{objectType}/views/{viewId}/records">client.views.records.<a href="./src/micro_so/resources/views/records.py">reorder</a>(view_id, \*, team_id, object_type, \*\*<a href="src/micro_so/types/views/record_reorder_params.py">params</a>) -> None</code>
- <code title="delete /v2/prism/{teamId}/{objectType}/views/{viewId}/records/{objectId}">client.views.records.<a href="./src/micro_so/resources/views/records.py">unpin</a>(object_id, \*, team_id, object_type, view_id) -> None</code>

# TriggeredAutomations

Types:

```python
from micro_so.types import TriggeredAutomation, TriggeredAutomationListResponse
```

Methods:

- <code title="post /v2/prism/{teamId}/{automationObjectType}/triggered_automations">client.triggered_automations.<a href="./src/micro_so/resources/triggered_automations.py">create</a>(automation_object_type, \*, path_team_id, \*\*<a href="src/micro_so/types/triggered_automation_create_params.py">params</a>) -> <a href="./src/micro_so/types/triggered_automation.py">TriggeredAutomation</a></code>
- <code title="put /v2/prism/{teamId}/{automationObjectType}/triggered_automations/{automationId}">client.triggered_automations.<a href="./src/micro_so/resources/triggered_automations.py">update</a>(automation_id, \*, path_team_id, automation_object_type, \*\*<a href="src/micro_so/types/triggered_automation_update_params.py">params</a>) -> <a href="./src/micro_so/types/triggered_automation.py">TriggeredAutomation</a></code>
- <code title="get /v2/prism/{teamId}/{automationObjectType}/triggered_automations">client.triggered_automations.<a href="./src/micro_so/resources/triggered_automations.py">list</a>(automation_object_type, \*, team_id, \*\*<a href="src/micro_so/types/triggered_automation_list_params.py">params</a>) -> <a href="./src/micro_so/types/triggered_automation_list_response.py">TriggeredAutomationListResponse</a></code>
- <code title="delete /v2/prism/{teamId}/{automationObjectType}/triggered_automations/{automationId}">client.triggered_automations.<a href="./src/micro_so/resources/triggered_automations.py">delete</a>(automation_id, \*, team_id, automation_object_type) -> None</code>
- <code title="get /v2/prism/{teamId}/{automationObjectType}/triggered_automations/{automationId}">client.triggered_automations.<a href="./src/micro_so/resources/triggered_automations.py">get</a>(automation_id, \*, team_id, automation_object_type) -> <a href="./src/micro_so/types/triggered_automation.py">TriggeredAutomation</a></code>

# Webhooks

Types:

```python
from micro_so.types import (
    Webhook,
    WebhookCreate,
    WebhookDelivery,
    WebhookDeliveryDetail,
    WebhookUpdate,
    WebhookWithSecret,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookListDeliveriesResponse,
    WebhookPingResponse,
    WebhookVerifyResponse,
)
```

Methods:

- <code title="post /v2/webhooks/{teamId}">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">create</a>(\*, team_id, \*\*<a href="src/micro_so/types/webhook_create_params.py">params</a>) -> <a href="./src/micro_so/types/webhook_with_secret.py">WebhookWithSecret</a></code>
- <code title="patch /v2/webhooks/{teamId}/{webhookId}">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">update</a>(webhook_id, \*, team_id, \*\*<a href="src/micro_so/types/webhook_update_params.py">params</a>) -> <a href="./src/micro_so/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /v2/webhooks/{teamId}">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">list</a>(\*, team_id) -> <a href="./src/micro_so/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v2/webhooks/{teamId}/{webhookId}">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">delete</a>(webhook_id, \*, team_id) -> None</code>
- <code title="get /v2/webhooks/{teamId}/{webhookId}">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">get</a>(webhook_id, \*, team_id) -> <a href="./src/micro_so/types/webhook.py">Webhook</a></code>
- <code title="get /v2/webhooks/{teamId}/deliveries">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">list_deliveries</a>(\*, team_id, \*\*<a href="src/micro_so/types/webhook_list_deliveries_params.py">params</a>) -> <a href="./src/micro_so/types/webhook_list_deliveries_response.py">WebhookListDeliveriesResponse</a></code>
- <code title="post /v2/webhooks/{teamId}/{webhookId}/ping">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">ping</a>(webhook_id, \*, team_id, \*\*<a href="src/micro_so/types/webhook_ping_params.py">params</a>) -> <a href="./src/micro_so/types/webhook_ping_response.py">WebhookPingResponse</a></code>
- <code title="post /v2/webhooks/{teamId}/{webhookId}/verify">client.webhooks.<a href="./src/micro_so/resources/webhooks/webhooks.py">verify</a>(webhook_id, \*, team_id) -> <a href="./src/micro_so/types/webhook_verify_response.py">WebhookVerifyResponse</a></code>

## Deliveries

Types:

```python
from micro_so.types.webhooks import DeliveryListResponse
```

Methods:

- <code title="get /v2/webhooks/{teamId}/{webhookId}/deliveries">client.webhooks.deliveries.<a href="./src/micro_so/resources/webhooks/deliveries.py">list</a>(webhook_id, \*, team_id, \*\*<a href="src/micro_so/types/webhooks/delivery_list_params.py">params</a>) -> <a href="./src/micro_so/types/webhooks/delivery_list_response.py">DeliveryListResponse</a></code>
- <code title="get /v2/webhooks/{teamId}/{webhookId}/deliveries/{deliveryId}">client.webhooks.deliveries.<a href="./src/micro_so/resources/webhooks/deliveries.py">get</a>(delivery_id, \*, team_id, webhook_id) -> <a href="./src/micro_so/types/webhook_delivery_detail.py">WebhookDeliveryDetail</a></code>

# Realtime

Types:

```python
from micro_so.types import RealtimeCreateTicketResponse
```

Methods:

- <code title="post /v2/realtime/ticket">client.realtime.<a href="./src/micro_so/resources/realtime.py">create_ticket</a>() -> <a href="./src/micro_so/types/realtime_create_ticket_response.py">RealtimeCreateTicketResponse</a></code>
