# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DealGetParams"]


class DealGetParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    select: str
    """Comma-separated property slugs to return.

    Use dot notation for relationships. `id` is always returned at the top level.
    Defaults to all properties.
    """
