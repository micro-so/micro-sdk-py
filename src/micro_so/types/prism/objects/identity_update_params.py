# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IdentityUpdateParams"]


class IdentityUpdateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    default: Dict[str, object]
    """Properties keyed by property slug.

    Values can be strings, numbers, booleans, arrays, or null. For
    select/multiselect properties, values may be option slugs or option UUIDs on
    write; option slugs are returned on read.
    """

    list: object

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]
