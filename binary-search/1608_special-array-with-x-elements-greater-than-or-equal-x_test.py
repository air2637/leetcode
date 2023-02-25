# https://leetcode.cn/problems/special-array-with-x-elements-greater-than-or-equal-x/

from typing import List
import unittest
from parameterized import parameterized


class Solution:

    def specialArray(self, nums:List[int]) -> int:
        lower, upper = 0, len(nums)
        nums.sort()
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            num_greater = self.howManyNumsGreaterThanValue(mid, nums)
            if num_greater > mid:
                # means more than mid numbers having their value >= mid, need to check a value greater than mid
                lower = mid + 1
            elif num_greater < mid:
                # means less than mid numbers having their value >= mid, need to check a value smaller than mid
                upper = mid - 1
            else:
                # handle special case where 0 number having their value >= 0
                # print(f"specialArray, returning {mid}")
                return mid if mid > 0 else -1
        return -1

    def howManyNumsGreaterThanValue(self, toCheck: int, sortedNums: List[int]) -> int:
        print(f"checking {toCheck} in {sortedNums}")
        lower , upper = 0, len(sortedNums) - 1
        ans = 0
        while lower <= upper and upper < len(sortedNums):
            mid = lower + (upper - lower) // 2
            if sortedNums[mid] >= toCheck:
                ans = len(sortedNums) - mid
                upper = mid - 1
            else:
                lower = mid + 1
        # print(f"returning {ans}")
        return ans

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()



    @parameterized.expand([
        ([3,5],2),
        ([0,0],-1),
        ([0,4,3,0,4],3),
    ]) 
    def test_specialArray(self, nums, expected):
        print()
        actual = self.solution.specialArray(nums)
        self.assertEqual(actual, expected)
