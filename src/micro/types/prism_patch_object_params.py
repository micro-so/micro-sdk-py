# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .object_type import ObjectType

__all__ = ["PrismPatchObjectParams"]


class PrismPatchObjectParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    object_type: Required[Annotated[ObjectType, PropertyInfo(alias="objectType")]]

    id: str

    crm: object

    default: Dict[str, object]
    """Properties keyed by property slug.

    Values can be strings, numbers, booleans, arrays, or null.
    """

    extended: object
