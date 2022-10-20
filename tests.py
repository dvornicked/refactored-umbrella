import unittest

from singleton import Database


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        d1 = Database()
        d2 = Database()
        self.assertEqual(d1, d2)

