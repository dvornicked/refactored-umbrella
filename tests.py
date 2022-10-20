import unittest
from unittest.mock import patch, call

from decorator import Circle, Square, ColoredShape
from factory import PointFactory
from observer import Observable, Observer
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


class ObserverTest(unittest.TestCase):
    @patch('builtins.print')
    def test_broadcast(self, mock_print):
        subject = Observable('Subject 1')

        observer1 = Observer('Observer 1', subject)
        observer2 = Observer('Observer 2', subject)

        subject.notify_observers('Broadcast 1')
        subject.unsubscribe(observer2)
        subject.notify_observers('Broadcast 2')

        self.assertEqual(mock_print.mock_calls, [call('Observer 1 got Broadcast 1 from Subject 1'),
                                                 call('Observer 2 got Broadcast 1 from Subject 1'),
                                                 call('Observer 1 got Broadcast 2 from Subject 1')])
