
# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/

"""_summary_
brute force.

set one pointer p1 from beginning of nums1, one pointer p2 from begining of num2.
iterate over nums1:
    search over nums2 so that p2 points to the same value as p1
    move both p1, p2 to its right, increment the counter as long as the values underlying p1, p2 matches.
    break when no longer match. (wait! can't just break here, as the same number may occur in succeeding sequence,
    and might be a longer match sequence there.)
    revert p2 to the beginning of nums2 again.
"""

from typing import List
import unittest
from parameterized import parameterized

class Solution():

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = [[0 for j in range(len(nums2))] for i in range(len(nums1))]
        cur_max = 0
        for i, vi in enumerate(nums1):
            for j, vj in enumerate(nums2):
                if vi == vj and i >=1 and j>=1:
                    res[i][j] = res[i-1][j-1] + 1
                elif vi == vj:
                    # i = 1 or/and j = 1 -> at least one of the two pointers is at the beginning
                    res[i][j] = 1
                cur_max = max(cur_max, res[i][j])
        return cur_max

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,2,3,2,1], [3,2,1,4,7], 3),
        ([0,0,0,0,0], [0,0,0,0,0], 5),
        ([1,2,3,2,1], [3,2,1,4,7], 3)
    ])
    def test_findLength(self, nums1, nums2, expected):
        actual = self.solution.findLength(nums1, nums2)
        self.assertEqual(actual, expected)