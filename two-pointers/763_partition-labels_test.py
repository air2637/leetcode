
# https://leetcode.cn/problems/partition-labels/

from typing import List
import unittest
from parameterized import parameterized

class CharBoundary():

    def __init__(self, val, left=-1, right=-1) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return self.val
        
    
class Solution():

    # def partitionLabels(self, s: str) -> List[int]:
    #     charDict = dict()
    #     for i, c in enumerate(s):
    #         if c in charDict:
    #             charDict[c].right = i
    #         else:
    #             charDict[c] = CharBoundary(c, i, i)
    #     # sort the CharBoundary objects by their left boundary in ascending order
    #     charDictList = charDict.values()
    #     sorted(charDictList, key=lambda cd: cd.left)
    #     group_count = 0
    #     current_right = 0
    #     pre_end = -1
    #     res = []
    #     for ele in charDictList:
    #         if ele.left <= current_right:
    #             current_right = max(current_right, ele.right) 
    #         else:
    #             res.append(current_right - pre_end)
    #             pre_end = current_right
    #             current_right = ele.right 
    #             group_count += 1
    #     res.append(current_right - pre_end)
    #     return res
    
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = dict()
        for i, c in enumerate(s):
            char_dict[c] = i
        local_max_index = -1
        pre_i = -1
        res = []
        for i, c in enumerate(s):
            if local_max_index == i:
                print(f"i at {i}, with {c}")
                res.append(i-pre_i)
                local_max_index = -1
                pre_i = i
            elif char_dict[c] > local_max_index:
                local_max_index = char_dict[c]
        return res


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("ababcbacadefegdehijhklij", [9,7,8]),
        ("eccbbbbdec", [10])
    ])
    def test_partitionLabels(self, s, expected):
        print()
        actual = self.solution.partitionLabels(s)
        self.assertListEqual(actual, expected)