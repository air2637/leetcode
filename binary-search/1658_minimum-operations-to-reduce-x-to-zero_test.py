
# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/

"""_summary_
Every time, we have two options to decide to act on - remove the head, tail
We keep trying until cumulated sum is:
- greater than target x -> return -1
- equal to the target x -> return steps taken so far ?? but might not be the shortest steps ??
- when no more number to remove but still less than the target x -> return -1

Solve the problem recursively:

Every layer we decide taking head/tail value as the result step:
base cases:
    - if target == 0: means previous layer already got the ans, return 0 (meaning the begining of the step)
    - if target < 0: return -1
take head:
    - target = target - head
    - update the head pointer
    - call this func(head_pointer, tail_pointer, target) -> returns steps taking
    - step = step + 1 if step >=0 else -1
take tail:
    - target = target - tail
    - update the tail pointer
    - call this func(head_pointer, tail_pointer, target) -> returns steps taking
    - step = step + 1 if step >=0 else -1
compare the steps returning from taking head vs. taking tail -> return the smaller one

"""

from typing import List
import unittest
from parameterized import parameterized

class Solution():

    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        head, tail = -1, 0
        head_sum, tail_sum = 0, sum(nums)
        steps = len(nums) + 1
        for head in range(-1,len(nums)):
            if head >= 0:
                head_sum += nums[head]
            while tail < len(nums) and head_sum + tail_sum > x:
                tail_sum -= nums[tail]
                tail += 1
            if head_sum + tail_sum == x:
                steps = min(steps, (head + 1) + (len(nums)- tail))
        return steps if steps < len(nums) else -1

    def minOperations2(self, nums: List[int], x: int) -> int:
        def get_cumulative_sum(nums):
            cum_sums = [0] * len(nums)
            cum_sums[0] = nums[0]
            for i in range(1,len(nums)):
                cum_sums[i] = cum_sums[i-1] + nums[i]
            return cum_sums

        def binary_search(sorted_nums, looked_for):
            mid = -1
            left, right = 0, len(sorted_nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_nums[mid] > looked_for:
                    right = mid - 1
                elif sorted_nums[mid] < looked_for:
                    left = mid + 1
                else:
                    return mid
            return mid if sorted_nums[mid] == looked_for else -1
        
        nums.insert(0, 0)
        left_end_cum_sums = get_cumulative_sum(nums)
        nums.pop(0)
        nums.append(0)
        right_end_cum_sums = get_cumulative_sum(nums[::-1])
        # print(f"left end cum sums are {left_end_cum_sums}")
        # print(f"right end cum sums are {right_end_cum_sums}")
        cur_steps = 0 
        for i in range(len(nums)):
            if left_end_cum_sums[i] <= x:
                # print(f"left side getting {left_end_cum_sums[i]}, so need right value {x - left_end_cum_sums[i]}")
                found_idx = binary_search(right_end_cum_sums, x - left_end_cum_sums[i])
                # print(f"is right found ? {found_idx}")
                if found_idx >= 0:
                    if (found_idx == len(right_end_cum_sums) - 1 and i != 0) \
                        or (found_idx != 0 and i == len(left_end_cum_sums) - 1):
                        continue
                    if cur_steps == 0:
                        cur_steps = (found_idx + i)
                    cur_steps = min(cur_steps, (found_idx + i))
                    # print(f"updating the cur_steps to {cur_steps}")
            else:
                break
        return cur_steps if cur_steps > 0 else -1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,1,4,2,3], 5, 2),
        # ([5,6,7,8,9], 4, -1),
        # ([3,2,20,1,1,3], 10, 5),
        # ([1,1],3, -1)
    ])
    def test_minOperations(self, nums, x, expected):
        print()
        actual = self.solution.minOperations(nums, x)
        self.assertEqual(actual, expected)