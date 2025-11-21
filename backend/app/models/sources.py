from pydantic import BaseModel
from typing import Optional, List


class PublicRecordsProperty(BaseModel):
    id: str
    address: Optional[str] = None
    beds: Optional[int] = None
    baths: Optional[int] = None
    sqft: Optional[int] = None
    year_built: Optional[int] = None


class ListingProperty(BaseModel):
    id: str
    address: Optional[str] = None
    beds: Optional[int] = None
    baths: Optional[int] = None
    sqft: Optional[int] = None
    price: Optional[int] = None
    description: Optional[str] = None


class UserNotesProperty(BaseModel):
    id: str
    notes: Optional[str] = None
    flags: Optional[List[str]] = None
