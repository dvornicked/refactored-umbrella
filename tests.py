import unittest

from decorator import Circle, Square, ColoredShape
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


class DecoratorTest(unittest.TestCase):
    def test_circle(self):
        circle = Circle(2)
        expected = 'A circle of radius 2'
        self.assertEqual(str(circle), expected)

    def test_square(self):
        square = Square(3)
        expected = 'A square with side 3'
        self.assertEqual(str(square), expected)

    def test_colored_circle(self):
        circle = Circle(2)
        colored_circle = ColoredShape(circle, 'Red')
        expected = 'A circle of radius 2 has the color Red'
        self.assertEqual(str(colored_circle), expected)

    def test_colored_square(self):
        square = Square(3)
        colored_square = ColoredShape(square, 'Red')
        expected = 'A square with side 3 has the color Red'
        self.assertEqual(str(colored_square), expected)
