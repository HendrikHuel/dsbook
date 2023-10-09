import os
from metaflow import FlowSpec, step

global_value = 5


class ProcessDemoFlow(FlowSpec):
    @step
    def start(self):
        """Print process id."""
        global global_value
        global_value = 9

        print(f"The process id is: {os.getpid()}")
        print(f"The global_value is: {global_value}")

        self.next(self.end)

    @step
    def end(self):
        """Check the global value and process id again."""
        # The PID changes. So metaflow uses different processes for each task. This is why the global_value in this step
        # is 5 instead of 9!
        print(f"The process id is: {os.getpid()}")
        print(f"The global_value is: {global_value}")


if __name__ == "__main__":
    ProcessDemoFlow()
