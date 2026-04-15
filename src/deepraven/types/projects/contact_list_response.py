# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ContactListResponse", "ContactListResponseItem"]


class ContactListResponseItem(BaseModel):
    id: str

    company: str

    external_id: str

    name: str

    project_id: str

    total_conversations: int

    unprocessed_count: int


ContactListResponse: TypeAlias = List[ContactListResponseItem]
