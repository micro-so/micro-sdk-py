# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookVerifyResponse", "WebhookVerifyResponseVerification"]


class WebhookVerifyResponseVerification(BaseModel):
    """Status of the verification handshake enqueued by this request.

    The handshake runs asynchronously in the dispatcher; poll the webhook (its `verified` flag flips to true on success) to observe the outcome.
    """

    status: Literal["pending"]
    """
    Always `pending` at the moment of the response — the dispatcher has been asked
    to run the handshake but has not reported back yet.
    """


class WebhookVerifyResponse(Webhook):
    """A webhook plus the status of a verification handshake enqueued by this request."""

    verification: Optional[WebhookVerifyResponseVerification] = None
    """Status of the verification handshake enqueued by this request.

    The handshake runs asynchronously in the dispatcher; poll the webhook (its
    `verified` flag flips to true on success) to observe the outcome.
    """
