# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...prism_object_properties_param import PrismObjectPropertiesParam

__all__ = ["OrganizationBulkCreateParams", "Options"]


class OrganizationBulkCreateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    objects: Required[Iterable[PrismObjectPropertiesParam]]
    """Array of objects to import with property values keyed by slug"""

    options: Options

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Options(TypedDict, total=False):
    case_insensitive: Annotated[bool, PropertyInfo(alias="caseInsensitive")]
    """Whether deduplication should be case insensitive"""

    dedupe_by: str
    """Property slug to deduplicate on"""

    list_id: str
    """App/CRM ID for context (optional)"""
