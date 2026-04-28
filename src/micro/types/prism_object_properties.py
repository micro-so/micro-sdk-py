# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["PrismObjectProperties"]


class PrismObjectProperties(BaseModel):
    id: Optional[str] = None

    crm: Optional[object] = None

    default: Optional[Dict[str, object]] = None
    """Properties keyed by property slug.

    Values can be strings, numbers, booleans, arrays, or null.
    """

    extended: Optional[object] = None
