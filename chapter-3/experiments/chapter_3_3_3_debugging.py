from metaflow import FlowSpec, step


class FullClassifierTrainFlow(FlowSpec):
    @step
    def start(self):
        """Load the wine data."""
        from sklearn import datasets
        from sklearn.model_selection import train_test_split

        X, y = datasets.load_wine(return_X_y=True)
        (
            self.train_data,
            self.test_data,
            self.train_labels,
            self.test_labels,
        ) = train_test_split(X, y, test_size=0.2, random_state=0)
        print("Data loaded successfully!")
        self.next(self.train_knn, self.train_svm)

    @step
    def train_knn(self):
        """Train a nearest-neighbor classifier."""
        from sklearn.neighbors import KNeighborsClassifier

        self.model = KNeighborsClassifier()
        self.model.fit(self.train_data, self.train_labels)

        self.next(self.choose_model)

    @step
    def train_svm(self):
        """Train a svm classifier."""
        from sklearn import svm

        self.model = svm.SVC(kernel="poly")
        self.model.fit(self.train_data, self.train_labels)

        self.next(self.choose_model)

    @step
    def choose_model(self, inputs):
        """Choose the best performing model."""

        def score(inp):
            return inp.model, inp.model.score(inp.test_data, inp.test_labels)

        self.results = sorted(map(score, inputs), key=lambda x: -x[1])
        self.model = self.results[0][0]

        self.next(self.end)

    @step
    def end(self):
        """Give information about the performance of the models."""
        print("Scores")
        print("\n".join("%s %f" % res for res in self.results))
        print(f"Best model {self.model}")


if __name__ == "__main__":
    FullClassifierTrainFlow()
