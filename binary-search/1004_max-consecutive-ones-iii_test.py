# https://leetcode.cn/problems/max-consecutive-ones-iii/


from typing import List
import unittest
from parameterized import parameterized

class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        quota = k
        start = end = 0
        max_length = 0
        while end < len(nums):
            if nums[end] == 1:
                # if current end points to 1, keep counting
                end += 1
            elif quota > 0:
                # current end points to a 0, but we got quota!
                end += 1
                quota -= 1
            else:
                # current end points to a 0, and no more quota, time to check the length we reached so far
                max_length = max(max_length, end - start)
                # print(f"start is {start}, end is {end}, current length is {end - start}, max length is {max_length}")
                start += 1
                if nums[start - 1] == 0:
                    # return a quota if previous start points to a 0
                    quota += 1
        return max(max_length, end - start)


class testSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        # ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
        # ([1,1,1,0,0,0,1,1,1,1,0],3, 10)
        ([0,0,0,1], 4, 4)
    ])
    def test_longestOnes(self, nums, k, expected):
        print()
        actual = self.solution.longestOnes(nums, k)
        self.assertEqual(actual, expected)