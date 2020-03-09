class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def test_method(self):
        pass


test = WasRun('test_method')
print(test.wasRun)
test.test_method()
print(test.wasRun)
