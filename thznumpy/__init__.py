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
    'Point',
    'Line',
]

from . import utils
from .classes import Point, Line

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
