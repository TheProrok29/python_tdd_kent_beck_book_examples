class WasRun:
    def __init__(self, name: str):
        self.wasRun = None

    def test_method(self) -> None:
        self.wasRun = 1


test = WasRun('test_method')
print(test.wasRun)
test.test_method()
print(test.wasRun)
