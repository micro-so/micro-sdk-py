# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ViewUpdateParams"]


class ViewUpdateParams(TypedDict, total=False):
    path_team_id: Annotated[str, PropertyInfo(alias="teamId")]

    view_object_type: Required[
        Annotated[
            Literal["action", "deal", "document", "event", "identity", "organization"],
            PropertyInfo(alias="viewObjectType"),
        ]
    ]

    aggregation_prop_def_id: Optional[str]

    aggregation_type: Optional[str]

    column_layout: Optional[Dict[str, object]]

    combinator: Literal["AND", "OR"]

    crm_id: Optional[str]

    filter: Iterable[Dict[str, object]]

    group_by: Optional[str]

    group_hidden_option_ids: Union[Iterable[object], object, None]

    group_hide_empty: Optional[bool]

    group_sort: Optional[str]

    icon: Optional[str]

    name: str

    select: SequenceNotStr[str]

    sort: Iterable[Dict[str, object]]

    sort_order: Optional[int]

    body_team_id: Annotated[Optional[str], PropertyInfo(alias="team_id")]

    user_id: Optional[str]

    view_type: str
