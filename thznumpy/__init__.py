"""天狐宗数学库
   _____   _             _   _                                     
  |_   _| | |__    ____ | \ | |  _   _   _ __ ___    _ __    _   _ 
    | |   | '_ \  |_  / |  \| | | | | | | '_ ` _ \  | '_ \  | | | |
    | |   | | | |  / /  | |\  | | |_| | | | | | | | | |_) | | |_| |
    |_|   |_| |_| /___| |_| \_|  \__,_| |_| |_| |_| | .__/   \__, |
                                                    |_|      |___/ 

"""
version = "0.0.1"
author = "Sen"
email = "tianhuzong@qq.com"

__all__ = [
    'utils',
    'classes',
    'geometry_utils',  # TODO 修改
    'Point',
    'Line',
    'is_point_on_line',
]

from . import utils, classes, geometry_utils
from .classes import Point, Line
from .geometry_utils import is_point_on_line

__art_text = """
   _____   _             _   _                                     
  |_   _| | |__    ____ | \ | |  _   _   _ __ ___    _ __    _   _ 
    | |   | '_ \  |_  / |  \| | | | | | | '_ ` _ \  | '_ \  | | | |
    | |   | | | |  / /  | |\  | | |_| | | | | | | | | |_) | | |_| |
    |_|   |_| |_| /___| |_| \_|  \__,_| |_| |_| |_| | .__/   \__, |
                                                    |_|      |___/ 
"""

print(
    __art_text,
    "version -> {}\n".format(version),
    "pypi -> https://pypi.org/project/thznumpy/\n",
    "github -> https://github.com/tianhuzong/thznumpy",
)
