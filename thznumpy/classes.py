import sympy
import numpy as np
from thznumpy import utils

class Point:
    """点
    表示在平面直角坐标系上的点
    Point("A",5,2) # 表示点A在的坐标是(5,2)
    """
    def __init__(self, name: str, x, y):
        """点构造函数
        :param name : str The name of the point,点的名字
        :param x 横坐标,任意实数
        :param y 纵坐标,任意实数
        """
        self.name = name
        self.x = x
        self.y = y


    def get_position(self):
    	"""获取点的坐标对
    	:return tuple 坐标
    	"""
    	return self.x, self.y

    def __repr__(self):
        return f'<Point object name={self.name} x={self.x} y={self.y}>'

    def __str__(self):
        return f'{self.name}({self.x},{self.y})'


class Line:
    """直线
    表示在平面直角坐标系中的直线
    
    p1 = Point("A",0,0)
    p2 = Point("B",1,1)
    L1 = Line(p1,p2)
    """
    def __init__(self, p1, p2):
        """构造函数
        :param p1 直线的一个点
        """
        self.p1 = p1
        self.p2 = p2
        self.name = self.p1.name + self.p2.name

    def get_eq(self):
        """返回直线的标准方程"""
        x1, y1 = self.p1.get_position()
        x2, y2 = self.p2.get_position()
        x, y = sympy.symbols("x y")
        if x1 == x2:
            standard_eq = sympy.simplify(sympy.Eq(x - x1, 0))
        elif y1 == y2:
            standard_eq = sympy.simplify(sympy.Eq(y - y1, 0))
        else:
            line_eq = sympy.Eq((x - x1)/(x2 - x1), (y - y1)/(y2 - y1))
            standard_eq = sympy.simplify(line_eq)
        return str(standard_eq.lhs - standard_eq.rhs) + " = 0"

    def get_slope(self):
        """返回方程的斜率"""
        x1, y1 = self.p1.get_position()
        x2, y2 = self.p2.get_position()
        if x1 == x2:
            return np.inf
        return (y2 - y1) / (x2 - x1)

    def __repr__(self):
        return f"<Line {self.name} <{self.get_eq()}> p1={self.p1.get_position()} p2={self.p2.get_position()}>"
 
    def __str__(self):
        return f"Line {self.name}: {self.get_eq()}"
