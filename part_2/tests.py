class TestCase:
    def __init__(self, name: str):
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str):
        self.wasRun = None
        TestCase.__init__(self, name)

    def test_method(self) -> None:
        self.wasRun = 1


test = WasRun('test_method')
print(test.wasRun)
test.run()
print(test.wasRun)
