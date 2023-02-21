
# https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/





from typing import List
import unittest
from parameterized import parameterized

class Solution:

    def isCapacitySatisfied(self, capacity, days, weights):
        counter = days
        i = 0
        accumulated = 0
        while i < len(weights):
            while i < len(weights) and accumulated <= capacity:
                accumulated += weights[i]
                # print(f"added {i} with value {weights[i]}")
                i += 1
            counter -= 1
            # print(f"left with {counter} days, i {i}")
            if accumulated <= capacity and i >= len(weights):
                break
            accumulated = 0
            i -= 1
            # print(f"now reset i to {i}\n")
        return True if counter>=0 else False

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lower, upper = max(weights), sum(weights)
        # we iterate between the lower and upper to find the mix capacity that fulfill the days condition
        while lower < upper:
            capacity = lower + (upper - lower) // 2
            if self.isCapacitySatisfied(capacity, days, weights):
                upper = capacity
            else:
                lower = capacity + 1
        # what a superise
        return upper


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()
    
    @parameterized.expand([
        (20, 5, [1,2,3,4,5,6,7,8,9,10], True),
        (15, 5, [1,2,3,4,5,6,7,8,9,10], True),
        (14, 5, [1,2,3,4,5,6,7,8,9,10], False),
    ])
    def test_isCapacitySatisfied(self, capacity, days, weights, expected):
        print()
        actual = self.solution.isCapacitySatisfied(capacity, days, weights)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        ([1,2,3,4,5,6,7,8,9,10], 5, 15),
        ([3,2,2,4,1,4], 3, 6),
        ([1,2,3,1,1], 4, 3)
    ])
    def test_shipWithinDays(self, weights, days, expected):
        actual = self.solution.shipWithinDays(weights, days)
        self.assertEqual(actual, expected)