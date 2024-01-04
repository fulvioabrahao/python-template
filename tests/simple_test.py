# very simple test
import unittest


class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)

    def test2(self):
        self.assertEqual(2, 2)
