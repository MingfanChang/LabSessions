import unittest


def fun(x):
    return None if x is None else x + 1


class MyTest(unittest.TestCase):

    # Tests are methods that start with "test", when you do unittest.main()
    # these methods will run.

    def test1(self):
        self.assertEqual(fun(None), None)

    def test2(self):
        self.assertEqual(fun(3), 4)

    # The following aren't tests and these methods will not run unless
    # explicitly called from one of the test methods.

    def no_test(self):
        self.assertEqual(True, False)

    def t(self):
        self.assertEqual(True, False)



if __name__ == '__main__':

    unittest.main()
