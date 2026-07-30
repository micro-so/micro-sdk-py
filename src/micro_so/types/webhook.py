# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    """A registered webhook endpoint."""

    id: str

    created_at: datetime

    enabled: bool
    """Disabled webhooks are skipped at delivery time."""

    name: str

    team_id: str

    url: str
    """Endpoint events are delivered to."""

    verified: bool
    """True once the endpoint has completed the verification handshake."""

    description: Optional[str] = None

    updated_at: Optional[datetime] = None

    verification_token: Optional[str] = None
    """
    Stable token replayed to the endpoint (as the `micro_hook_token` query param)
    during the verification handshake. The endpoint may check it to confirm the
    request originated from Micro.
    """

    verified_at: Optional[datetime] = None
