import unittest
from divisible import divisible


class TestDivisible(unittest.TestCase):

    def test_divisible(self):

        self.assertTrue(divisible(20, 10))
        self.assertFalse(divisible(2, 3))


if __name__ == '__main__':
    unittest.main()
