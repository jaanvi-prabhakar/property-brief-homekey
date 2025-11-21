from fastapi import FastAPI, HTTPException
from app.services.agent import PropertyBriefAgent
from app.services.datasources import load_json

app = FastAPI(title="Property Brief Aggregation API")

agent = PropertyBriefAgent()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/properties")
def list_properties():
    """
    Returns a list of property IDs + basic labels from the mock datasets.
    This makes it easy for the frontend/UI to list available homes.
    """
    public_records = load_json("public_records.json")

    # Return a simple array: [{ id: "p1", address: "123 Maple St" }]
    properties = []
    for pid, record in public_records.items():
        properties.append({
            "id": pid,
            "address": record.get("address")
        })

    return {"properties": properties}


@app.get("/properties/{property_id}/brief")
def get_property_brief(property_id: str):
    """
    Returns the unified PropertyBrief for a given property ID.
    Includes: merged fields, confidence scores, sources, conflicts.
    """
    result = agent.run(property_id)

    if not result:
        raise HTTPException(status_code=404, detail="Property not found")

    return result
