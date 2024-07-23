# classes module
`thznumpy.classes`

## preparation
```python
import thznumpy
```

## Point
### Point object,Represents a point in a plane rectangular coordinate system
Usage：
```python
thznumpy.Point(name, x, y)
```
Parameters：
| parameter | required | type | description |
| :--- | :---: | :---: | ---: |
| name | Y | str | the name of the point |
| x | Y | int<sup>1</sup> | the abscissa of plane rectangular coordinate system |
| y | Y | int<sup>2</sup> | the ordinate of the plane rectangular coordinate system |

Tip：

1.The type of `x` can be int, float, as well as various data types from numpy and sympy

2.The type of `y` can be int, float, as well as various data types from numpy and sympy

example:
```python
>>> import thznumpy
>>> thznumpy.Point("O", 0, 0)
<Point object name=O x=0 y=0>
>>> thznumpy.Point("A", pow(2, 0.5), 0)
<Point object name=A x=1.4142135623730951 y=0>
```

### the methods of Point object
| method | desicription |
| :--- | ---: |
| `get_position(self)` | get the coordinates of the  point,returns a tuple |

#### get_position
get the coordinates of the point,tuple(x, y)
parameter list：None

example:
```python
>>> import thznumpy
>>> p1 = thznumpy.Point("O", 0, 0)
>>> print(p1.get_position())
(0, 0)
```

## Line
### Line object,表示在平面直角坐标系上的直线
使用方法：
```python
thznumpy.Line(p1, p2)
```
参数列表：
| 参数名称 | 是否必填 | 参数类型 | 说明 |
| :--- | :---: | :---: | ---: |
| p1 | Y | thznumpy.Point | 直线上的一个点 |
| p2 | Y | thznumpy.Point | 直线上的另一个点 |


示例:
```python
>>> import thznumpy
>>> p1 = thznumpy.Point("O", 0, 0)
>>> p2 = thznumpy.Point("A", pow(2, 0.5), 0)
>>> L1 = thznumpy.Line(p1, p2)
>>> L1
<Line OA <y = 0>         p1=(0, 0)         p2=(1.4142135623730951, 0)>
>>>
```

### Line对象的方法
| 方法 | 说明 |
| :--- | ---: |
| `get_eq(self)` | 获取直线的标准方程,返回一个字符串 |
| `get_eq_obj(self)` | 获取直线的标准方程,返回sympy.Eq |
| `get_eq(self)` | 获取的斜率,返回浮点数或`numpy.inf` |

示例:
```python
import thznumpy
>>> p1 = thznumpy.Point("O", 0, 0)
>>> p2 = thznumpy.Point("A", pow(2, 0.5), 0)
>>> L1 = thznumpy.Line(p1, p2)
>>> # get_eq
>>> L1.get_eq()
'y = 0'
>>> # get_eq_obj
>>> L1.get_eq_obj()
Eq(y, 0)
```