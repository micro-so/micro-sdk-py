# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookWithSecret", "WebhookWithSecretVerification"]


class WebhookWithSecretVerification(BaseModel):
    """Status of the verification handshake enqueued by this request.

    The handshake runs asynchronously in the dispatcher; poll the webhook (its `verified` flag flips to true on success) to observe the outcome.
    """

    status: Literal["pending"]
    """
    Always `pending` at the moment of the response — the dispatcher has been asked
    to run the handshake but has not reported back yet.
    """


class WebhookWithSecret(Webhook):
    """Returned ONLY on creation.

    Includes the signing secret (shown once) and the pending verification status.
    """

    secret: str
    """HMAC signing secret (prefix `whsec_`).

    Store it now — it is never returned again. The dispatcher signs each delivered
    payload with it so your endpoint can verify authenticity.
    """

    verification: Optional[WebhookWithSecretVerification] = None
    """Status of the verification handshake enqueued by this request.

    The handshake runs asynchronously in the dispatcher; poll the webhook (its
    `verified` flag flips to true on success) to observe the outcome.
    """
