


# https://leetcode.cn/problems/4sum/




import unittest
from parameterized import parameterized
from typing import List


"""
Treat it as 2 outer loops + 1 two-pointers question
The 2 outer loops iterate all possible first 2 values and let the two-pointers look for the rest 2 values
Complexity should be O(n^2)*O(n) = O(n^3), comparing to brute force O(n^4)
"""

class Solution():

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result_list = []
        q1 = 0
        nums_length = len(nums)
        while q1 < nums_length - 3:
            # print(f"now q1 is {q1}")
            if q1 - 1 >= 0 and nums[q1] == nums[q1 - 1]:
                """
                 if first two values, say they are a, b and a = b
                 when both a and b are the candidates, means [a, b, x, x] has been added into the result list
                 when only a or b is the candidate, means [a, x, x, x] has been added, and no point to add [b, x, x, x], given a = b
                """
                q1 += 1
                continue
            q2 = q1 + 1
            while q2 < nums_length - 2:
                # print(f"now q2 is {q2}")
                if q2 > q1 + 1 and nums[q2] == nums[q2- 1]:
                    # adding q2 > q1 + 1 to allow the first occurance of nums[q2] as the 2nd number in the result set, though it has same value with its preceding
                    q2 += 1
                    continue
                q3 = q2 + 1
                q4 = nums_length - 1
                while q3 < q4:
                    cur_total = nums[q1] + nums[q2] + nums[q3] + nums[q4]
                    if cur_total == target:
                        # print(f"q3 is {q3}, q4 is {q4}")
                        result_list.append([nums[q1],nums[q2], nums[q3], nums[q4]])
                        q3 += 1
                        while q3 < q4 and nums[q3] == nums[q3 - 1]:
                            q3 += 1
                    elif cur_total > target:
                        q4 -= 1
                    else:
                        q3 += 1
                q2 += 1
            q1 += 1
        return result_list


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        # ([1,0,-1,0,-2,2], 0, ([-2,-1,1,2],[-2,0,0,2],[-1,0,0,1],)),
        # ([0,1,2,2,3,3,4], 10, ([0, 3, 3, 4], [1, 2, 3, 4],)),
        # ([2,2,2,2,2], 8, ([2,2,2,2],)),
        ([-2,-1,-1,1,1,2,2], 0, ([-2,-1,1,2],[-1,-1,1,1]))
    ])
    def test_fourSum(self, nums, target, expected):
        self.assertTupleEqual(expected, tuple(self.solution.fourSum(nums, target)))
        