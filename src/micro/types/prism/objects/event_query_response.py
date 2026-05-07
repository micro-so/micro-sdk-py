# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["EventQueryResponse", "Data"]


class Data(BaseModel):
    """Object returned by reads (get/create/patch/restore). id is always present."""

    id: str

    crm: Optional[object] = None

    default: Optional[Dict[str, object]] = None
    """Properties keyed by property slug."""

    extended: Optional[object] = None


class EventQueryResponse(BaseModel):
    data: List[Data]

    has_more: Optional[bool] = None
    """True when the page returned the maximum number of rows; another page may exist."""
