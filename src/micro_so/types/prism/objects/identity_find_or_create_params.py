# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IdentityFindOrCreateParams", "Match"]


class IdentityFindOrCreateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    match: Required[Match]

    defaults: Dict[str, object]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Match(TypedDict, total=False):
    email_address: Required[str]
