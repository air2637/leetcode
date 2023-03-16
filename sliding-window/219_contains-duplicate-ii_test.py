# https://leetcode.cn/problems/contains-duplicate-ii/

from collections import Counter
from typing import List
import unittest
from parameterized import parameterized

class Solution:


    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        counter = Counter()
        while right < len(nums):
            counter[nums[right]] += 1
            if counter[nums[right]] >= 2:
                # print(f"now the right index is {right}, with count {counter[nums[right]]}")
                return True
            if right - left >= k:
                # print(f"right is {right}, left is {left}")
                counter[nums[left]] -= 1
                left += 1
            right += 1
        return False


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,2,3,1], 3, True),
        ([1,0,1,1], 1, True),
        ([1,2,3,1,2,3], 2, False),
    ])
    def test_containsNearbyDuplicate(self, nums, k, expected):
        actual = self.solution.containsNearbyDuplicate(nums, k)
        self.assertEqual(actual, expected)
