# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["PrismObjectPropertiesParam"]


class PrismObjectPropertiesParam(TypedDict, total=False):
    default: Dict[str, object]
    """Properties keyed by property slug.

    Values can be strings, numbers, booleans, arrays, or null. For
    select/multiselect properties, values may be option slugs or option UUIDs on
    write; option slugs are returned on read.
    """

    list: object
