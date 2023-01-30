


# https://leetcode.cn/problems/next-permutation/

"""
The objective is to find the nearest permutation that has greater value than the given nums.
We need to search from 'the lowest significant' digit and find the num that barely greater than the digit.
Pseudocode:
right = nums[-1]
from the last num and check till it reaches the 1st num:
    if num_check >= right:
        continue
    else:
        from last digit checking reversly to the index of num_check + 1:
            see if any num > num_check:
                swap the value
                return
    right = num_check
return the reverse of current nums
"""


from parameterized import parameterized
import unittest
from typing import List

class Solution():

    def nextPermutation(self, nums: List[int]) -> None:
        
        def doReverse(nums, leftBoundary, rightBoundary):
            while leftBoundary < rightBoundary:
                nums[leftBoundary], nums[rightBoundary] = nums[rightBoundary], nums[leftBoundary]
                leftBoundary += 1
                rightBoundary -= 1

        right = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= right:
                right = nums[i]
                continue
            for k in range(len(nums)-1, i, -1):
                if nums[k] > nums[i]:
                    nums[i], nums[k] = nums[k], nums[i]
                    # after the swap, we need to reverse the order for the numbers from index i onwards,
                    # as they are in reverse order before the operation.
                    doReverse(nums, i+1, len(nums)-1)
                    return
            right = nums[i]
        doReverse(nums, 0, len(nums)-1) # equivalent to nums.sort()


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,2,3], [1,3,2]),
        ([2,2,1], [1,2,2]),
        ([1,1,5], [1,5,1]),
        ([1,3,2], [2,1,3]),
        ([2,3,1], [3,1,2])
    ]) 
    def test_nextPermutation(self, nums, expected):
        self.solution.nextPermutation(nums)
        self.assertEqual(expected, nums)