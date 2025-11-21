import { useEffect, useState } from "react";
import { getProperties } from "../api/property";
import type { PropertyListItem } from "../types/property";

export default function PropertyList() {
  const [properties, setProperties] = useState<PropertyListItem[]>([]);

  useEffect(() => {
    getProperties().then((data) => setProperties(data.properties));
  }, []);

  return (
    <div>
      <h1>Properties</h1>
      <ul>
        {properties.map((p) => (
          <li key={p.id}>
            <a href={`/properties/${p.id}`}>{p.address}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}
