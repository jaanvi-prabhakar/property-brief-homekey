from app.services.aggregator import PropertyAggregator


class PropertyBriefAgent:
    def __init__(self):
        self.aggregator = PropertyAggregator()

    def run(self, property_id: str):
        raw = self.aggregator.collect_sources(property_id)
        return self.aggregator.aggregate(raw)
