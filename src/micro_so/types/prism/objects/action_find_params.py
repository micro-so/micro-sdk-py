# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionFindParams"]


class ActionFindParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    slug: Required[str]

    list_id: str
    """Scope the lookup to a specific list/app."""
