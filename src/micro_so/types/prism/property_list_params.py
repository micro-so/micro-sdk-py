# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyListParams"]


class PropertyListParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    autofill: bool

    list_id: str
    """Scope properties to a specific list/app."""

    term: str
