import unittest

from factory import PointFactory
from singleton import Database


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        d1 = Database()
        d2 = Database()
        self.assertEqual(d1, d2)


class FactoryTest(unittest.TestCase):
    def test_cartesian_point(self):
        point = PointFactory.new_cartesian_point(5, 5)
        expected = 'x: 5, y: 5'
        self.assertEqual(str(point), expected)

    def test_polar_point(self):
        point = PointFactory.new_polar_point(5, 5)
        expected = 'x: -4.794621373315692, y: 1.4183109273161312'
        self.assertEqual(str(point), expected)
