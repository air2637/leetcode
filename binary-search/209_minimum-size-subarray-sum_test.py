
# https://leetcode.cn/problems/minimum-size-subarray-sum/


import sys
from typing import List
import unittest
from parameterized import parameterized

class Solution():

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        cur_sum = nums[i]
        min_len = sys.maxsize
        while j < len(nums):
            if cur_sum >= target:
                min_len = min(min_len, (j - i) + 1)
                if min_len == 1:
                    return min_len
                cur_sum -= nums[i]
                i += 1
            else:
                j += 1
                if j < len(nums):
                    cur_sum += nums[j]
        return 0 if min_len == sys.maxsize else min_len

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        (7,[2,3,1,2,4,3], 2),
        (4,[1,4,4], 1),
        (11,[1,1,1,1,1,1,1,1], 0),

    ])
    def test_minSubArrayLen(self, target, nums, expected):
        actual = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(actual, expected)

