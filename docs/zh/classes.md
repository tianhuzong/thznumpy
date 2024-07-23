# classes模块
`thznumpy.classes`

## 准备
```python
import thznumpy
```

## Point
### Point对象,表示在平面直角坐标系上的点
使用方法：
```python
thznumpy.Point(name, x, y)
```
参数列表：
| 参数名称 | 是否必填 | 参数类型 | 说明 |
| :--- | :---: | :---: | ---: |
| name | Y | str | 点的名称 |
| x | Y | int<sup>1</sup> | 平面直角坐标系的横坐标 |
| y | Y | int<sup>2</sup> |平面直角坐标系的纵坐标 |

注：

1.`x`的类型可以是int、float，甚至是numpy的一些数据类型、sympy的一些数据类型都可以

2.`y`的类型可以是int、float，甚至是numpy的一些数据类型、sympy的一些数据类型都可以

示例:
```python
>>> import thznumpy
>>> thznumpy.Point("O", 0, 0)
<Point object name=O x=0 y=0>
>>> thznumpy.Point("A", pow(2, 0.5), 0)
<Point object name=A x=1.4142135623730951 y=0>
```

### Point对象的方法
| 方法 | 说明 |
| :--- | ---: |
| `get_position(self)` | 获取点的坐标对,返回一个元组 |

#### get_position
返回点的坐标对,tuple(x, y)
参数列表：无

示例:
```python
>>> import thznumpy
>>> p1 = thznumpy.Point("O", 0, 0)
>>> print(p1.get_position())
(0, 0)
```

## Line
### Line对象,表示在平面直角坐标系上的直线
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