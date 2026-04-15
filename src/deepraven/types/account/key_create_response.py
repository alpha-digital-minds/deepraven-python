# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    id: str

    account_id: str

    created_at: str

    key: str

    name: str
