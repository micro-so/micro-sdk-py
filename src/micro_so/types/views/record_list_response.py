# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["RecordListResponse"]


class RecordListResponse(BaseModel):
    data: List[Dict[str, object]]

    has_more: bool
    """True if more records exist beyond this page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null when `has_more` is false."""
