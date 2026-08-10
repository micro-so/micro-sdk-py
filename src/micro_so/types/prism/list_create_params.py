# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListCreateParams"]


class ListCreateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    template_id: Required[
        Literal[
            "sales_deals",
            "recruiting",
            "partnerships",
            "fundraising",
            "knowledge_base",
            "issue_tracker",
            "content_calendar",
            "job_applications",
            "project_tracker",
            "feedback",
            "portco_tracker",
            "deal_flow",
            "lp_fundraising",
            "custom",
        ]
    ]
    """Template to seed the list from.

    `type` is derived server-side from this template.
    """

    icon: str
    """Emoji or icon override."""

    name: str

    object_type: Literal["organization", "identity", "action", "document", "deal"]
    """Required only when template_id is `custom`."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
