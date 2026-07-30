# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["PropertyOption"]


class PropertyOption(BaseModel):
    """An enabled option for a select_str or multiselect_str property definition."""

    id: str

    slug: str

    color_scheme: Optional[str] = None

    crm_id: Optional[str] = None

    description: Optional[str] = None

    icon: Optional[str] = None

    list_id: Optional[str] = None

    option_group: Optional[str] = None

    sort_index: Optional[int] = None

    value: Optional[str] = None
    """Display value for the option."""
