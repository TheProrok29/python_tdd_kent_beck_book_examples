class TestCase:
    pass


class WasRun(TestCase):
    def __init__(self, name: str):
        self.wasRun = None
        self.name = name

    def test_method(self) -> None:
        self.wasRun = 1

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


test = WasRun('test_method')
print(test.wasRun)
test.run()
print(test.wasRun)
