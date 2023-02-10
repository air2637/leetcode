

# https://leetcode.cn/problems/sort-colors/

from typing import List
import unittest
from parameterized import parameterized

class Solution():

    def sortColors(self, nums: List[int]) -> None:
        hasSawp = False
        i, j = 0, 1
        while True:
            hasSawp = False
            while j < len(nums):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    hasSawp = True
                i, j = j, j + 1
            if not hasSawp:
                return
            i, j = 0, 1
        print(nums)

class TestSolutionJ(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([0,2,1,0], [0,0,1,2]),
        ([2,0,2,1,1,0],[0,0,1,1,2,2])
    ]) 
    def test_sortColors(self, nums, expected):
        self.solution.sortColors(nums)
        self.assertListEqual(expected, nums)