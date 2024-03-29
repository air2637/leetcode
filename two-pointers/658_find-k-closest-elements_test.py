

# https://leetcode.cn/problems/find-k-closest-elements/


from bisect import bisect_left
from collections import deque
import unittest
from parameterized import parameterized
from typing import List

class Solution:

    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     if x <= arr[0]:
    #         return arr[0:k]
    #     if x >= arr[-1]:
    #         return arr[-k:]
    #     # x is somewhere in between the arr[0] and arr[-1]
    #     res = deque()
    #     for n in arr:
    #         if len(res) >= k:
    #             if abs(res[0]-x) > abs(n-x):
    #                 res.popleft()        
    #                 res.append(n)
    #             elif res[0] == n:
    #                 # as the abs diff could be from both left of the target
    #                 continue
    #             else:
    #                 return list(res)
    #         else:
    #             res.append(n)
    #     return list(res)
    
        
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left points to the index where arr[:left] < x
        left = bisect_left(arr, x) - 1
        right = left + 1
        n = 1
        while n <= k:
            if left < 0:
                right += 1
            elif right < len(arr) and x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1
            n += 1
        return arr[left + 1: right]


class TestSoluton(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,2,3,4,5], 4, 3, [1,2,3,4]),
        ([1,2,3,4,5,12,13], 3, 6, [3,4,5]),
        ([1,2,3,4,5], 4, -1, [1,2,3,4]),
        ([1,1,1,10,10,10], 1, 9, [10])
    ])
    def test_findClosestElements(self, arr, k, x, expected):
        actual = self.solution.findClosestElements(arr, k, x)
        self.assertListEqual(actual, expected)