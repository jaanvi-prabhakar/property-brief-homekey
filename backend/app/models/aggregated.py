from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional, Literal

T = TypeVar("T")


# Confidence annotations for each field
FieldConfidence = Literal["high", "medium", "low"]


class AggregatedField(BaseModel, Generic[T]):
    value: Optional[T]
    confidence: FieldConfidence
    sources: List[str]
    conflicts: Optional[List[str]] = None


class PropertyBrief(BaseModel):
    id: str
    address: AggregatedField[str]
    beds: AggregatedField[int]
    baths: AggregatedField[int]
    sqft: AggregatedField[int]
    year_built: AggregatedField[int]
    price: AggregatedField[int]
    description: AggregatedField[str]
    notes: AggregatedField[str]
