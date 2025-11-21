import json
from pathlib import Path
from typing import Optional

from app.models.sources import (
    PublicRecordsProperty,
    ListingProperty,
    UserNotesProperty
)

DATA_DIR = Path(__file__).parent.parent / "data"


def load_json(filename: str) -> dict:
    file_path = DATA_DIR / filename
    with open(file_path, "r") as f:
        return json.load(f)


def get_public_records(property_id: str) -> Optional[PublicRecordsProperty]:
    data = load_json("public_records.json")
    record = data.get(property_id)
    if record:
        return PublicRecordsProperty(**record)
    return None


def get_listing_data(property_id: str) -> Optional[ListingProperty]:
    data = load_json("listings.json")
    listing = data.get(property_id)
    if listing:
        return ListingProperty(**listing)
    return None


def get_user_notes(property_id: str) -> Optional[UserNotesProperty]:
    data = load_json("user_notes.json")
    notes = data.get(property_id)
    if notes:
        return UserNotesProperty(**notes)
    return None
