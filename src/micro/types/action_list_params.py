# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ActionListParams", "Query"]


class ActionListParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    query: Required[Query]

    id: Union[str, SequenceNotStr[str]]

    boxes: SequenceNotStr[str]

    deleted: bool

    sources: SequenceNotStr[str]


class Query(TypedDict, total=False):
    select: Required[SequenceNotStr[str]]
    """Property slugs to select.

    Use dot notation for relationships (e.g. attendee.contact.first_name)
    """

    combinator: Literal["AND", "OR"]
    """Logical operator for combining filters"""

    crm_id: str

    filter: Iterable[Dict[str, Dict[str, Union[str, bool, SequenceNotStr[str]]]]]
    """Filters as [{ slug: { operator: value } }]"""

    limit: int

    page: int

    sort: Iterable[Dict[str, Literal["asc", "desc"]]]
    """Sort order as [{ slug: direction }]. Array order determines sort priority"""
