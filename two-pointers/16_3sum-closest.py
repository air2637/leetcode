import sys
import unittest
from parameterized import parameterized
from typing import List



# https://leetcode.cn/problems/3sum-closest/

class Solution():

    def threeSumClosest(self, nums:List[int], target:int) -> int:
        nums.sort()
        min_diff = sys.maxsize
        min_diff_sum = nums[0] + nums[1] + nums[2]
        p1 = 0
        while p1 < len(nums) - 2:
            print(f"current p1 {p1}")
            # skip the duplicate where starting with the same value as nums[p1-1]
            while p1 - 1 >= 0 and p1 < len(nums) - 2 and nums[p1] == nums[p1 - 1]:
                p1 += 1
            
            p2 = p1 + 1
            p3 = len(nums) - 1
            print(f"now p2 {p2}, and p3 {p3}")
            while p2 < p3:
                cur_sum = nums[p1] + nums[p2] + nums[p3]
                if abs(cur_sum - target) < min_diff:
                    min_diff = abs(cur_sum - target)
                    min_diff_sum = cur_sum
                if min_diff == 0:
                    return cur_sum
                if target > cur_sum:
                    p2 += 1 
                    while p2 < p3 and nums[p2] == nums[p2-1]:
                        p2 += 1
                else:
                    p3 -= 1
                    while p2 < p3 and nums[p3] == nums[p3+1]:
                        p3 -= 1
            p1 += 1
        return min_diff_sum


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        # ([-1,2,1,-4], 1, 2),
        # ([0,0,0], 1, 0),
        # ([0,1,2],3,3),
        # ([-100,-98,-2,-1],-101,-101),
        # ([1,1,1,1], 0, 3),
        ([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -14, -15)
    ])
    def test_threeSumClosest(self, nums, target, expected):
        self.assertEqual(expected, self.solution.threeSumClosest(nums, target))
    
    