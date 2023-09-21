from metaflow import FlowSpec, step


class CounterBranchFlow(FlowSpec):
    @step
    def start(self):
        """Start of the DAG."""
        self.creature = "dog"
        self.count = 0

        self.next(self.add_one, self.add_two)

    @step
    def add_one(self):
        """Add one to count."""
        self.count += 1
        self.next(self.join)

    @step
    def add_two(self):
        """Add two to count."""
        self.count += 2
        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the results of the split."""
        self.count = max(inp.count for inp in inputs)

        print(f"count from add_one {inputs.add_one.count}.")
        print(f"count from add_two {inputs.add_two.count}.")

        self.creature = inputs[0].creature

        self.next(self.end)

    @step
    def end(self):
        """End of the workflow."""
        print(f"The creature is {self.creature}.")
        print(f"The final count is {self.count}.")


if __name__ == "__main__":
    CounterBranchFlow()
