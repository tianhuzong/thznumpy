"""本模块是thznumpy的测试模块
"""

import unittest
import numpy as np
import thznumpy

class ThzNumTestCase(unittest.TestCase):

    def test_Point(self):
        """测试创建点对象"""
        #import thznumpy
        p1 = thznumpy.Point("A",5,2)
        self.assertEqual(p1.name,"A")
        self.assertEqual(p1.x,5)
        self.assertEqual(p1.y,2)
        self.assertEqual(p1.get_position(),(5,2))

    def test_Line_usual(self):
        """测试创建正常的线对象(线不会垂直于坐标轴)"""
        A = thznumpy.Point("A",0,0)
        B = thznumpy.Point("B",5201314,5201314)
        L1 = thznumpy.Line(A,B)
        #测试线的方程
        eq = L1.get_eq()
        self.assertTrue(
                eq == "x - y = 0" or eq == "y - x = 0",
                f"Failed,expect 'x - y = 0' or 'y - x = 0',but got {eq}"
                )
        #测试线的斜率
        slope = L1.get_slope()
        self.assertEqual(slope,1.0)

    def test_Line_unusual(self):
        """测试不正常的线(平行于坐标轴)"""
        # 垂直于y
        A = thznumpy.Point("A",1,20)
        B = thznumpy.Point("B",5201314,20)
        L1 = thznumpy.Line(A,B)
        #测试线的方程
        eq = L1.get_eq()
        self.assertEqual(
                eq,
                "y - 20 = 0",
                f"Failed,expect 'y - 20 = 0',but got {eq}"
                )
        #测试线的斜率
        slope = L1.get_slope()
        self.assertEqual(slope,0.0)

        # 垂直于x
        A = thznumpy.Point("A",1,20)
        B = thznumpy.Point("B",1,520)
        L1 = thznumpy.Line(A,B)
        #测试线的方程
        eq = L1.get_eq()
        self.assertEqual(
                eq,
                "x - 1 = 0",
                f"Failed,expect 'x - 1 = 0',but got {eq}"
                )
        #测试线的斜率
        slope = L1.get_slope()
        self.assertEqual(slope,np.inf)
