"""这个模块包含了一些数学函数
"""
from typing import Union
import numpy as np

# 三角函数


def sin(x: int | float | list):
    """正弦函数
    :params x: int | float | list 角度值,注意是以角度为单位,可以传入一个数组
    :return np.float64 | np.array 返回这个角(这些角)的正弦值
    """
    return np.sin(np.deg2rad(x))


def arcsin(x: Union[np.array, list]):
    """反正弦函数
    :params x: np.array | list | np.float64 正弦值,在-1到1之间,可以传入一个数组
    :return np.array |  np.float64 返回角度值
    """
    return np.deg2rad(np.arcsin(x))


def cos(x: int | float | list):
    """正弦函数
    :params x: int | float | list 角度值,注意是以角度为单位,可以传入一个数组
    :return np.float64 | np.array 返回这个角(这些角)的余弦值
    """
    return np.cos(np.deg2rad(x))


def arccos(x: Union[np.array, list]):
    """反正弦函数
    :params x: np.array | list | np.float64 余弦值,在-1到1之间,可以传入一个数组
    :return np.array |  np.float64 返回角度值
    """
    return np.deg2rad(np.arccos(x))


def tan(x: int | float | list):
    """正切函数
    :params x: int | float | list 角度值,注意是以角度为单位,可以传入一个数组
    :return np.float64 | np.array 返回这个角(这些角)的正切值
    """
    return np.tan(np.deg2rad(x))


def arctan(x: Union[np.array, list]):
    """反正切函数
    :params x: np.array | list | np.float64 正切值,可以传入一个数组
    :return np.array |  np.float64 返回角度值
    """
    return np.rad2deg(np.arctan(x))
