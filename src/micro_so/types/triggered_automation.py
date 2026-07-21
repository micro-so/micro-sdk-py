# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TriggeredAutomation", "Action", "Changeset", "State"]


class Action(BaseModel):
    """An action the automation runs when it fires.

    `type` selects the kind; the remaining fields are type-specific (`agent` → `agent_id`, `webhook` → `webhook_id`, `email`/`linkedin` → the send-as user, template, and recipient-view fields). Generic: new action types add fields here.
    """

    type: Literal["agent", "webhook", "wait", "email", "linkedin"]

    agent_id: Optional[str] = None
    """Required when `type` is `agent`. The agent to run."""

    cron_expression: Optional[str] = None
    """wait: cron schedule for the resume time.

    Exactly one of delay_seconds or cron_expression.
    """

    delay_seconds: Optional[int] = None
    """wait: relative delay in seconds.

    Exactly one of delay_seconds or cron_expression.
    """

    recipient_email_prop_def_id: Optional[str] = None
    """Required when `type` is `email`.

    The property (on the recipient view object) holding the recipient email address.
    """

    recipient_provider_prop_def_id: Optional[str] = None
    """Required when `type` is `linkedin`.

    The property (on the recipient view object) holding the recipient LinkedIn
    provider id.
    """

    recipient_view_id: Optional[str] = None
    """Required when `type` is `email` or `linkedin`.

    The saved prism view resolved at send time to the recipient audience (its filter
    re-runs each step, so responders drop out of later drip sends).
    """

    recipient_view_object_type: Optional[str] = None
    """Required when `type` is `email` or `linkedin`.

    Must be `contact` — the recipient audience is a contact view (contacts carry the
    direct email / linkedin provider property).
    """

    send_as_user_id: Optional[str] = None
    """Required when `type` is `email` or `linkedin`.

    The user (external id) the message is sent as.
    """

    subject: Optional[str] = None
    """Required when `type` is `email`.

    The subject line; rendered as a Liquid template per recipient.
    """

    template_id: Optional[str] = None
    """Required when `type` is `email` or `linkedin`.

    The email-template document whose body is rendered (Liquid) per recipient.
    """

    timezone: Optional[str] = None
    """wait: IANA timezone for evaluating cron_expression (optional)."""

    webhook_id: Optional[str] = None
    """Required when `type` is `webhook`.

    The id of the webhook the event is dispatched to (async) when the automation
    fires.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Changeset(BaseModel):
    """
    A changeset filter group (update automations only): a combinator plus an array of transition clauses matching what is changing. Dot-paths (nested reference filters) are NOT permitted — direct properties only.
    """

    combinator: Optional[Literal["AND", "OR"]] = None

    filter: Optional[List[Dict[str, object]]] = None
    """
    Each entry is a transition clause { slug: { from?: { comparator: value }, to?: {
    comparator: value } } }. `from` matches the prior value, `to` the new value; an
    empty body { slug: {} } matches any change to that property.
    """


class State(BaseModel):
    """A filter group: a combinator plus an array of slug-based clauses.

    Dot-paths (e.g. `organization.location`) express nested reference filters.
    """

    combinator: Optional[Literal["AND", "OR"]] = None

    filter: Optional[List[Dict[str, object]]] = None
    """Each entry is { slug: { comparator: value } }"""


class TriggeredAutomation(BaseModel):
    """A triggered automation.

    `kind` selects the shape: `update` fires on object updates and requires a `changeset` (from/to transition) filter plus an optional `state` precondition; `lifecycle` fires on create and/or delete (`on_create`/`on_delete`) and requires a `state` filter (no changeset). `state` permits dot-paths (nested reference filters); `changeset` is direct properties only. Object type is taken from the path.
    """

    kind: Literal["update", "lifecycle"]

    name: str

    id: Optional[str] = None

    actions: Optional[List[Action]] = None
    """
    Actions to run when the automation fires; each item has a `type` plus
    type-specific fields.
    """

    changeset: Optional[Changeset] = None
    """
    A changeset filter group (update automations only): a combinator plus an array
    of transition clauses matching what is changing. Dot-paths (nested reference
    filters) are NOT permitted — direct properties only.
    """

    created_at: Optional[str] = None

    enabled: Optional[bool] = None

    list_id: Optional[str] = None

    on_create: Optional[bool] = None
    """Lifecycle automations only."""

    on_delete: Optional[bool] = None
    """Lifecycle automations only."""

    state: Optional[State] = None
    """A filter group: a combinator plus an array of slug-based clauses.

    Dot-paths (e.g. `organization.location`) express nested reference filters.
    """

    team_id: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None
