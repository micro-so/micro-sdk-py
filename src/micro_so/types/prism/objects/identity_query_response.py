# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["IdentityQueryResponse", "Data"]


class Data(BaseModel):
    """Row returned by the query endpoint.

    `id` is always present at the top level. Selected property values are returned under `properties`, keyed by property slug. Reference-typed values are returned as nested `{ id, properties }` objects.
    """

    id: str

    is_user_object: Optional[bool] = None

    properties: Optional[Dict[str, object]] = None
    """Selected property values keyed by property slug.

    For select/multiselect properties, option slugs are returned. For reference
    properties, values are nested `{ id, properties }` objects.
    """

    source: Optional[str] = None


class IdentityQueryResponse(BaseModel):
    data: List[Data]

    has_more: Optional[bool] = None
    """True when the page returned the maximum number of rows; another page may exist."""
