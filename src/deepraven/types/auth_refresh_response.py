# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthRefreshResponse"]


class AuthRefreshResponse(BaseModel):
    access_token: str

    expires_in: Optional[int] = None

    refresh_token: Optional[str] = None

    token_type: Optional[str] = None
