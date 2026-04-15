# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["KeyListResponse", "KeyListResponseItem"]


class KeyListResponseItem(BaseModel):
    id: str

    created_at: str

    name: str

    project_id: str

    last_used_at: Optional[str] = None

    revoked_at: Optional[str] = None


KeyListResponse: TypeAlias = List[KeyListResponseItem]
