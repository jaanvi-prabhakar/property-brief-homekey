# Property Brief Aggregation System

This repository implements a backend-focused feature that generates a **unified, reliable property brief** from fragmented and inconsistent real-estate data. The project demonstrates clear data modeling, conflict resolution logic, confidence scoring, and a production-inspired service layout.

## Overview

Real-estate information often comes from multiple sources — public records, listing portals, and human notes, each containing different or incomplete fields.  
This system:

- Loads raw data from multiple sources
- Normalizes and merges attributes
- Resolves conflicts using a deterministic priority order
- Assigns confidence levels to each merged field
- Outputs a structured, explainable `PropertyBrief` object

The result is a clean, trustworthy brief suitable for UI display or agentic AI workflows.

## Architecture

```
backend/
app/
main.py
models/
sources.py
aggregated.py
services/
datasources.py
aggregator.py
agent.py
data/
public_records.json
listings.json
user_notes.json
frontend/
README.md
```

**Key Components:**

- **Mock Data Sources** — Three JSON files representing public records, listing data, and user notes.
- **Source Models** — Typed Pydantic schemas for raw input.
- **Aggregated Models** — `AggregatedField` and `PropertyBrief`, including confidence and conflict metadata.
- **Data Loaders** — Utility functions for loading/validating data from JSON.
- **Aggregator** — Core logic that merges fields, resolves conflicts, and produces a unified brief.
- **Agent Wrapper** — Encapsulates workflow orchestration (`collect → aggregate`).

## Core Logic

The system defines a clear **trust priority**:

public_records > listing > user_notes

### Merging Rules

- **High Confidence** → All sources agree
- **Medium Confidence** → Only one source provides the value
- **Low Confidence** → Conflicting values across sources (resolved by priority)

Every `AggregatedField` includes:

- `value`
- `confidence`
- `sources` (which contributed)
- `conflicts` (only when disagreements exist)

This ensures full transparency and explainability.

## API Endpoints (Backend)

Planned primary endpoints:

- `GET /properties`  
  Returns list of available mock properties.

- `GET /properties/{id}/brief`  
  Returns the unified, confidence scored `PropertyBrief`.

- `GET /health`  
  Simple service availability check.

## Future Enhancements

- Integration with real MLS / municipal APIs
- Redis caching for faster response
- Async data pipelines
- AI summarization layers for human readable briefs
- Expanded data sources (permits, schools, flood risk, valuation history)
- Full React/TypeScript frontend consumption

## Summary

This project delivers a clean and modular implementation of a property data aggregation system.  
It emphasizes:

- Strong typing
- Deterministic conflict resolution
- Confidence scoring
- Clear data provenance
- Extensibility for future real-world use cases

The result is a robust backend foundation for generating reliable **Property Briefs** from multiple, inconsistent data inputs.
