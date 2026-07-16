# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .triggered_automation import TriggeredAutomation

__all__ = ["TriggeredAutomationListResponse"]


class TriggeredAutomationListResponse(BaseModel):
    data: List[TriggeredAutomation]

    has_more: bool
    """True if more automations exist beyond this page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page; null when has_more is false."""
