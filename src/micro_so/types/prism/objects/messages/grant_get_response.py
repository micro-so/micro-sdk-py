# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["GrantGetResponse"]


class GrantGetResponse(BaseModel):
    """The grants on a record.

    For `message`, also carries the entity ids of everyone on the message, resolved from its address headers when the grant was written. The id arrays are read-only and are null when participant resolution was unavailable (for example the mailbox had no Gmail token at the time).
    """

    contact_ids: Optional[List[str]] = None

    group_id: Optional[Dict[str, Literal["a", "r", "w"]]] = None

    identity_ids: Optional[List[str]] = None

    organization_ids: Optional[List[str]] = None

    share_level: Optional[Literal["metadata", "full"]] = None
    """How much of the record the grant exposes.

    `metadata` shares only the record's headers and participants; `full` shares its
    contents. Currently recorded on the access row and returned on read — it is not
    yet enforced by the read path. Applies to `message` grants; ignored for other
    object types.
    """

    team_id: Optional[Dict[str, Literal["a", "r", "w"]]] = None

    user_id: Optional[Dict[str, Literal["a", "r", "w"]]] = None
