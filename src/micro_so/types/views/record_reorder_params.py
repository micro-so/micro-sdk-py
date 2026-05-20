# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["RecordReorderParams"]


class RecordReorderParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    view_object_type: Required[
        Annotated[
            Literal["action", "deal", "document", "event", "identity", "organization"],
            PropertyInfo(alias="viewObjectType"),
        ]
    ]

    object_ids: Required[SequenceNotStr[str]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
