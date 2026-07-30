# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...prism_object_properties_param import PrismObjectPropertiesParam

__all__ = ["IdentityBulkCreateParams", "Options"]


class IdentityBulkCreateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    objects: Required[Iterable[PrismObjectPropertiesParam]]
    """Array of objects to import with property values keyed by slug"""

    options: Options

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Options(TypedDict, total=False):
    case_insensitive: Annotated[bool, PropertyInfo(alias="caseInsensitive")]
    """Whether deduplication should be case insensitive"""

    create_missing_options: bool
    """
    When true, unknown values for select/multiselect properties are created as new
    options instead of failing the import
    """

    crm_id: str
    """Deprecated alias for list_id."""

    dedupe_by: Union[str, SequenceNotStr[str]]
    """Property slug to deduplicate on.

    A single-element array is also accepted; compound (multi-slug) dedupe is not
    supported yet and is rejected with guidance.
    """

    list_id: str
    """App/CRM ID for context (optional)"""

    require_list_stage: bool
    """Require app_stage for every row in the selected list.

    app_stage is a reserved list-scoped alias for native status.
    """

    update_existing: bool
    """
    Patch a deduplicated record with the supplied properties instead of skipping it.
    """
