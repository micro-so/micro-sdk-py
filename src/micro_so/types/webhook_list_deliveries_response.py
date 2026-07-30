# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .webhook_delivery import WebhookDelivery

__all__ = ["WebhookListDeliveriesResponse"]


class WebhookListDeliveriesResponse(BaseModel):
    data: List[WebhookDelivery]

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page; null when there are no more."""
