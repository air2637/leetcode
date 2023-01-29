import unittest
from parameterized import parameterized
from typing import List

# https://leetcode.cn/problems/3sum/

"""
Sort the list from smallest to the largets
3 pointers, p1, p2 are index for the first 2 numbers, p3 are the index for th largest number
while p1 < len(nums)-2:
    while p2 < p3:
        find the sum of nums[p1], nums[p2], nums[p3]
        if the sum > 0, move p3 to left
        else move the p2 to right
    shift p1 one index right
    set p2 = p1 + 1
    p3 = last index

"""


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        the_result = [] 
        p1 = 0
        while p1 < len(nums) - 2:
            # print(f"refreshing p1 {p1}")
            if p1 > 0 and nums[p1] == nums[p1-1]:
                # skip the p1 as there has been a result populated with nums[p1-1] as the first value
                p1 += 1
                continue 
            target_sum = 0 - nums[p1]
            p2 = p1 + 1
            p3 = len(nums)-1
            while p2 < p3:
                the_sum = nums[p2] + nums[p3]
                if the_sum > target_sum:
                    p3 -= 1
                elif the_sum < target_sum:
                    p2 += 1
                else:
                    # print(f"indexes are {p1}, {p2}, {p3}")
                    the_result.append([nums[p1], nums[p2], nums[p3]])
                    while p2 < p3 and nums[p2] == nums[p2+1]:
                        p2 += 1
                    while p2 < p3 and nums[p3] == nums[p3-1]:
                        p3 -= 1
                    p2 += 1 # still can shift the pointer and the new p2 pointed value has been added into the result set
                    p3 -= 1
            p1 += 1
        return the_result


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([-1,0,1,2,-1,-4], ([-1,-1,2],[-1,0,1])),
        ([0,1,1], ()),
        ([0,0,0], ([0,0,0],)),
        ([-5,1,2,4,4], ([-5,1,4],))
    ])
    def test_threeSum(self, nums, expected):
        self.assertTupleEqual(expected, tuple(self.solution.threeSum(nums)))