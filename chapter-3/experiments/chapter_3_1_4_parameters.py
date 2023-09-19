from metaflow import FlowSpec, Parameter, step


class ParameterFLow(FlowSpec):
    animal = Parameter("creature", help="Specify an animal.", required=True)
    count = Parameter("count", help="Number of animals.", default=1, type=int)
    ratio = Parameter("ratio", help="Ratio between 0.0 and 1.0", type=float)

    @step
    def start(self):
        """Print input parameters."""
        print(f"{self.animal} is a string of {len(self.animal)} characters.")
        print(f"Count is an integer: {self.count + 1} = {self.count + 1}.")
        print(f"Ratio is a {type(self.ratio)} whose value is {self.ratio}.")
        self.next(self.end)

    @step
    def end(self):
        """Finish flow."""
        print("Done!")


if __name__ == "__main__":
    ParameterFLow()
