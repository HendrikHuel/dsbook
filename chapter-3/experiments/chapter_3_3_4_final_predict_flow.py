from metaflow import FlowSpec, step, Flow, Parameter, JSONType


class FullClassifierPredictFlow(FlowSpec):
    vector = Parameter("vector", type=JSONType, default='[14, 2, 3, 20, 120, 3, 3, 0.3, 2, 6, 1, 3, 1280]')

    @step
    def start(self):
        """Parse results from train step."""
        run = Flow("FullClassifierTrainFlow").latest_run
        self.train_run_id = run.pathspec
        self.model = run["end"].task.data.model

        print(f"Input vector {self.vector}")

        self.next(self.end)

    @step
    def end(self):
        """Use model to do stuff."""
        self.prediction = self.model.predict([self.vector])
        print(f"Model: {self.model}")
        print(f"Predicted classes: {self.prediction[0]}")


if __name__ == "__main__":
    FullClassifierPredictFlow()
    # python chapter_3_3_4_final_predict_flow.py run --vector '[14.3, 1.92, 2.72, 20.0, 120.0, 2.8, 3.14, 0.33, 1.97, 6.2, 1.07, 2.65, 1280.0]'
