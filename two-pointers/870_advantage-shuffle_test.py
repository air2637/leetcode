
# https://leetcode.cn/problems/advantage-shuffle/


from collections import deque
from typing import List
import unittest
from parameterized import parameterized

class Solution():

    # def findNumBarelyGreaterThan(self, target, nums):
        
    #     def binarySearch(start, end):
    #         # print(f"begin with start {start}, end {end}")
    #         if start >= end:
    #             # print(f"final stage with start {start}, end {end}")
    #             if nums[start] > target:
    #                 return start
    #             return start + 1
    #         mid = start + (end - start)//2
    #         if nums[mid] > target:
    #             end = mid - 1
    #         elif nums[mid] <= target:
    #             start = mid + 1
    #         return binarySearch(start, end)

    #     # print(f"binary search {target}, in {nums}") 
    #     res_index = binarySearch(0, len(nums) - 1)
    #     return nums[0] if res_index >= len(nums) else nums[res_index]

    # def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # print()
    #     res = []
    #     nums1.sort()
    #     for i in nums2:
    #         r = self.findNumBarelyGreaterThan(i, nums1)
    #         # print(f"appending {r}")
    #         res.append(r)
    #         nums1.remove(r)
    #     return res

    def binarySearch(self, sorted, target):
        left , right = 0, len(sorted) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if sorted[mid] > target:
                # boundary inclusive as we need to find the value greater than target
                right = mid
            else:
                # assign right / left with mid value ensures left will never exceeds right
                left = mid
        if sorted[left] > target:
            return left
        if sorted[right] > target:
            return right
        return -1

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        res = []
        for n in nums2:
            indexMinNumGreater = self.binarySearch(nums1, n)
            toAppendAndRemove = 0 if indexMinNumGreater < 0 else indexMinNumGreater
            res.append(nums1[indexMinNumGreater])
            nums1.remove(nums1[indexMinNumGreater])
        return res

    # def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # need to reserve the postions of nums, but still need to get the sense of ordering of the nums
    #     ordered_nums2_indexs = sorted(range(len(nums2)), key=lambda i: nums2[i])
    #     # print(f"ordered indexs are {ordered_nums2_indexs}")
    #     nums1.sort()
    #     cur_nums2_min_index, cur_nums2_max_index = 0, len(nums2) - 1
    #     res = [0] * len(nums2)
    #     winCount = 0
    #     for n in nums1:
    #         # print(f"assigning {n}, by comparing with {nums2[ordered_nums2_indexs[cur_nums2_min_index]]} @ {ordered_nums2_indexs[cur_nums2_min_index]}")
    #         if n <= nums2[ordered_nums2_indexs[cur_nums2_min_index]]:
    #             # print(f"assinged to max of nums2 @ {ordered_nums2_indexs[cur_nums2_max_index]}")
    #             res[ordered_nums2_indexs[cur_nums2_max_index]] = n
    #             cur_nums2_max_index -= 1
    #         else:
    #             # print(f"assiged to min of nums2 @ {ordered_nums2_indexs[cur_nums2_min_index]}")
    #             res[ordered_nums2_indexs[cur_nums2_min_index]] = n
    #             cur_nums2_min_index += 1
    #             winCount += 1
    #         # print(f"now the res {res}, wins {winCount}\n")
    #     return res

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        (17, [1,11,16,18], 18),
        (17, [1,11,17,18,19], 18),
        (2, [1,11,17,18,19], 11),
        (2, [3,11,17,18,19], 3),
        (21, [3,11,17,18,19], 3),
        (13, [8,12,24,32], 24),
        (4, [4, 4, 4, 5, 6, 6, 7], 5),
    ]) 
    def test_findNumBarelyGreaterThan(self, target, nums, expected):
        actual = self.solution.findNumBarelyGreaterThan(target, nums)
        self.assertEqual(actual, expected)

    @parameterized.expand([
        (17, [1,11,16,18], 18),
        (17, [1,11,17,18,19], 18),
        (2, [1,11,17,18,19], 11),
        (2, [3,11,17,18,19], 3),
        (21, [3,11,17,18,19], 3),
        (13, [8,12,24,32], 24),
        (4, [4, 4, 4, 5, 6, 6, 7], 5),
    ]) 
    def test_binarySearch(self, target, nums, expected):
        firstIndexGreater = self.solution.binarySearch(nums, target)
        self.assertEqual(nums[0] if firstIndexGreater < 0 else nums[firstIndexGreater], expected)


    @parameterized.expand([
        ([2,7,11,15], [1,10,4,11], [2,11,7,15]),
        ([12,24,8,32], [13,25,32,11], [24,32,8,12]),
        ([8,2,4,4,5,6,6,0,4,7],[0,8,7,4,4,2,8,5,2,0],[2, 7, 8, 5, 6, 4, 0, 6, 4, 4])
    ])
    def test_advantageCount(self, nums1, nums2, expected):
        print()
        actual = self.solution.advantageCount(nums1, nums2)
        self.assertListEqual(actual, expected)