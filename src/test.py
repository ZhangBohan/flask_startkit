import unittest


class FlaskrTestCase(unittest.TestCase):

    def test_demo(self):
        assert 2 == (1+1)

if __name__ == '__main__':
    unittest.main()