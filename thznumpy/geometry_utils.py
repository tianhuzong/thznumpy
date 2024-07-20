"""本模块是一些条件判断
例如，给出一个点和一条直线判断点是否在直线上
"""
import sympy
import numpy as np
import thznumpy


def is_point_on_line(point, line) -> bool:
    """判断点是否在直线上
    :param point 点
    :type Point
    :param line 直线
    :type Line
    :return 在直线上返回True,否则返回False
    """
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


def are_lines_parallel(line1, line2) -> bool:
    """判断两直线是否平行
    当两直线重合(方程相同)时返回False
    :param line1 第一条直线
    :type Line
    :param line2 第二条直线
    :type Line
    :return 平行则True,否则返回False
    """
    if line1.get_eq() == line2.get_eq():
        return False
    elif line1.get_slope() == line2.get_slope():
        return True
    else:
        return False


def are_lines_perpendicular(l1, l2) -> bool:
    """判断两直线是否垂直
    :param l1 第一条直线
    :type Line
    :param l2 第二条直线
    :type Line
    :return 垂直返回True,否则返回False
    """
    m_l1 = l1.get_slope()
    m_l2 = l2.get_slope()
    if m_l1 == 0.0:
        if m_l2 == np.nan:
            return True
        else:
            return False
    elif m_l1 == np.nan:
        if m_l2 == 0.0:
            return True
        else:
            return False
    elif m_l1 * m_l2 == -1:
        return True
    else:
        return False


def get_intersection(name, l1, l2):
    """返回两直线的交点,平行或重合则抛出错误
    param: name 交点的名称
    param: l1 第一条直线
    param: l2 第二条直线
    throw: ValueError 当两条直线平行或重合时抛出错误
    return: 返回两直线交点`Point(name, x, y)`
    """
    if (l1.get_eq() == l2.get_eq()) or are_lines_parallel(l1, l2):
        raise ValueError("两直线平行或重合")
    point_position = [position[1] for position in sympy.solve([l1.get_eq_obj(),l2.get_eq_obj()]).items()]
    return thznumpy.Point(name,*point_position)