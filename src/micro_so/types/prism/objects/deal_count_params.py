# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DealCountParams"]


class DealCountParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    list_id: str
    """Scope the count to a specific list/app."""
