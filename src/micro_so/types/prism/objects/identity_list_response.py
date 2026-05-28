# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["IdentityListResponse", "Data"]


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

    source: Optional[List[str]] = None


class IdentityListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """
    Accurate end-of-data signal — false on the last page, never forces clients to
    overshoot.
    """

    next_cursor: Optional[str] = None

    total: Optional[int] = None
    """Populated only when `?include_total=true` was passed."""
