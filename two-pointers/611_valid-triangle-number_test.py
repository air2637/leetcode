# https://leetcode.cn/problems/valid-triangle-number/

"""
condition of a triangle 3 sides:
a + b > c
a + c > b
b + c > a
if we sort the length, so that a < b < c, and for sure b + c > a , a + c > b
left with a check on whether a + b > c


|-|-|------------------|---------
a b c_start           c_end

|--|-|-------------------|---------
a  b c_start           c_end
"""


from typing import List
import unittest
from parameterized import parameterized

class Solution():

    # def triangleNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #     count = 0
    #     for a_index in range(len(nums) -2):
    #         for b_index in range(a_index + 1, len(nums) - 1):
    #             c_index = b_index + 1
    #             while c_index < len(nums) and  nums[a_index] + nums[b_index] > nums[c_index]:
    #                 print(f"valid nums are {a_index}, {b_index}, {c_index}")
    #                 c_index += 1
    #             count += (c_index - b_index -1)
    #     return count

    # def triangleNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #     count = 0
    #     for a_idx in range(len(nums)-2):
    #         b_idx = a_idx + 1
    #         c_idx = len(nums) - 1
    #         while b_idx < c_idx:
    #             if (nums[a_idx] + nums[b_idx]) < nums[c_idx]:
    #                 b_idx += 1
    #             else:
    #                 count += (c_idx - b_idx) 
    #                 c_idx -= 1

    """
    The essence of two pointer here is that two move in direction of towarding each other.
    So the outer most loop for C (locking c value) -> So logic for A and B are moving toward each other (inward)
    """
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for c in range(len(nums)-1,1,-1):
            b = c - 1
            a = 0
            while a < b:
                if nums[a] + nums[b] <= nums[c]:
                    a += 1
                else:
                    count += b - a 
                    b -= 1
        return count

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([2,2,3,4], 3),
        ([4,2,3,4], 4),
        ([7,0,0,0], 0),
        ([1,1,1,0], 1),
    ])
    def test_triangleNumber(self, nums, expected):
        print()
        actual = self.solution.triangleNumber(nums)
        self.assertEqual(actual, expected)