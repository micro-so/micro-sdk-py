# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ViewGetParams"]


class ViewGetParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    view_object_type: Required[
        Annotated[
            Literal["comment", "action", "deal", "engagement", "document", "event", "identity", "organization"],
            PropertyInfo(alias="viewObjectType"),
        ]
    ]

    cursor: str
    """Forwarded to the records sub-resource when `include=records`."""

    include: str
    """Comma-separated list of optional sub-resources to inline.

    Currently the only recognized value is `records` — when present, the response is
    `{view, records}` rather than the bare view bundle.
    """

    limit: int
    """Forwarded to the records sub-resource when `include=records`."""

    page: int
    """Forwarded to the records sub-resource when `include=records`."""
