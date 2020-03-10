class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def test_started(self):
        self.runCount += 1

    def test_failed(self):
        self.errorCount += 1

    def summary(self):
        return f'{self.runCount} run, {self.errorCount} failed'


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name: str):
        self.name = name

    def set_up(self) -> None:
        pass

    def run(self, result) -> TestResult:
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
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

    def test_broken_method(self):
        raise Exception


class TestCaseTest(TestCase):
    def set_up(self) -> None:
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert ('set_up test_method tear_down ' == test.log)

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert ('1 run, 0 failed' == self.result.summary())

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert ('1 run, 1 failed' == self.result.summary())

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert ('1 run, 1 failed' == self.result.summary())

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        assert ('2 run, 1 failed' == self.result.summary())


suite = TestSuite()
suite.add(TestCaseTest("test_template_method"))
suite.add(TestCaseTest("test_result"))
suite.add(TestCaseTest("test_failed_result"))
suite.add(TestCaseTest("test_failed_result_formatting"))
suite.add(TestCaseTest("test_suite"))
result = TestResult()
suite.run(result)
print(result.summary())
