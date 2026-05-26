# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ImportJobGetResponse", "Error", "Result", "ResultError"]


class Error(BaseModel):
    """Set when status=failed; describes the job-level failure (not per-row)."""

    code: Optional[str] = None

    message: Optional[str] = None


class ResultError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None


class Result(BaseModel):
    id: Optional[str] = None

    created: Optional[bool] = None

    error: Optional[ResultError] = None

    existing: Optional[bool] = None
    """True if the row matched an existing record via the dedupe key."""


class ImportJobGetResponse(BaseModel):
    """Status snapshot of an import job.

    Same shape used by the POST /import response and by GET /imports/{jobId}.
    """

    job_id: Optional[str] = None
    """Null for sync imports (results inlined). Set for async imports."""

    status: Literal["complete", "processing", "failed"]

    total: int
    """Total number of rows in the import."""

    created_at: Optional[datetime] = None

    error: Optional[Error] = None
    """Set when status=failed; describes the job-level failure (not per-row)."""

    expires_at: Optional[datetime] = None

    failed: Optional[int] = None

    processed: Optional[int] = None
    """Rows that have been attempted (succeeded + failed)."""

    results: Optional[List[Result]] = None
    """Per-row outcomes.

    Always present for sync imports; populated for async imports once the job
    reaches `complete`.
    """

    succeeded: Optional[int] = None

    updated_at: Optional[datetime] = None
