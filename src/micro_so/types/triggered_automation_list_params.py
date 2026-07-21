# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggeredAutomationListParams"]


class TriggeredAutomationListParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    cursor: str
    """
    Opaque pagination cursor (from a prior response's next_cursor); supersedes
    page/limit when present.
    """

    kind: Literal["update", "lifecycle"]
    """Optional filter to a single automation kind.

    When omitted, both kinds are returned.
    """

    limit: int
    """Maximum items per page (<= 50; defaults to 50)."""

    list_id: str
    """List (CRM) id to scope the listing to.

    When omitted, automations owned by the path team are returned.
    """

    page: int
    """1-based page number. Prefer cursor."""
