# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["GrantUpdateParams"]


class GrantUpdateParams(TypedDict, total=False):
    path_team_id: Annotated[str, PropertyInfo(alias="teamId")]

    team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]]

    body_team_id: Annotated[Dict[str, Literal["a", "r", "w"]], PropertyInfo(alias="team_id")]

    user_id: Iterable[Dict[str, Literal["a", "r", "w"]]]
