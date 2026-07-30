# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookDelivery"]


class WebhookDelivery(BaseModel):
    """
    A webhook delivery — one logical event delivery to an endpoint, grouping its attempts. Status and status_code reflect the latest attempt.
    """

    created_at: datetime

    delivery_id: str

    status: Literal["success", "failed"]

    type: Literal["delivery", "verification"]

    webhook_id: str

    attempts: Optional[int] = None
    """Number of attempts made so far (including async retries)."""

    event: Optional[str] = None
    """Event name (e.g. `webhook.test`); `verification` for handshake runs."""

    status_code: Optional[int] = None
    """HTTP status of the latest attempt; null on a transport error."""

    team_id: Optional[str] = None

    updated_at: Optional[datetime] = None

    url: Optional[str] = None
