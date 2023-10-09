from metaflow import FlowSpec, step, resources

LENGTH = 10_000


class LongStringFlow(FlowSpec):
    @resources(memory=10_000)
    @step
    def start(self):
        """Generate long string. To simulate high RAM consumption for the current step."""
        long_string = b"x" * LENGTH
        print("A lot of momory is consumed.")
        self.next(self.end)

    @step
    def end(self):
        """End of the flow."""
        print("Done!")


if __name__ == "__main__":
    LongStringFlow()
