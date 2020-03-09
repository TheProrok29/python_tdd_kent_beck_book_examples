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


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun('test_method')
        assert (not test.wasRun)
        test.run()
        assert (test.wasRun)

    def test_set_up(self):
        test = WasRun('test_method')
        test.run()
        assert (test.was_set_up)


TestCaseTest('test_running').run()
TestCaseTest('test_set_up').run()
