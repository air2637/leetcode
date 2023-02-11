
# https://leetcode.cn/problems/sqrtx/

import unittest
from parameterized import parameterized

class Solution():

    def mySqrt(self, num: int) -> int:
        if num == 0:
            return 0
        x_i = num
        c = num
        while True:
            x_j = 0.5 * (x_i + c / x_i)
            if abs(x_i - x_j) < 1e-7:
                break
            x_i = x_j
        return int(x_i)


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        (8, 2)
    ])
    def test_mySqrt(self, num, expected):
        actual = self.solution.mySqrt(num)
        self.assertEqual(actual, expected)