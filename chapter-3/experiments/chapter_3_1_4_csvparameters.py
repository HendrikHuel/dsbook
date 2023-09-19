from metaflow import FlowSpec, Parameter, IncludeFile, step

from io import StringIO
import csv


class CSVFileFlow(FlowSpec):
    data = IncludeFile("csv", help="CSV file to be parsed.", is_text=True)
    delimiter = Parameter("delimiter", help="The delimiter of the csv.", default=";")

    @step
    def start(self):
        """Print file."""
        fileobj = StringIO(self.data)
        for i, row in enumerate(csv.reader(fileobj, delimiter=self.delimiter)):
            print(f"row {i}: {row}")
        self.next(self.end)

    @step
    def end(self):
        """The end of the flow."""
        print("Done!")


if __name__ == "__main__":
    CSVFileFlow()
