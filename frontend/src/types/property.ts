export interface AggregatedField<T> {
    value: T | null;
    confidence: "high" | "medium" | "low";
    sources: string[];
    conflicts?: string[] | null;
  }
  
  export interface PropertyBrief {
    id: string;
    address: AggregatedField<string>;
    beds: AggregatedField<number>;
    baths: AggregatedField<number>;
    sqft: AggregatedField<number>;
    year_built: AggregatedField<number>;
    price: AggregatedField<number>;
    description: AggregatedField<string>;
    notes: AggregatedField<string>;
  }
  
  export interface PropertyListItem {
    id: string;
    address: string;
  }
  