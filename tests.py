import math
import unittest
import rectangle
import square
import triangle
import circle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(1000000, 1000000), 1000000000000)
        self.assertEqual(rectangle.area(0, 500), 0)
        self.assertEqual(rectangle.area(1000000000, 1), 1000000000)
        self.assertEqual(rectangle.area(0.5, 0.2), 0.1)
        self.assertEqual(rectangle.area(7, 8), 56)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(1000000, 1000000), 4000000)
        self.assertEqual(rectangle.perimeter(0, 500), 1000)
        self.assertEqual(rectangle.perimeter(1000000000, 1), 2000000002)
        self.assertEqual(rectangle.perimeter(0.5, 0.2), 1.4)
        self.assertEqual(rectangle.perimeter(8, 5), 26)

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle.area(1000000), 1000000000000 * math.pi)
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.area(0.1), 0.01 * math.pi)
        self.assertEqual(circle.area(4), 16 * math.pi)
        self.assertEqual(circle.area(0.25), 0.0625 * math.pi)

    def test_perimeter(self):
        self.assertEqual(circle.perimeter(1000000), 2000000 * math.pi)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(circle.perimeter(0.1), 0.2 * math.pi)
        self.assertEqual(circle.perimeter(4), 8 * math.pi)
        self.assertEqual(circle.perimeter(0.25), 0.5 * math.pi)

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(1000000), 1000000000000)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(0.5), 0.25)
        self.assertEqual(square.area(6), 36)
        self.assertEqual(square.area(0.25), 0.0625)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(1000000), 4000000)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(0.1), 0.4)
        self.assertEqual(square.perimeter(8), 32)
        self.assertEqual(square.perimeter(0.25), 1)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(1000000, 500000), 250000000000)
        self.assertEqual(triangle.area(0, 10), 0)
        self.assertEqual(triangle.area(1000000, 1), 500000)
        self.assertEqual(triangle.area(0.1, 0.5), 0.025)
        self.assertEqual(triangle.area(10, 5), 25)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(1000000, 1000000, 1000000), 3000000)
        self.assertEqual(triangle.perimeter(0, 5, 5), 10)
        self.assertEqual(triangle.perimeter(500000, 0.4, 0.6), 500001)
        self.assertEqual(triangle.perimeter(0.1, 0.25, 0.25), 0.6)
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

