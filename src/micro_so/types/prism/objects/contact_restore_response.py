# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["ContactRestoreResponse"]


class ContactRestoreResponse(BaseModel):
    """Object returned by reads (get/create/patch/restore). id is always present."""

    id: str

    crm: Optional[object] = None

    default: Optional[Dict[str, object]] = None
    """Properties keyed by property slug."""

    extended: Optional[object] = None
