# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["DocumentQueryResponse", "Data"]


class Data(BaseModel):
    """Object returned by reads (get/create/patch/restore). id is always present."""

    id: str

    default: Optional[Dict[str, object]] = None
    """Properties keyed by property slug."""

    list: Optional[object] = None


class DocumentQueryResponse(BaseModel):
    data: List[Data]

    has_more: Optional[bool] = None
    """True when the page returned the maximum number of rows; another page may exist."""
