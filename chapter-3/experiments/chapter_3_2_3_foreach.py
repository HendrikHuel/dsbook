from metaflow import FlowSpec, step


class ForeEachFlow(FlowSpec):
    @step
    def start(self):
        """Start of the DAG."""
        self.creatures = ["dog", "bird", "horse"]
        self.next(self.analyze_creatures, foreach="creatures")

    @step
    def analyze_creatures(self):
        """Analyze creatures."""
        print(f"Analyzing {self.input} ...")
        self.creature = self.input
        self.score = len(self.creature)
        self.next(self.join)

    @step
    def join(self, inputs):
        """Find best creatrue."""
        self.best = max(inputs, key=lambda x: x.score).creature
        self.merge_artifacts(inputs, include=["creatures"])
        self.next(self.end)

    @step
    def end(self):
        """The end of the DAG."""
        print(f"Creatures in the race {self.creatures}")
        print(f"{self.best} won!")


if __name__ == "__main__":
    ForeEachFlow()
