# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TriggeredAutomationUpdateParams", "Action", "Changeset", "State"]


class TriggeredAutomationUpdateParams(TypedDict, total=False):
    path_team_id: Annotated[str, PropertyInfo(alias="teamId")]

    automation_object_type: Required[
        Annotated[
            Literal[
                "message",
                "action",
                "event",
                "document",
                "identity",
                "linkedin_message",
                "deal",
                "organization",
                "contact",
            ],
            PropertyInfo(alias="automationObjectType"),
        ]
    ]
    """Object types that support triggered automations.

    Must match the triggered-automation whitelist in @micro/database migrate-sql
    (TRIGGERED_AUTOMATION_OBJECTS).
    """

    kind: Required[Literal["update", "lifecycle"]]

    name: Required[str]

    id: str

    actions: Iterable[Action]
    """
    Actions to run when the automation fires; each item has a `type` plus
    type-specific fields.
    """

    changeset: Changeset
    """
    A changeset filter group (update automations only): a combinator plus an array
    of transition clauses matching what is changing. Dot-paths (nested reference
    filters) are NOT permitted — direct properties only.
    """

    created_at: str

    enabled: bool

    list_id: Optional[str]

    on_create: bool
    """Lifecycle automations only."""

    on_delete: bool
    """Lifecycle automations only."""

    state: State
    """A filter group: a combinator plus an array of slug-based clauses.

    Dot-paths (e.g. `organization.location`) express nested reference filters.
    """

    body_team_id: Annotated[Optional[str], PropertyInfo(alias="team_id")]

    updated_at: Optional[str]

    user_id: Optional[str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Action(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """An action the automation runs when it fires.

    `type` selects the kind; the remaining fields are type-specific (`agent` → `agent_id`, `webhook` → `webhook_id`, `email`/`linkedin` → the send-as user, template, and recipient-view fields). Generic: new action types add fields here.
    """

    type: Required[Literal["agent", "webhook", "wait", "email", "linkedin"]]

    agent_id: Optional[str]
    """Required when `type` is `agent`. The agent to run."""

    cron_expression: Optional[str]
    """wait: cron schedule for the resume time.

    Exactly one of delay_seconds or cron_expression.
    """

    delay_seconds: Optional[int]
    """wait: relative delay in seconds.

    Exactly one of delay_seconds or cron_expression.
    """

    recipient_email_prop_def_id: Optional[str]
    """Required when `type` is `email`.

    The property (on the recipient view object) holding the recipient email address.
    """

    recipient_provider_prop_def_id: Optional[str]
    """Required when `type` is `linkedin`.

    The property (on the recipient view object) holding the recipient LinkedIn
    provider id.
    """

    recipient_view_id: Optional[str]
    """Required when `type` is `email` or `linkedin`.

    The saved prism view resolved at send time to the recipient audience (its filter
    re-runs each step, so responders drop out of later drip sends).
    """

    recipient_view_object_type: Optional[str]
    """Required when `type` is `email` or `linkedin`.

    Must be `contact` — the recipient audience is a contact view (contacts carry the
    direct email / linkedin provider property).
    """

    send_as_user_id: Optional[str]
    """Required when `type` is `email` or `linkedin`.

    The user (external id) the message is sent as.
    """

    subject: Optional[str]
    """Required when `type` is `email`.

    The subject line; rendered as a Liquid template per recipient.
    """

    template_id: Optional[str]
    """Required when `type` is `email` or `linkedin`.

    The email-template document whose body is rendered (Liquid) per recipient.
    """

    timezone: Optional[str]
    """wait: IANA timezone for evaluating cron_expression (optional)."""

    webhook_id: Optional[str]
    """Required when `type` is `webhook`.

    The id of the webhook the event is dispatched to (async) when the automation
    fires.
    """


class Changeset(TypedDict, total=False):
    """
    A changeset filter group (update automations only): a combinator plus an array of transition clauses matching what is changing. Dot-paths (nested reference filters) are NOT permitted — direct properties only.
    """

    combinator: Literal["AND", "OR"]

    filter: Iterable[Dict[str, object]]
    """
    Each entry is a transition clause { slug: { from?: { comparator: value }, to?: {
    comparator: value } } }. `from` matches the prior value, `to` the new value; an
    empty body { slug: {} } matches any change to that property.
    """


class State(TypedDict, total=False):
    """A filter group: a combinator plus an array of slug-based clauses.

    Dot-paths (e.g. `organization.location`) express nested reference filters.
    """

    combinator: Literal["AND", "OR"]

    filter: Iterable[Dict[str, object]]
    """Each entry is { slug: { comparator: value } }"""
