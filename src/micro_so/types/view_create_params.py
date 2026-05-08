# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ViewCreateParams"]


class ViewCreateParams(TypedDict, total=False):
    path_team_id: Annotated[str, PropertyInfo(alias="teamId")]

    name: Required[str]

    view_type: Required[str]

    id: str

    aggregation_prop_def_id: Optional[str]

    aggregation_type: Optional[str]

    column_layout: Optional[Dict[str, object]]

    combinator: Literal["AND", "OR"]

    created_at: str

    crm_id: Optional[str]

    filter: Iterable[Dict[str, object]]
    """Each entry is { slug: { comparator: value } }"""

    group_by: Optional[str]
    """Property slug to group by"""

    group_hidden_option_ids: Union[Iterable[object], object, None]

    group_hide_empty: Optional[bool]

    group_sort: Optional[str]

    icon: Optional[str]

    select: SequenceNotStr[str]
    """Property slugs (dot-paths permitted for refs)"""

    sort: Iterable[Dict[str, object]]
    """Each entry is { slug: 'asc' | 'desc' }"""

    sort_order: Optional[int]

    body_team_id: Annotated[Optional[str], PropertyInfo(alias="team_id")]

    updated_at: Optional[str]

    user_id: Optional[str]
