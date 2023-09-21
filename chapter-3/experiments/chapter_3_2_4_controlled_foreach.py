from metaflow import FlowSpec, step


class ControlledForEach(FlowSpec):
    @step
    def start(self):
        """Start of the DAG."""
        self.ints = list(range(1000))
        self.next(self.multiply, foreach="ints")

    @step
    def multiply(self):
        """Multiply input by 1_000."""
        self.result = self.input * 1_000
        self.next(self.join)

    @step
    def join(self, inputs):
        """Sum multiplied numbers."""
        self.total = sum(inp.result for inp in inputs)
        self.next(self.end)

    @step
    def end(self):
        """The end of the DAG."""
        print(f"The total is {self.total}.")


if __name__ == "__main__":
    ControlledForEach()

    # python chapter_3_2_4_controlled_foreach.py run
    # python chapter_3_2_4_controlled_foreach.py run --max-num-splits 1000 --max-workers=16
    # python chapter_3_2_4_controlled_foreach.py run --max-num-splits 1000 --max-workers=2
