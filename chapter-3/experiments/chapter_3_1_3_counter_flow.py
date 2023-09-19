from metaflow import FlowSpec, step


class CounterFlow(FlowSpec):
    @step
    def start(self):
        """Starting point."""
        self.count = 0
        self.next(self.add)

    @step
    def add(self):
        """Increment by 1."""
        print(f"The count is {self.count} before incrementing.")
        self.count += 1
        self.next(self.end)

    @step
    def end(self):
        """Finish line."""
        self.count += 1
        print(f"The final count is {self.count}.")


if __name__ == "__main__":
    CounterFlow()
