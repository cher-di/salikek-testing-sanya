import sympy as _sympy
from typing import Tuple as _Tuple


def find_intersection_dots(a: float, b: float, c: float, d: float) -> _Tuple[_Tuple[float, float]]:
    """Find intersection for two functions: y = sqrt(x - a) + b, y = |x - d|

    Args:
        a: float coefficient a
        b: float coefficient b
        c: float coefficient c
        d: float coefficient d

    Returns:
        tuple with tuples with x and y - intersection dots
    Raises:
        TypeError: an error occurred if a, b, c or d is not float
    """
    for i in (a, b, c, d):
        if type(i) not in (int, float):
            raise TypeError(f'Сoefficient expected to have type - float, got - {type(i)}')

    d1 = (b - 1) ** 2 - 4 * a * (c + d + 1)
    d2 = (b + 1) ** 2 - 4 * a * (c + d - 1)
    d3 = (b + 1) ** 2 - 4 * a * (c - d - 1)
    d4 = (b - 1) ** 2 - 4 * a * (c - d + 1)

    def _y(_x: float) -> float:
        return abs(abs(_x - 1) - d)

    result = []

    if d1 >= 0:
        x1 = (-(b - 1) + d1 ** 0.5) // (2 * a)
        x2 = (-(b - 1) - d1 ** 0.5) // (2 * a)
        for x in (x1, x2):
            if x >= 1 and abs(x - 1) - d >= 0:
                result.append((x, _y(x)))

    if d2 >= 0:
        x1 = (-(b + 1) + d2 ** 0.5) // (2 * a)
        x2 = (-(b + 1) - d2 ** 0.5) // (2 * a)
        for x in (x1, x2):
            if x < 1 and abs(x - 1) - d >= 0:
                result.append((x, _y(x)))

    if d3 >= 0:
        x1 = (-(b + 1) + d3 ** 0.5) // (2 * a)
        x2 = (-(b + 1) - d3 ** 0.5) // (2 * a)
        for x in (x1, x2):
            if x >= 1 and abs(x - 1) - d < 0:
                result.append((x, _y(x)))

    if d4 >= 0:
        x1 = (-(b - 1) + d4 ** 0.5) // (2 * a)
        x2 = (-(b - 1) - d4 ** 0.5) // (2 * a)
        for x in (x1, x2):
            if x < 1 and abs(x - 1) - d < 0:
                result.append((x, _y(x)))

    result = set(result)
    result = sorted(result)

    return tuple(result)


def find_intersection_dots_right(a: float, b: float, c: float, d: float) -> _Tuple[_Tuple[float, float]]:
    """Find intersection for two functions: y = sqrt(x - a) + b, y = |x - d|

    Args:
        a: float coefficient a
        b: float coefficient b
        c: float coefficient c
        d: float coefficient d

    Returns:
        tuple with tuples with x and y - intersection dots
    Raises:
        TypeError: an error occurred if a, b, c or d is not float
    """
    for i in (a, b, d):
        if type(i) not in (int, float):
            raise TypeError(f'Сoefficient expected to have type - float, got - {type(i)}')

    x, y = _sympy.symbols('x, y')
    left = _sympy.Eq(a * x ** 2 + b * x + c, 0)
    right1 = _sympy.Eq(x - 1 - d, 0)
    right2 = _sympy.Eq(-x + 1 - d, 0)
    right3 = _sympy.Eq(-x + 1 + d, 0)
    right4 = _sympy.Eq(x - 1 + d, 0)

    solution1 = _sympy.solve((left, right1), (x, y))
    solution2 = _sympy.solve((left, right2), (x, y))
    solution3 = _sympy.solve((left, right3), (x, y))
    solution4 = _sympy.solve((left, right4), (x, y))

    result1 = [(_x.evalf(), _y.evalf()) for (_x, _y) in solution1
               if type(_x.evalf()) != _sympy.core.add.Add and type(_y.evalf()) != _sympy.core.add.Add]
    result1 = [(x, y) for (x, y) in result1 if x >= 1 and abs(x - 1) - d >= 0]

    result2 = [(_x.evalf(), _y.evalf()) for (_x, _y) in solution2
               if type(_x.evalf()) != _sympy.core.add.Add and type(_y.evalf()) != _sympy.core.add.Add]
    result2 = [(x, y) for (x, y) in result2 if x < 1 and abs(x - 1) - d >= 0]

    result3 = [(_x.evalf(), _y.evalf()) for (_x, _y) in solution3
               if type(_x.evalf()) != _sympy.core.add.Add and type(_y.evalf()) != _sympy.core.add.Add]
    result3 = [(x, y) for (x, y) in result3 if x >= 1 and abs(x - 1) - d < 0]

    result4 = [(_x.evalf(), _y.evalf()) for (_x, _y) in solution4
               if type(_x.evalf()) != _sympy.core.add.Add and type(_y.evalf()) != _sympy.core.add.Add]
    result4 = [(x, y) for (x, y) in result4 if x < 1 and abs(x - 1) - d < 0]

    result = result1 + result2 + result3 + result4
    result = set(result)
    result = sorted(result)

    return tuple(result)


if __name__ == '__main__':
    print('App for find intersection points')
