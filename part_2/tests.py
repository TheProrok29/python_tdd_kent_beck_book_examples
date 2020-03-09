class WasRun:
    def __init__(self, name: str):
        self.wasRun = None

    def test_method(self) -> None:
        self.wasRun = 1

    def run(self) -> None:
        self.test_method()


test = WasRun('test_method')
print(test.wasRun)
test.run()
print(test.wasRun)
