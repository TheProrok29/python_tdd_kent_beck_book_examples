class TestCase:
    def __init__(self, name: str):
        self.name = name

    def set_up(self) -> None:
        pass

    def run(self) -> None:
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str):
        self.wasRun = None
        TestCase.__init__(self, name)

    def test_method(self) -> None:
        self.wasRun = 1

    def set_up(self) -> None:
        self.wasRun = None
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun('test_method')
        assert (not test.wasRun)
        test.run()
        assert (test.wasRun)

    def test_set_up(self):
        test = WasRun('test_method')
        test.run()
        assert (test.wasSetUp)


TestCaseTest('test_running').run()
TestCaseTest('test_set_up').run()
