# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["GrantUpdateParams"]


class GrantUpdateParams(TypedDict, total=False):
    path_team_id: Annotated[str, PropertyInfo(alias="teamId")]

    share_level: Literal["metadata", "full"]
    """How much of the record the grant exposes.

    `metadata` shares only the record's headers and participants; `full` shares its
    contents. Currently recorded on the access row and returned on read — it is not
    yet enforced by the read path. Applies to `message` grants; ignored for other
    object types.
    """

    team_group_id: Iterable[Dict[str, Literal["a", "r", "w"]]]

    body_team_id: Annotated[Dict[str, Literal["a", "r", "w"]], PropertyInfo(alias="team_id")]

    user_id: Iterable[Dict[str, Literal["a", "r", "w"]]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
