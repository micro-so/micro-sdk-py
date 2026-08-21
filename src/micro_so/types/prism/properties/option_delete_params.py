# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OptionDeleteParams"]


class OptionDeleteParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    object_type: Required[
        Annotated[
            Literal[
                "comment",
                "deal",
                "engagement",
                "identity",
                "ai_chat_thread",
                "ai_chat_message",
                "agent_site",
                "document",
                "action",
                "event",
                "organization",
                "contact",
            ],
            PropertyInfo(alias="objectType"),
        ]
    ]
    """Object types that support CRUD, query, list, and per-type property metadata.

    `GET /v2/prism/{teamId}/properties` (list-all) also returns definitions for
    pipeline-owned types that are not in this set — including `message`, `thread`,
    and `linkedin_thread`. Those types are not queryable. Contacts expose
    `last_email` as a `ref_message`; you cannot query `message` to follow it.
    """

    property_id: Required[Annotated[str, PropertyInfo(alias="propertyId")]]

    type: Required[
        Literal[
            "num",
            "str",
            "bool",
            "date",
            "text",
            "byte",
            "select_str",
            "multi_str",
            "multiselect_str",
            "jsonb",
            "ref_identity",
            "ref_user",
            "ref_organization",
            "ref_contact",
            "ref_thread",
            "ref_message",
            "ref_event",
            "ref_account",
            "ref_ai_chat_thread",
            "ref_ai_chat_message",
            "multiref_ai_chat_message",
            "multiref_agent_site",
            "multiref_action",
            "multiref_comment",
            "multiref_contact",
            "multiref_label",
            "multiref_thread",
            "multiref_messages",
            "multiref_document",
            "multiref_identity",
            "multiref_organization",
            "multiref_engagement",
            "multiref_attendee",
            "multiref_meeting_entry",
            "multiref_read_receipt",
            "multiref_account",
            "multiref_source",
        ]
    ]
    """Storage type for a property definition.

    Determines which per-type table holds the values, and which display formats the
    property can take.
    """

    list_id: str
