# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .properties.property_option import PropertyOption

__all__ = ["PropertyDefinition"]


class PropertyDefinition(BaseModel):
    """Definition for a single property on an object type.

    Definitions with team_id and crm_id null are shared defaults; values may be scoped to a team and/or list (crm).
    """

    id: str

    slug: str

    type: Literal[
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
        "multiref_agent_artifact",
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
    """Storage type for a property definition.

    Determines which per-type table holds the values, and which display formats the
    property can take.
    """

    alias: Optional[Literal["app_stage"]] = None
    """Reserved alias naming this definition, or null.

    `app_stage` marks the list pipeline stage definition. Resolve stages by this
    field rather than by name, slug, or team_id: a superseded native `status`
    definition can coexist with the pipeline one and is otherwise identical on the
    wire.
    """

    crm_id: Optional[str] = None
    """Identifier of the list this definition is scoped to, when applicable."""

    list_id: Optional[str] = None
    """Canonical identifier of the list this definition is scoped to."""

    locked: Optional[bool] = None

    name: Optional[str] = None

    native: Optional[bool] = None

    options: Optional[List[PropertyOption]] = None
    """Present only for select_str and multiselect_str types."""

    required: Optional[bool] = None
    """
    When true, records of this object type must carry a non-empty value for this
    property on create, and a patch may not clear it.
    """

    role_id: Optional[str] = None
    """The property's display format.

    Always populated on definitions created through this API; a null here means the
    definition predates that and will render as an unknown format until it is
    patched.
    """

    team_id: Optional[str] = None
