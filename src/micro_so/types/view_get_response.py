# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ViewGetResponse"]


class ViewGetResponse(BaseModel):
    """
    A view (saved configuration for displaying records of a given object type) plus its select/filter/sort children. Properties in select/filter/sort are referenced by slug.
    """

    name: str

    view_type: str

    id: Optional[str] = None

    aggregation_prop_def_id: Optional[str] = None

    aggregation_type: Optional[str] = None

    column_layout: Optional[Dict[str, object]] = None

    combinator: Optional[Literal["AND", "OR"]] = None

    created_at: Optional[str] = None

    filter: Optional[List[Dict[str, object]]] = None
    """Each entry is { slug: { comparator: value } }"""

    group_by: Optional[str] = None
    """Property slug to group by"""

    group_hidden_option_ids: Union[List[object], object, None] = None

    group_hide_empty: Optional[bool] = None

    group_sort: Optional[str] = None

    icon: Optional[str] = None

    list_id: Optional[str] = None

    select: Optional[List[str]] = None
    """Property slugs (dot-paths permitted for refs)"""

    sort: Optional[List[Dict[str, object]]] = None
    """Each entry is { slug: 'asc' | 'desc' }"""

    sort_order: Optional[int] = None

    team_id: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None
