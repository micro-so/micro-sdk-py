# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "EngagementQueryParams",
    "Query",
    "QueryFilterQueryFilterItem",
    "QueryFilterQueryFilterItemPrismQueryFilterEq",
    "QueryFilterQueryFilterItemPrismQueryFilterNe",
    "QueryFilterQueryFilterItemPrismQueryFilterLt",
    "QueryFilterQueryFilterItemPrismQueryFilterGt",
    "QueryFilterQueryFilterItemPrismQueryFilterLte",
    "QueryFilterQueryFilterItemPrismQueryFilterGte",
    "QueryFilterQueryFilterItemContains",
    "QueryFilterQueryFilterItemBeginsWith",
    "QueryFilterQueryFilterItemEndsWith",
    "QueryFilterQueryFilterItemNotContains",
    "QueryFilterQueryFilterItemExists",
    "QueryFilterQueryFilterItemNotExists",
    "QueryFilterQueryFilterItemIsNull",
    "QueryFilterQueryFilterItemIsNotNull",
    "QueryFilterQueryFilterItemBetween",
    "QueryFilterQueryFilterItemIn",
    "QueryFilterQueryFilterItemNotIn",
]


class EngagementQueryParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    query: Required[Query]

    id: Union[str, SequenceNotStr[str]]

    boxes: SequenceNotStr[str]

    cursor: str
    """Alternative location for the opaque cursor (a sibling of `query`).

    Use whichever feels more natural; if both are present, `query.cursor` wins.
    """

    deleted: bool

    include_total: bool
    """When true, the response includes a `total` field with the unpaginated row count.

    Costs an additional pass over the result set — for unfiltered totals prefer
    `GET /v2/prism/{teamId}/{objectType}/count` instead.
    """

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


class QueryFilterQueryFilterItemContains(TypedDict, total=False):
    contains: Required[Union[str, bool, SequenceNotStr[str]]]


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


class QueryFilterQueryFilterItemIsNull(TypedDict, total=False):
    is_null: Required[Union[str, bool, SequenceNotStr[str]]]


class QueryFilterQueryFilterItemIsNotNull(TypedDict, total=False):
    is_not_null: Required[Union[str, bool, SequenceNotStr[str]]]


class QueryFilterQueryFilterItemBetween(TypedDict, total=False):
    between: Required[Union[str, bool, SequenceNotStr[str]]]


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
    QueryFilterQueryFilterItemContains,
    QueryFilterQueryFilterItemBeginsWith,
    QueryFilterQueryFilterItemEndsWith,
    QueryFilterQueryFilterItemNotContains,
    QueryFilterQueryFilterItemExists,
    QueryFilterQueryFilterItemNotExists,
    QueryFilterQueryFilterItemIsNull,
    QueryFilterQueryFilterItemIsNotNull,
    QueryFilterQueryFilterItemBetween,
    QueryFilterQueryFilterItemIn,
    QueryFilterQueryFilterItemNotIn,
]


class Query(TypedDict, total=False):
    select: Required[SequenceNotStr[str]]
    """Property slugs to select.

    Use dot notation for relationships (e.g. attendee.contact.first_name). `id` is
    always returned at the top level of each row and does not need to be selected.
    """

    combinator: Literal["AND", "OR"]
    """Logical operator for combining filters"""

    cursor: str
    """Opaque cursor from a previous response's `next_cursor`.

    Pass it back unchanged to fetch the next page. When set, `page` and `limit` are
    derived from the cursor and any explicit values are ignored.
    """

    filter: Iterable[Dict[str, QueryFilterQueryFilterItem]]
    """Filters as [{ slug: { operator: value } }].

    For select/multiselect properties, values may be option slugs or option UUIDs.
    """

    limit: int
    """Maximum number of rows to return.

    Capped server-side at 50; requests above the cap are rejected.
    """

    list_id: str

    page: int
    """Page number (1-based).

    Prefer `cursor`. Page-number pagination drifts under concurrent writes; use it
    only for one-shot exports.
    """

    sort: Iterable[Dict[str, Literal["asc", "desc"]]]
    """Sort order as [{ slug: direction }]. Array order determines sort priority"""
