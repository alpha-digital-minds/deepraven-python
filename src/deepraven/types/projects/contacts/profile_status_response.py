# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ProfileStatusResponse"]


class ProfileStatusResponse(BaseModel):
    contact_id: str

    status: str
