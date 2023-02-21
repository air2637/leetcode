
# https://leetcode.cn/problems/find-peak-element/

from typing import List
import unittest
from parameterized import parameterized

class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if mid == i:
                return i if nums[j] < nums[i] else j
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                j = mid
            else:
                i = mid
        return 0

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,2,3,1],(2,)),
        ([1,2,1,3,5,6,4],(1,5)),
        ([1,2],(1,))
    ])
    def test_findPeakElement(self, nums, expected):
        actual = self.solution.findPeakElement(nums)
        self.assertTrue(actual in expected)