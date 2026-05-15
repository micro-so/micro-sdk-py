# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "OrganizationQueryParams",
    "Query",
    "QueryFilterQueryFilterItem",
    "QueryFilterQueryFilterItemPrismQueryFilterEq",
    "QueryFilterQueryFilterItemPrismQueryFilterNe",
    "QueryFilterQueryFilterItemPrismQueryFilterLt",
    "QueryFilterQueryFilterItemPrismQueryFilterGt",
    "QueryFilterQueryFilterItemPrismQueryFilterLte",
    "QueryFilterQueryFilterItemPrismQueryFilterGte",
    "QueryFilterQueryFilterItemLikeRegex",
    "QueryFilterQueryFilterItemBeginsWith",
    "QueryFilterQueryFilterItemEndsWith",
    "QueryFilterQueryFilterItemNotContains",
    "QueryFilterQueryFilterItemExists",
    "QueryFilterQueryFilterItemNotExists",
    "QueryFilterQueryFilterItemIn",
    "QueryFilterQueryFilterItemNotIn",
]


class OrganizationQueryParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    query: Required[Query]

    id: Union[str, SequenceNotStr[str]]

    boxes: SequenceNotStr[str]

    deleted: bool

    sources: SequenceNotStr[str]


class QueryFilterQueryFilterItemPrismQueryFilterEq(TypedDict, total=False):
    api_empty: Required[Annotated[Union[str, bool], PropertyInfo(alias="=")]]


class QueryFilterQueryFilterItemPrismQueryFilterNe(TypedDict, total=False):
    api_empty: Required[Annotated[Union[str, bool], PropertyInfo(alias="!=")]]


class QueryFilterQueryFilterItemPrismQueryFilterLt(TypedDict, total=False):
    api_empty: Required[Annotated[str, PropertyInfo(alias="<")]]


class QueryFilterQueryFilterItemPrismQueryFilterGt(TypedDict, total=False):
    api_empty: Required[Annotated[str, PropertyInfo(alias=">")]]


class QueryFilterQueryFilterItemPrismQueryFilterLte(TypedDict, total=False):
    api_empty: Required[Annotated[str, PropertyInfo(alias="<=")]]


class QueryFilterQueryFilterItemPrismQueryFilterGte(TypedDict, total=False):
    api_empty: Required[Annotated[str, PropertyInfo(alias=">=")]]


class QueryFilterQueryFilterItemLikeRegex(TypedDict, total=False):
    like_regex: Required[str]


class QueryFilterQueryFilterItemBeginsWith(TypedDict, total=False):
    begins_with: Required[str]


class QueryFilterQueryFilterItemEndsWith(TypedDict, total=False):
    ends_with: Required[str]


class QueryFilterQueryFilterItemNotContains(TypedDict, total=False):
    not_contains: Required[str]


class QueryFilterQueryFilterItemExists(TypedDict, total=False):
    exists: Required[bool]


class QueryFilterQueryFilterItemNotExists(TypedDict, total=False):
    not_exists: Required[bool]


_QueryFilterQueryFilterItemInReservedKeywords = TypedDict(
    "_QueryFilterQueryFilterItemInReservedKeywords",
    {
        "in": SequenceNotStr[str],
    },
    total=False,
)


class QueryFilterQueryFilterItemIn(_QueryFilterQueryFilterItemInReservedKeywords, total=False):
    pass


class QueryFilterQueryFilterItemNotIn(TypedDict, total=False):
    not_in: Required[SequenceNotStr[str]]


QueryFilterQueryFilterItem: TypeAlias = Union[
    QueryFilterQueryFilterItemPrismQueryFilterEq,
    QueryFilterQueryFilterItemPrismQueryFilterNe,
    QueryFilterQueryFilterItemPrismQueryFilterLt,
    QueryFilterQueryFilterItemPrismQueryFilterGt,
    QueryFilterQueryFilterItemPrismQueryFilterLte,
    QueryFilterQueryFilterItemPrismQueryFilterGte,
    QueryFilterQueryFilterItemLikeRegex,
    QueryFilterQueryFilterItemBeginsWith,
    QueryFilterQueryFilterItemEndsWith,
    QueryFilterQueryFilterItemNotContains,
    QueryFilterQueryFilterItemExists,
    QueryFilterQueryFilterItemNotExists,
    QueryFilterQueryFilterItemIn,
    QueryFilterQueryFilterItemNotIn,
]


class Query(TypedDict, total=False):
    select: Required[SequenceNotStr[str]]
    """Property slugs to select.

    Use dot notation for relationships (e.g. attendee.contact.first_name)
    """

    combinator: Literal["AND", "OR"]
    """Logical operator for combining filters"""

    filter: Iterable[Dict[str, QueryFilterQueryFilterItem]]
    """Filters as [{ slug: { operator: value } }].

    For select/multiselect properties, values may be option slugs or option UUIDs.
    """

    limit: int

    list_id: str

    page: int

    sort: Iterable[Dict[str, Literal["asc", "desc"]]]
    """Sort order as [{ slug: direction }]. Array order determines sort priority"""
