# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["OrganizationQueryResponse", "Data"]


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


class OrganizationQueryResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Accurate end-of-data signal.

    False when this page contains the last record; true only when at least one more
    record exists. (Implementation note: the server fetches one extra row internally
    to determine this — clients never need to overshoot to discover the end.)
    """

    next_cursor: Optional[str] = None
    """Opaque cursor pointing at the next page.

    Pass it back unchanged in the request body (`cursor`) of the next call. Null
    when `has_more` is false.
    """

    total: Optional[int] = None
    """Only populated when the request set `include_total: true`.

    Total number of records matching the query, ignoring pagination. Opt-in because
    it costs an additional pass over the result set.
    """
