# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ConversationCreateResponse"]


class ConversationCreateResponse(BaseModel):
    contact_id: str

    conversations_added: int

    profile_update: str

    project_id: str
