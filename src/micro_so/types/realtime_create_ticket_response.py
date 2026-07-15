# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RealtimeCreateTicketResponse"]


class RealtimeCreateTicketResponse(BaseModel):
    expires_in: int
    """Seconds until the ticket expires.

    Refresh (call the endpoint again) before reconnecting.
    """

    ticket: str
    """Short-lived token authenticating a realtime WebSocket connection.

    Pass as the `token` query parameter when connecting.
    """

    ws_url: Optional[str] = None
    """WebSocket URL for this environment (wss://stream.developers[.staging].micro.so).

    Connect here with the ticket as the `token` query parameter.
    """
