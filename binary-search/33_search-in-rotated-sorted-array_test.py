
# https://leetcode.cn/problems/search-in-rotated-sorted-array/


"""_summary_
                8
            7
        6
    5
4
                                    4
                                3
                            2
                        1


6, 7, 8, 1, 2, 3, 4, 5

4, 5, 6, 7, 8, 1, 2, 3



if target between nums[left] and nums[right] -> no match for sure

when jump to the mid
if nums[mid] == target return
if the nums[mid] < target:
    normally -> left = mid
    but need to check if nums[right] < target, 
        -> yes, then right = mid
        -> no, then left = mid
else 
    normally -> right = mid
    but need to check if nums[left] > target,
        -> yes, then left = mid
        -> no, then right = mid
"""


from typing import List
import unittest
from parameterized import parameterized

class Solution():

    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1
        if nums[left] > target and nums[right] < target:
            return -1
        while left <= right:
            mid = left + (right - left) // 2
            print(f"checking mid @ {mid}, with value {nums[mid]}")
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if nums[right] < target and nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right boundary pointed value is sitting between nums[mid] and target, need to check the right half
                if nums[right] >= target and nums[mid] >= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
        ([4,5,6,7,8,1,2,3], 6, 2),
        ([4,5,6,7,8,1,2,3], 8, 4),
        ([3,1], 1, 1),
        ([1,3],3,1)
    ])
    def test_search(self, nums, target, expected):
        print(f"\nnums are {nums}, for searching {target}")
        actual = self.solution.search(nums, target)
        self.assertEqual(actual, expected)