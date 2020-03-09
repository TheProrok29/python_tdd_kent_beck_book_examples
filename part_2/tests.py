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
        self.log = self.log + 'test_method '

    def set_up(self) -> None:
        self.wasRun = None
        self.log = 'set_up '


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert ('set_up test_method ' == test.log)


TestCaseTest('test_template_method').run()
