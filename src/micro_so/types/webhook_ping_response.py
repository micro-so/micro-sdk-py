# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookPingResponse"]


class WebhookPingResponse(BaseModel):
    dispatched: bool

    event: str

    webhook_id: str
