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
