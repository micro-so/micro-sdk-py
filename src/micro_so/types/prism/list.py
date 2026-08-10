# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import typing
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["List", "View"]


class View(BaseModel):
    id: str

    name: typing.Optional[str] = None


class List(BaseModel):
    id: str

    name: str

    object_type: Literal["organization", "identity", "action", "document", "deal"]
    """Prism object type this list holds."""

    team_id: str

    created_at: typing.Optional[datetime] = None

    description: typing.Optional[str] = None

    icon: typing.Optional[str] = None
    """Emoji or icon key for the list."""

    type: typing.Optional[str] = None
    """Internal template type (e.g.

    dealFlow, hiring). Derived from template_id on create.
    """

    views: typing.Optional[typing.List[View]] = None
