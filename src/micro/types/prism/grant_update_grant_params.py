# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..object_type import ObjectType

__all__ = ["GrantUpdateGrantParams"]


class GrantUpdateGrantParams(TypedDict, total=False):
    path_team_id: Annotated[str, PropertyInfo(alias="teamId")]

    object_type: Required[Annotated[ObjectType, PropertyInfo(alias="objectType")]]

    team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]]

    body_team_id: Annotated[Dict[str, Literal["a", "r", "w"]], PropertyInfo(alias="team_id")]

    user_id: Iterable[Dict[str, Literal["a", "r", "w"]]]
