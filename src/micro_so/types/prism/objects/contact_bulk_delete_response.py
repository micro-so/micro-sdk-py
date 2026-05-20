# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ContactBulkDeleteResponse", "Result", "ResultError", "ResultRecord", "Summary"]


class ResultError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None


class ResultRecord(BaseModel):
    """Object returned by reads (get/create/patch/restore). id is always present."""

    id: str

    default: Optional[Dict[str, object]] = None
    """Properties keyed by property slug."""

    list: Optional[object] = None


class Result(BaseModel):
    id: Optional[str] = None
    """Item ID, or null if the input was unparseable."""

    status: Literal["ok", "error"]

    error: Optional[ResultError] = None

    record: Optional[ResultRecord] = None
    """Object returned by reads (get/create/patch/restore). id is always present."""


class Summary(BaseModel):
    failed: int

    succeeded: int

    total: int


class ContactBulkDeleteResponse(BaseModel):
    """Partial-success bulk operation result.

    Inspect `results[].status` per item; the operation as a whole returns 200 even if some items failed.
    """

    results: List[Result]

    summary: Summary
