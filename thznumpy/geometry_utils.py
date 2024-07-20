"""本模块是一些条件判断
例如，给出一个点和一条直线判断点是否在直线上
# TODO 为这个文件命名
"""
import sympy


def is_point_on_line(point, line):
    """判断点是否在直线上"""
    x, y = sympy.symbols("x y")
    x1, y1 = point.get_position()
    eq_str = line.get_eq()
    eq = sympy.Eq(
        *[sympy.parse_expr(x) for x in eq_str.split('=')]
        ).subs({x: x1, y: y1})
    if eq is sympy.logic.boolalg.BooleanTrue():
        return True
    else:
        return False
