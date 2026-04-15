# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["ProfileExtractSyncResponse", "Personal", "Preferences", "Relationship", "Relative", "Sales"]


class Personal(BaseModel):
    company: Optional[str] = None

    delivery_address: Optional[str] = None

    gender: Optional[str] = None

    location: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None

    role: Optional[str] = None


class Preferences(BaseModel):
    best_contact_channel: Optional[str] = None

    communication_style: Optional[str] = None

    languages: Optional[List[str]] = None


class Relationship(BaseModel):
    last_contact_date: Optional[str] = None

    personal_details: Optional[List[str]] = None

    status: Optional[str] = None


class Relative(BaseModel):
    age: Optional[str] = None

    gender: Optional[str] = None

    name: Optional[str] = None

    notes: Optional[str] = None

    preferences: Optional[List[str]] = None

    relation: Optional[str] = None

    sizes: Optional[Dict[str, str]] = None


class Sales(BaseModel):
    budget_range: Optional[str] = None

    buying_persona: Optional[str] = None

    buying_triggers: Optional[List[str]] = None

    current_needs: Optional[List[str]] = None

    objections_raised: Optional[List[str]] = None

    pain_points: Optional[List[str]] = None

    purchase_history: Optional[List[str]] = None


class ProfileExtractSyncResponse(BaseModel):
    user_id: str

    created_at: Optional[str] = None

    personal: Optional[Personal] = None

    preferences: Optional[Preferences] = None

    relationship: Optional[Relationship] = None

    relatives: Optional[List[Relative]] = None

    sales: Optional[Sales] = None

    updated_at: Optional[str] = None
