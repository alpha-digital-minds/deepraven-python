# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["ConversationListResponse", "ConversationListResponseItem", "ConversationListResponseItemMessage"]


class ConversationListResponseItemMessage(BaseModel):
    content: str

    role: str


class ConversationListResponseItem(BaseModel):
    messages: List[ConversationListResponseItemMessage]

    metadata: Optional[Dict[str, object]] = None

    processed: Optional[bool] = None

    timestamp: Optional[str] = None


ConversationListResponse: TypeAlias = List[ConversationListResponseItem]
