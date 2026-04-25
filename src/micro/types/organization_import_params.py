# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .prism_object_properties_param import PrismObjectPropertiesParam

__all__ = ["OrganizationImportParams", "Options"]


class OrganizationImportParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    objects: Required[Iterable[PrismObjectPropertiesParam]]
    """Array of objects to import with their property values"""

    options: Options


class Options(TypedDict, total=False):
    case_insensitive: Annotated[bool, PropertyInfo(alias="caseInsensitive")]
    """Whether deduplication should be case insensitive"""

    crm_id: str
    """App/CRM ID for context (optional)"""

    dedupe_by: str
    """Property definition ID to deduplicate on"""

    dedupe_type: Literal["str", "multi_str", "multiref_contact"]
    """Type of the deduplication property"""
