# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    team_id: Annotated[str, PropertyInfo(alias="teamId")]

    default: Dict[str, object]
    """Properties keyed by property slug.

    Values can be strings, numbers, booleans, arrays, or null. For
    select/multiselect properties, values may be option slugs or option UUIDs on
    write; option slugs are returned on read. Identity email_addresses accepts
    contact UUIDs or email strings on create/update. Emails use Micro normalization
    and resolve to contact links within the write transaction; creating an identity
    does not merge other identities. Arrays replace links; {\\__op: 'append'|'remove',
    values: [...]} changes only the specified links. Removing an email never creates
    a contact. Identity companies contains organization UUIDs, whose read access is
    checked when adding links.
    """

    list: object

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
