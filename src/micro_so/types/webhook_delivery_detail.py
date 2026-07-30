# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .webhook_delivery import WebhookDelivery

__all__ = ["WebhookDeliveryDetail", "WebhookDeliveryDetailAttemptHistory"]


class WebhookDeliveryDetailAttemptHistory(BaseModel):
    """A single HTTP attempt within a delivery (including async retries)."""

    attempt: int
    """1-based attempt number."""

    created_at: datetime

    status: Literal["success", "failed"]

    error: Optional[str] = None
    """Failure reason, when status is failed."""

    request_body: Optional[str] = None
    """Body sent to the endpoint (delivery only); may be truncated."""

    response_body: Optional[str] = None
    """Body returned by the endpoint; may be truncated."""

    status_code: Optional[int] = None


class WebhookDeliveryDetail(WebhookDelivery):
    """A delivery plus its full attempt timeline."""

    attempt_history: Optional[List[WebhookDeliveryDetailAttemptHistory]] = None
