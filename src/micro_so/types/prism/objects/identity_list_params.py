# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IdentityListParams"]


class IdentityListParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    cursor: str
    """Opaque cursor from a previous response's `next_cursor`.

    Pass it back unchanged to fetch the next page.
    """

    deleted: bool
    """Include soft-deleted records. Pass the literal string `true`."""

    include_total: bool
    """
    When set to `true`, the response includes a `total` field with the unpaginated
    row count. Costs an extra pass; prefer `GET .../count` for the unfiltered total.
    """

    limit: int
    """Maximum number of rows to return. Capped server-side at 50."""

    list_id: str
    """Scope properties to a specific list/app."""

    select: str
    """Comma-separated property slugs to return.

    Use dot notation for relationships. `id` is always returned at the top level.
    Defaults to all properties.
    """

    sort: str
    """Comma-separated list of slugs.

    Prefix with `-` for descending. Example: `sort=-updated_at,name`.
    """
