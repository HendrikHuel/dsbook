from metaflow import FlowSpec, Parameter, JSONType, step


class JSONParameterFlow(FlowSpec):
    mapping = Parameter(
        "mapping",
        help="Specify a mapping.",
        default='{"some": "default"}',
        type=JSONType,
    )

    @step
    def start(self):
        """Print mapping."""
        for key, item in self.mapping.items():
            print(f"key: {key}, value: {item}")
        self.next(self.end)

    @step
    def end(self):
        """Finish line."""
        print("Done.")


if __name__ == "__main__":
    JSONParameterFlow()
