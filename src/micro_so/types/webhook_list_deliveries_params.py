# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookListDeliveriesParams"]


class WebhookListDeliveriesParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    cursor: str
    """Opaque cursor from a previous response's `next_cursor`."""

    limit: int
    """Page size (1–100, default 25)."""

    status: Literal["success", "failed"]
    """Filter by outcome."""

    type: Literal["delivery", "verification", "all"]
    """Filter by run type.

    Defaults to `delivery` (event deliveries). Pass `all` to include verification
    handshakes.
    """
