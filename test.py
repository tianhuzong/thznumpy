"""本模块是thznumpy的测试模块
"""

import unittest
import numpy as np
import thznumpy


class ThzNumpyClassesTestCase(unittest.TestCase):
    """classes模块的测试类"""
    def test_Point(self):
        """测试创建点对象"""
        p1 = thznumpy.Point("A", 5, 2)
        self.assertEqual(p1.name, "A")
        self.assertEqual(p1.x, 5)
        self.assertEqual(p1.y, 2)
        self.assertEqual(p1.get_position(), (5, 2))

    def test_Line_usual(self):
        """测试创建正常的线对象(线不会垂直于坐标轴)"""
        A = thznumpy.Point("A", 0, 0)
        B = thznumpy.Point("B", 5201314, 5201314)
        L1 = thznumpy.Line(A, B)
        # 测试线的方程
        eq = L1.get_eq()
        self.assertTrue(
                eq == "x - y = 0" or eq == "y - x = 0",
                f"Failed,expect 'x - y = 0' or 'y - x = 0',but got {eq}"
                )
        # 测试线的斜率
        slope = L1.get_slope()
        self.assertEqual(slope, 1.0)

    def test_Line_unusual(self):
        """测试不正常的线(平行于坐标轴)"""
        # 垂直于y
        A = thznumpy.Point("A", 1, 20)
        B = thznumpy.Point("B", 5201314, 20)
        L1 = thznumpy.Line(A, B)
        # 测试线的方程
        eq = L1.get_eq()
        self.assertEqual(
                eq,
                "y - 20 = 0",
                f"Failed,expect 'y - 20 = 0',but got {eq}"
                )
        # 测试线的斜率
        slope = L1.get_slope()
        self.assertEqual(slope, 0.0)

        # 垂直于x
        A = thznumpy.Point("A", 1, 20)
        B = thznumpy.Point("B", 1, 520)
        L1 = thznumpy.Line(A, B)
        # 测试线的方程
        eq = L1.get_eq()
        self.assertEqual(
                eq,
                "x - 1 = 0",
                f"Failed,expect 'x - 1 = 0',but got {eq}"
                )
        # 测试线的斜率
        slope = L1.get_slope()
        self.assertEqual(slope, np.inf)


class ThzNumpyGeometryUtilsTestCase(unittest.TestCase):
    """geometry_utils模块的测试类"""

    def test_is_point_on_line(self):
        """测试点是否在直线上"""

        p1 = thznumpy.Point("A", 5, 2)
        p2 = thznumpy.Point("B", 10, 4)
        L1 = thznumpy.Line(p1, p2)

        # 1.点在直线上
        p_checked = thznumpy.Point("C", 20, 8)
        self.assertTrue(thznumpy.is_point_on_line(p_checked, L1))

        # 2.点不在直线上
        p_checked2 = thznumpy.Point("D", 20, 7)
        self.assertFalse(thznumpy.is_point_on_line(p_checked2, L1))

    def test_are_lines_parallel(self):
        """测试两直线是否平行"""
        p1 = thznumpy.Point("A", 5, 2)
        p2 = thznumpy.Point("B", 10, 4)

        p3 = thznumpy.Point("C", 5, 3)
        p4 = thznumpy.Point("D", 10, 5)

        p5 = thznumpy.Point("E", 15, 6)
        p6 = thznumpy.Point("F", 20, 8)

        p7 = thznumpy.Point("G", 5, 0)
        p8 = thznumpy.Point("H", 7, 20)

        L1 = thznumpy.Line(p1, p2)
        L2 = thznumpy.Line(p3, p4)
        L3 = thznumpy.Line(p5, p6)
        L4 = thznumpy.Line(p7, p8)

        # 测试平行
        self.assertTrue(thznumpy.are_lines_parallel(L1, L2))
        # 测试重合
        self.assertFalse(thznumpy.are_lines_parallel(L1, L3))
        # 测试不平行
        self.assertFalse(thznumpy.are_lines_parallel(L1, L4))

    def test_are_lines_perpendicular(self):
        """测试两直线是否垂直"""
        p1 = thznumpy.Point("A", 5, 2)
        p2 = thznumpy.Point("B", 10, 4)

        p3 = thznumpy.Point("C", 0, 0)
        p4 = thznumpy.Point("D", 1, -2.5)

        p5 = thznumpy.Point("E", 15, 6)
        p6 = thznumpy.Point("F", 20, 8)

        L1 = thznumpy.Line(p1, p2)
        L2 = thznumpy.Line(p3, p4)
        L3 = thznumpy.Line(p5, p6)

        # 测试垂直
        self.assertTrue(thznumpy.are_lines_perpendicular(L1, L2))
        # 测试不垂直
        self.assertFalse(thznumpy.are_lines_perpendicular(L1, L3))

    def test_get_intersection(self):
        """测试获取两直线的交点"""
        p1 = thznumpy.Point("A", 5, 2)
        p2 = thznumpy.Point("B", 10, 4)

        p3 = thznumpy.Point("C", 5, 3)
        p4 = thznumpy.Point("D", 10, 5)

        p5 = thznumpy.Point("E", 15, 6)
        p6 = thznumpy.Point("F", 20, 8)

        p7 = thznumpy.Point("G", 0, 0)
        p8 = thznumpy.Point("H", 1, -2.5)

        L1 = thznumpy.Line(p1, p2)
        L2 = thznumpy.Line(p3, p4)
        L3 = thznumpy.Line(p5, p6)
        L4 = thznumpy.Line(p7, p8)

        # 两直线平行
        with self.assertRaises(ValueError):
            thznumpy.get_intersection("O", L1, L2)
        # 两直线重合
        with self.assertRaises(ValueError):
            thznumpy.get_intersection("O", L1, L3)
        self.assertEqual(
            thznumpy.get_intersection("O", L1, L4).get_position(),
            thznumpy.Point("O", 0, 0).get_position()
            )
