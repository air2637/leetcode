# https://leetcode.cn/problems/count-the-number-of-good-subarrays/

from collections import defaultdict
from typing import Counter, List
import unittest
from parameterized import parameterized

class Solution:

    def countGood(self, nums: List[int], k: int) -> int:
        left = right = 0
        counter = Counter()
        pairs = 0
        good_cnt = 0
        while right < len(nums):
            # what a smart logic - when the same number appears, would increse the pairs the freq of the number before updating
            pairs += counter[nums[right]]
            counter[nums[right]] += 1
            while pairs >= k and left < right:
                good_cnt += len(nums) - (right + 1) + 1
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                left += 1
            right += 1
        return good_cnt

    def getCombinationCount(self, objectNums: int, objectChoosenNums: int) -> int:
        dividend = divisor = 1
        current = objectNums
        for i in range(objectChoosenNums):
            dividend *= current
            divisor *= (i + 1)
            current -= 1
        return dividend // divisor

    def countGood2(self, nums: List[int], k: int) -> int:
        left = right = 0
        num_counter = Counter()
        good_sublist_cnt = 0
        res = 0
        num_cnt = defaultdict(int) 
        while right < len(nums):
            num_counter[nums[right]] += 1
            combo = self.getCombinationCount(num_counter[nums[right]], 2) 
            delta = combo - num_cnt[nums[right]]
            num_cnt[nums[right]] = combo
            good_sublist_cnt += delta
            if good_sublist_cnt >= k:
                print(f"satisfied {nums[left:right+1]}")
                res += len(nums) - (right + 1) + 1

                print("now shifting left pointer") 
                while good_sublist_cnt >= k and left < right:
                    before = num_cnt[nums[left]]
                    num_counter[nums[left]] -= 1
                    after = self.getCombinationCount(num_counter[nums[left]], 2)
                    num_cnt[nums[left]] = after
                    if after < before:
                        good_sublist_cnt -= (before - after)
                    if good_sublist_cnt >=k:
                        print(f"satisdied {nums[left:right+1]}")
                        res += len(nums) - (right + 1) + 1
                    left += 1

            right += 1
        return res

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([3,1,4,3,2,2,4], 2, 4),
        ([1,1,1,1,1], 10, 1),
        ([2,1,3,1,2,2,3,3,2,2,1,1,1,3,1],11, 21),
        ([2,3,1,3,2,3,3,3,1,1,3,2,2,2], 18, 9)
    ])
    def test_countGood(self, nums, k, expected):
        actual = self.solution.countGood(nums, k)
        self.assertEqual(actual, expected)
