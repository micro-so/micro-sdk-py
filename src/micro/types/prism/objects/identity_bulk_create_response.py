# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["IdentityBulkCreateResponse", "Result", "Summary"]


class Result(BaseModel):
    id: Optional[str] = None

    created: Optional[bool] = None

    error: Optional[str] = None

    existing: Optional[bool] = None


class Summary(BaseModel):
    created: Optional[int] = None

    errors: Optional[int] = None

    existing: Optional[int] = None

    total: Optional[int] = None


class IdentityBulkCreateResponse(BaseModel):
    results: Optional[List[Result]] = None

    status: Optional[Literal["complete"]] = None

    summary: Optional[Summary] = None
