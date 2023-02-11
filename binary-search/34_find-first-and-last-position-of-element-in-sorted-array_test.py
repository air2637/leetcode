

# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List
import unittest
from parameterized import parameterized

class Solution():

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     start, end = 0, len(nums) - 1
    #     found = False
    #     while start < end - 1:
    #         mid = start + (end - start) // 2
    #         if nums[mid] > target:
    #             end = mid
    #         elif nums[mid] < target:
    #             start = mid
    #         else:
    #             found = True
    #             break
    #     if not found and start > end:
    #         return [-1, -1]
    #     if not found and nums[start] != target and nums[end] != target:
    #         return [-1, -1]
    #     elif not found:
    #         mid = start if nums[start] == target else end
    #     left = right = mid
    #     while left - 1 >= 0 and nums[left-1] == nums[mid]:
    #         left -= 1
    #     while right + 1 < len(nums) and nums[right+1] == nums[mid]:
    #         right += 1
    #     return [left, right]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftBoundary = self.binarySearch(nums, target, True)
        rightBoundary = self.binarySearch(nums, target, False)
        print(f"left -> {leftBoundary}, right -> {rightBoundary}")
        if leftBoundary <= rightBoundary \
            and rightBoundary < len(nums) and leftBoundary + 1 >= 0 and rightBoundary >= 0 \
            and nums[leftBoundary + 1] == nums[rightBoundary]:
            return [leftBoundary + 1, rightBoundary]
        return [-1,-1]

    def binarySearch(self, nums, target, leftBoundary):
        left, right = 0, len(nums) - 1
        boundary = -1
        while left <= right:
            mid = left + (right - left) // 2
            if (nums[mid] < target) \
                    or (not leftBoundary and nums[mid] <= target):
                boundary = mid
                left = mid + 1
            else:
                right = mid - 1
        return boundary

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([5,7,7,8,8,10], 8, [3,4]),
        ([5,7,7,8,8,10], 6, [-1,-1]),
        ([], 6, [-1,-1]),
        ([1], 1, [0,0]),
        ([1,4], 4, [1,1]),
        ([1,3], 1, [0,0]),
    ])
    def test_searchRange(self, nums, target, expected):
        print()
        actual = self.solution.searchRange(nums, target)
        self.assertListEqual(actual, expected)