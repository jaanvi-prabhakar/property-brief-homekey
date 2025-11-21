import { useEffect, useState } from "react";
import { getPropertyBrief } from "../api/property";
import { useParams } from "react-router-dom";
import type { PropertyBrief } from "../types/property";

export default function PropertyDetail() {
  const { id } = useParams();
  const [brief, setBrief] = useState<PropertyBrief | null>(null);

  useEffect(() => {
    if (id) {
      getPropertyBrief(id).then((data) => setBrief(data));
    }
  }, [id]);

  if (!brief) return <div>Loading...</div>;

  return (
    <div>
      <h1>Property Brief - {brief.id}</h1>

      <h2>Address</h2>
      <p>
        {brief.address.value}
        <small>({brief.address.confidence} confidence)</small>
      </p>

      <h2>Details</h2>
      <ul>
        <li>
          Beds: {brief.beds.value} ({brief.beds.confidence})
        </li>
        <li>
          Baths: {brief.baths.value} ({brief.baths.confidence})
        </li>
        <li>
          Sqft: {brief.sqft.value} ({brief.sqft.confidence})
        </li>
        <li>
          Price: {brief.price.value} ({brief.price.confidence})
        </li>
      </ul>

      <h2>Description</h2>
      <p>{brief.description.value}</p>

      <h2>Notes</h2>
      <p>{brief.notes.value}</p>

      {brief.beds.conflicts && (
        <div style={{ color: "red" }}>
          <strong>Conflicts:</strong> {brief.beds.conflicts.join(", ")}
        </div>
      )}
    </div>
  );
}
