# https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/

from collections import deque
import unittest
from parameterized import parameterized


class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        def doAdd(arr, num):
            res = [0] * len(arr)
            for i, v in enumerate(arr):
                if i % 2 != 0:
                    res[i] = (v + num) % 10
                else:
                    res[i] = v
            return res
        
        def doRotate(arr, num):
            return arr[-num:] + arr[:-num]

        char_arr = list(s)
        int_arr = [int(c) for c in char_arr] 
        tracker = set()
        for_check = deque([int_arr]) 
        cur_minimum = None
        while len(for_check) > 0:
            cur_check = for_check.popleft()
            cur_str = ''.join([str(n) for n in cur_check])
            if cur_str not in tracker:
                tracker.add(cur_str)
                if not cur_minimum:
                    cur_minimum = cur_str
                cur_minimum = cur_str if cur_str < cur_minimum else cur_minimum
                res1 = doAdd(cur_check, a)
                if ''.join([str(n) for n in res1]) not in tracker:
                    for_check.append(res1)
                res2 = doRotate(cur_check,b)
                if ''.join([str(n) for n in res2]) not in tracker:
                    for_check.append(res2)
        return cur_minimum

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution() 

    @parameterized.expand([
        ("74", 5, 1, "24"),
        ("5525", 9, 2, "2050"),
        ("0011", 4, 2, "0011"),
        ("43987654", 7, 3, "00553311"),
    ])
    def test_findLexSmallestString(self, s, a, b, expected):
        actual = self.solution.findLexSmallestString(s, a, b)
        self.assertEqual(actual, expected)