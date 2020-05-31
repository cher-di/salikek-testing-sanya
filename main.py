import sympy as _sympy
from typing import Tuple as _Tuple


def find_intersection_dots(a: float, b: float, d: float) -> _Tuple[_Tuple[float, float]]:
    """Find intersection for two functions: y = sqrt(x - a) + b, y = |x - d|

    Args:
        a: float coefficient a
        b: float coefficient b
        d: float coefficient d

    Returns:
        tuple with tuples with x and y - intersection dots
    Raises:
        TypeError: an error occurred if a, b, or d is not float
    """
    for i in (a, b, d):
        if type(i) not in (int, float):
            raise TypeError(f'Сoefficient expected to have type - float, got - {type(i)}')

    d1 = 1 - 4 * (a - b - d)
    d2 = 1 - 4 * (a + b - d)

    def x_y(_k: float) -> (float, float):
        _x = _k ** 2 + a
        _y = abs(_x - d)
        return _x, _y

    result = []
    if d1 >= 0:
        k = (1 + d1 ** 0.5) / 2
        x, y = x_y(k)
        result.append((x, y))

        k = (1 - d1 ** 0.5) / 2
        if k >= 0:
            x, y = x_y(k)
            result.append((x, y))

    if d2 >= 0:
        k = (-1 + d2 ** 0.5) / 2
        if k >= 0:
            x, y = x_y(k)
            result.append((x, y))

    return tuple(result)


def find_intersection_dots_right(a: float, b: float, d: float) -> _Tuple[_Tuple[float, float]]:
    """Find intersection for two functions: y = sqrt(x - a) + b, y = |x - d|

    Args:
        a: float coefficient a
        b: float coefficient b
        d: float coefficient d

    Returns:
        tuple with tuples with x and y - intersection dots
    Raises:
        TypeError: an error occurred if a, b, or d is not float
    """
    for i in (a, b, d):
        if type(i) not in (int, float):
            raise TypeError(f'Сoefficient expected to have type - float, got - {type(i)}')

    x, y = _sympy.symbols('x, y')
    eq1 = _sympy.Eq(y - (x - a) ** 0.5 - b, 0)
    eq2 = _sympy.Eq(y - x + d, 0)
    eq3 = _sympy.Eq(y + x - d, 0)

    solution1 = _sympy.solve((eq1, eq2), (x, y))
    solution2 = _sympy.solve((eq1, eq3), (x, y))

    return tuple((_x.evalf(), _y.evalf()) for (_x, _y) in solution1 + solution2)


if __name__ == '__main__':
    print('App for find intersection points')
