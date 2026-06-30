# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OrganizationBulkUpdateParams", "Item"]


class OrganizationBulkUpdateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    items: Required[Iterable[Item]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Item(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """
    Object with `id` plus the same property body shape as PATCH (`default`/`list`/`extended`).
    """

    id: Required[str]
