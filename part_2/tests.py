class TestResult:
    def __init__(self):
        self.runCount = 0

    def test_started(self):
        self.runCount += 1

    def summary(self):
        return f'{self.runCount} run, 0 failed'


class TestCase:
    def __init__(self, name: str):
        self.name = name

    def set_up(self) -> None:
        pass

    def run(self) -> TestResult:
        result = TestResult()
        result.test_started()
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return result

    def tear_down(self):
        pass


class WasRun(TestCase):
    def __init__(self, name: str):
        self.wasRun = None
        TestCase.__init__(self, name)

    def set_up(self) -> None:
        self.wasRun = None
        self.log = 'set_up '

    def test_method(self) -> None:
        self.wasRun = 1
        self.log = self.log + 'test_method '

    def tear_down(self) -> None:
        self.log = self.log + 'tear_down '


class TestCaseTest(TestCase):

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert ('set_up test_method tear_down ' == test.log)

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert ('1 run, 0 failed' == result.summary())

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert ('1 run, 1 failed' == result.summary())


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
