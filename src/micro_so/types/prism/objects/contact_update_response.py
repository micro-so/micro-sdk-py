# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["ContactUpdateResponse"]


class ContactUpdateResponse(BaseModel):
    """Object returned by reads (get/create/patch/restore). id is always present."""

    id: str

    default: Optional[Dict[str, object]] = None
    """Properties keyed by property slug."""

    list: Optional[object] = None
