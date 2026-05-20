# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecordListParams"]


class RecordListParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    view_object_type: Required[
        Annotated[
            Literal["action", "deal", "document", "event", "identity", "organization"],
            PropertyInfo(alias="viewObjectType"),
        ]
    ]

    cursor: str
    """Opaque cursor from a previous response's `next_cursor`.

    Pass it back unchanged to fetch the next page. When set, `page` and `limit` are
    derived from the cursor.
    """

    limit: int

    page: int
    """Page number (1-based). Prefer `cursor`."""
