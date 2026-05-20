# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ActionCountResponse"]


class ActionCountResponse(BaseModel):
    total: int
    """Number of records matching the access scope."""
