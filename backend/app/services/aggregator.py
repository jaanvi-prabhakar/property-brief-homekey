'''
A field aggregator (for strings + numbers)
A PropertyAggregator class that: loads raw data from the source loaders, merges the values, outputs a PropertyBrief
A priority order for conflicts
Confidence scoring rules
'''

from typing import List, Optional, Tuple
from app.models.aggregated import AggregatedField, PropertyBrief
from app.models.sources import PublicRecordsProperty, ListingProperty, UserNotesProperty
from app.services.datasources import get_public_records, get_listing_data, get_user_notes
from app.services.datasources import (
    get_public_records,
    get_listing_data,
    get_user_notes
)
from app.models.aggregated import PropertyBrief

SOURCE_PRIORITY = ["public_records", "listing", "user_notes"]

def aggregate_numeric_field(values: List[Tuple[str, Optional[int]]]) -> AggregatedField[int]:
    present = [(src, v) for src, v in values if v is not None]

    if not present:
        return AggregatedField(value=None, confidence="low", sources=[])

    distinct = {v for _, v in present}
    sources = [src for src, _ in present]

    # All values same
    if len(distinct) == 1:
        return AggregatedField(value=present[0][1], confidence="high", sources=sources)

    # Conflict
    chosen_source = next(src for src in SOURCE_PRIORITY if src in sources)
    chosen_value = next(v for src, v in present if src == chosen_source)
    conflicts = [f"{src}={v}" for src, v in present]

    return AggregatedField(
        value=chosen_value,
        confidence="low",
        sources=sources,
        conflicts=conflicts
    )

def aggregate_string_field(values: List[Tuple[str, Optional[str]]]) -> AggregatedField[str]:
    present = [(src, v) for src, v in values if v]

    if not present:
        return AggregatedField(value=None, confidence="low", sources=[])

    distinct = {v for _, v in present}
    sources = [src for src, _ in present]

    # All values same
    if len(distinct) == 1:
        return AggregatedField(value=present[0][1], confidence="high", sources=sources)

    # Conflict
    chosen_source = next(src for src in SOURCE_PRIORITY if src in sources)
    chosen_value = next(v for src, v in present if src == chosen_source)
    conflicts = [f"{src}='{v}'" for src, v in present]

    return AggregatedField(
        value=chosen_value,
        confidence="low",
        sources=sources,
        conflicts=conflicts
    )

class PropertyAggregator:

    def collect_sources(self, property_id: str):
        return {
            "public_records": get_public_records(property_id),
            "listing": get_listing_data(property_id),
            "user_notes": get_user_notes(property_id)
        }

    def aggregate(self, raw):
        pr = raw["public_records"]
        lt = raw["listing"]
        un = raw["user_notes"]

        return PropertyBrief(
            id=raw["public_records"].id if pr else raw["listing"].id,

            address=aggregate_string_field([
                ("public_records", pr.address if pr else None),
                ("listing", lt.address if lt else None),
                ("user_notes", None),
            ]),

            beds=aggregate_numeric_field([
                ("public_records", pr.beds if pr else None),
                ("listing", lt.beds if lt else None),
                ("user_notes", None),
            ]),

            baths=aggregate_numeric_field([
                ("public_records", pr.baths if pr else None),
                ("listing", lt.baths if lt else None),
                ("user_notes", None),
            ]),

            sqft=aggregate_numeric_field([
                ("public_records", pr.sqft if pr else None),
                ("listing", lt.sqft if lt else None),
                ("user_notes", None),
            ]),

            year_built=aggregate_numeric_field([
                ("public_records", pr.year_built if pr else None),
                ("listing", None),
                ("user_notes", None),
            ]),

            price=aggregate_numeric_field([
                ("public_records", None),
                ("listing", lt.price if lt else None),
                ("user_notes", None),
            ]),

            description=aggregate_string_field([
                ("public_records", None),
                ("listing", lt.description if lt else None),
                ("user_notes", None),
            ]),

            notes=aggregate_string_field([
                ("public_records", None),
                ("listing", None),
                ("user_notes", un.notes if un else None),
            ])
        )
