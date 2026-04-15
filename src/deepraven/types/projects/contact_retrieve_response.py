# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContactRetrieveResponse"]


class ContactRetrieveResponse(BaseModel):
    id: str

    created_at: str

    external_id: str

    project_id: str
