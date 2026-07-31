# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyCreateParams", "Option"]


class PropertyCreateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    name: Required[str]
    """Human-readable name, unique within the scope the definition is created in.

    A name already taken in that scope returns 409; the message names the existing
    definition's id, slug and type so you can write to it instead.
    """

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

    icon: Optional[str]

    list_id: Optional[str]
    """Scopes the definition to one list/app.

    Omit it only for a property that genuinely belongs to the whole workspace: a
    definition created without `list_id` is workspace-global and surfaces on every
    list of this object type.
    """

    options: Iterable[Option]
    """Only honored when `type` is `select_str` or `multiselect_str`."""

    required: bool
    """When true, records must carry a non-empty value for this property on create.

    Defaults to false.
    """

    role_id: Optional[str]
    """
    Optional display format for the property, drawn from the workspace's property
    roles. Omit it and the canonical role for `type` is applied (plain text, plain
    number, checkbox). Supply it only to pick a narrower format such as email, URL
    or currency; the role's data type must match `type`.
    """

    slug: str
    """URL-safe identifier.

    When omitted it defaults to a slugified `name` and is disambiguated with a
    numeric suffix on conflict. When supplied explicitly it is treated as part of
    your write contract and is never silently renamed — a collision returns 409
    instead.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Option(TypedDict, total=False):
    value: Required[str]

    color_scheme: Optional[str]

    description: Optional[str]

    icon: Optional[str]

    option_group: Optional[str]

    slug: str

    sort_index: Optional[int]
