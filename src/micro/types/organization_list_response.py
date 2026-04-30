# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OrganizationListResponse"]


class OrganizationListResponse(BaseModel):
    data: Optional[List[object]] = None

    total: Optional[int] = None
