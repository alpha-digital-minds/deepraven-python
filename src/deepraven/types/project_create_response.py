# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProjectCreateResponse"]


class ProjectCreateResponse(BaseModel):
    id: str

    account_id: str

    created_at: str

    name: str

    updated_at: str

    description: Optional[str] = None
