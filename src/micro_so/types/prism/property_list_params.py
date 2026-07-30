# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyListParams"]


class PropertyListParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    autofill: bool

    include_options: Union[bool, Literal["true", "false", "0", "1"]]
    """
    When false, return property definitions without hydrating select/multiselect
    option rows. Defaults to true server-side (parseIncludeOptions). Accepts boolean
    or query-string forms (true/false/0/1). Uses anyOf (not oneOf) so qs/AJV
    boolean-vs-string ambiguity does not 400 when Speakeasy SDKs send
    include_options=true.
    """

    list_id: str
    """Scope properties to a specific list/app.

    Scoping is strict: the response carries only that list's definitions, not the
    workspace-global ones that also apply to its records. Call once with `list_id`
    and once without to see everything a write could resolve against.
    """

    term: str
    """Case-insensitive substring match on the property name.

    Use this to find an existing property before creating a new one.
    """
