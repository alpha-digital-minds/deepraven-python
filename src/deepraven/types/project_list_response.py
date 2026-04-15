# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ProjectListResponse", "ProjectListResponseItem"]


class ProjectListResponseItem(BaseModel):
    id: str

    account_id: str

    created_at: str

    name: str

    updated_at: str

    description: Optional[str] = None


ProjectListResponse: TypeAlias = List[ProjectListResponseItem]
