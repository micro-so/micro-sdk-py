# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContactBulkUpdateParams", "Item"]


class ContactBulkUpdateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    items: Required[Iterable[Item]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Item(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Object with `id` plus the same property body shape as PATCH (`default`/`list`/`extended`).
    """

    id: Required[str]
