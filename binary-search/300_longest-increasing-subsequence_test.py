
# https://leetcode.cn/problems/longest-increasing-subsequence/

from typing import List
import unittest
from parameterized import parameterized

class Solution():

    def lengthOfLIS(self, nums: List[int])-> int:
        if not nums:
            return 0
        res = 1
        best_state_till_each_index = []
        for i, cur in enumerate(nums):
            if i == 0:
                best_state_till_each_index.append(1)
                continue
            cur_max_length = 1
            for j in range(i):
                if nums[j] < cur:
                    cur_max_length = max(cur_max_length, best_state_till_each_index[j]+1)
            best_state_till_each_index.append(cur_max_length)
            res = max(cur_max_length, res)
        # print(f"{best_state_till_each_index}")
        return res 


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([10,9,2,5,3,7,101,18], 4),
        ([4,10,4,3,8,9],3),
        ([1,3,6,7,9,4,10,5,6],6)
    ])
    def test_lengthOfLIS(self, nums, expected):
        actual = self.solution.lengthOfLIS(nums)
        self.assertEqual(actual, expected)