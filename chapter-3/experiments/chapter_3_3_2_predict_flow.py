from metaflow import FlowSpec, step, Flow, Parameter, JSONType


class ClassifierPredictFlow(FlowSpec):
    vector = Parameter("vector", type=JSONType, required=True)

    @step
    def start(self):
        """Parse results from train step."""
        run = Flow("ClassifierTrainFlow").latest_run
        self.train_run_id = run.pathspec
        self.model = run["end"].task.data.model

        print(f"Input vector {self.vector}")

        self.next(self.end)

    @step
    def end(self):
        """Use model to do stuff."""
        print(f"Model: {self.model}")


if __name__ == "__main__":
    ClassifierPredictFlow()
