import unittest

from typing import Iterable as _Iterable, Tuple as _Tuple

from main import find_intersection_dots, find_intersection_dots_right


DELTA = 10 ** -6


class TestFindIntersectionDots(unittest.TestCase):
    def template_test(self, examples: _Iterable[_Tuple[float, float, float]]):
        for i, (a, b, d) in enumerate(examples):
            with self.subTest(i=i, msg=f'a: {a}, b: {b}, d: {d}'):
                result = find_intersection_dots(a, b, d)
                right_result = find_intersection_dots_right(a, b, d)
                self.assertEqual(len(result), len(right_result))
                for solution in zip(result, right_result):
                    first_pair, second_pair = solution
                    for value in zip(first_pair, second_pair):
                        first, second = value
                        self.assertAlmostEqual(first, second, delta=DELTA)

    def test_no_solution(self):
        examples = [(1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0), (7, 0, 0), (8, 0, 0), (9, 0, 0)]
        self.template_test(examples)

    def test_one_solution(self):
        examples = [(-5, -3, 4), (-5, -3, 5), (-5, -2, -1), (-5, -2, 0), (-5, -2, 1), (-5, -2, 2), (-5, -2, 3),
                    (-5, -2, 4), (-5, -1, -3), (-5, -1, -2), (-5, -1, -1), (-5, -1, 0), (-5, -1, 1), (-5, -1, 2),
                    (-5, -1, 3), (-5, -1, 4), (-5, -1, 5), (-5, 0, -4), (-5, 0, -3), (-5, 0, -2), (-5, 0, -1),
                    (-5, 0, 0), (-5, 0, 1), (-5, 0, 2), (-5, 0, 3), (-5, 0, 4), (-5, 0, 5), (-5, 1, -5)]
        self.template_test(examples)

    def test_two_solutions(self):
        examples = [(-8662, 4682, 9271), (-4342, 6598, 9828), (-1344, 3532, 5260), (-6049, 1026, -1942),
                    (-9952, 7112, -373),
                    (-7406, 5589, 3728), (-9331, 6551, -1208), (-8947, 4260, 566), (-3534, 7083, 9402),
                    (-9694, 4102, -3965),
                    (-7949, 2340, 8319), (-6244, 4025, 5403), (-8175, 6086, 164), (-4353, 4067, 6389),
                    (-6641, 4424, 6895),
                    (-6537, 4247, 6180)]
        self.template_test(examples)


if __name__ == '__main__':
    unittest.main()
