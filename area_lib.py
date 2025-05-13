import math
from typing import Union
from abc import ABC, abstractmethod

class Area_of_a_figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @staticmethod
    def calculate_area(area: 'Area_of_a_figure') -> float:
        return area.area()

class Triangle(Area_of_a_figure):
    def __init__(self, side_of_a_triangle_a: float, side_of_a_triangle_b: float, side_of_a_triangle_c: float):
        if any(side <= 0 for side in (side_of_a_triangle_a, side_of_a_triangle_b, side_of_a_triangle_c)):
            raise ValueError("Ошибка: Все стороны должны иметь положительные значения.")
        
        # Теорема неравества треуг. гласит, что сторона треуг. должна быть меньше суммы двух других сторон.
        if not (side_of_a_triangle_a + side_of_a_triangle_b > side_of_a_triangle_c and 
                side_of_a_triangle_a + side_of_a_triangle_c > side_of_a_triangle_b and 
                side_of_a_triangle_b + side_of_a_triangle_c > side_of_a_triangle_a):
            raise ValueError("Ошибка: Сторона треугольника должна быть меньше суммы двух его других сторон.")
        
        self.side_of_a_triangle_a = side_of_a_triangle_a
        self.side_of_a_triangle_b = side_of_a_triangle_b
        self.side_of_a_triangle_c = side_of_a_triangle_c

    def area(self) -> float:
        # Формула Герона (вычисление площади по 3-м сторонам).
        s = (self.side_of_a_triangle_a + self.side_of_a_triangle_b + self.side_of_a_triangle_c) / 2
        return math.sqrt(s * (s - self.side_of_a_triangle_a) * (s - self.side_of_a_triangle_b) * (s - self.side_of_a_triangle_c))

    def check_right_triangle(self, tolerance: float = 1e-6) -> bool:
        sides = sorted([self.side_of_a_triangle_a, self.side_of_a_triangle_b, self.side_of_a_triangle_c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance
    
class Circle(Area_of_a_figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Ошибка: Радиус должен быть положительным.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

def calculate_area(area: Union[Circle, Triangle]) -> float:
    # Вычисление площади области, не зная ее типа.
    return Area_of_a_figure.calculate_area(area)