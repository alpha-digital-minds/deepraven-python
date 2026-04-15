# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConversationCreateParams", "Message"]


class ConversationCreateParams(TypedDict, total=False):
    project_id: Required[str]

    messages: Required[Iterable[Message]]

    metadata: Optional[Dict[str, object]]


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]
