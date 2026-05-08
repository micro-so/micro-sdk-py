# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["GrantGetResponse"]


class GrantGetResponse(BaseModel):
    team_group_id: Optional[List[Dict[str, Literal["a", "r", "w"]]]] = None

    team_id: Optional[Dict[str, Literal["a", "r", "w"]]] = None

    user_id: Optional[List[Dict[str, Literal["a", "r", "w"]]]] = None
