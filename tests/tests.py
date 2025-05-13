import unittest
import math
from area_of_a_figure_lib.area_lib import Circle, Triangle, Area_of_a_figure, calculate_area

class TestAreas(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)
        
    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)
        
    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)
            
    def test_right_angled(self):
        self.assertTrue(Triangle(3, 4, 5).check_right_triangle())
        self.assertTrue(Triangle(5, 12, 13).check_right_triangle())
        self.assertFalse(Triangle(5, 5, 5).check_right_triangle())
        
    def test_calculate_area(self):
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [calculate_area(shape) for shape in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)
        
    def test_adding_new_shape(self):
        # Наследуем абстрактный класс Area_of_a_figure, определяем вычисление площади.
        class Square(Area_of_a_figure):
            def __init__(self, side):
                self.side = side
                
            def area(self):
                return self.side ** 2
                
        square = Square(4)
        self.assertAlmostEqual(calculate_area(square), 16.0)

if __name__ == '__main__':
    unittest.main()