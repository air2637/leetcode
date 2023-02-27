# https://leetcode.cn/problems/find-all-anagrams-in-a-string/


from collections import Counter
from typing import List
import unittest
from parameterized import parameterized

class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        two pointers - left, right
        if s[right] not a needed char in p:
            left = right + 1
        if registrar > len(p):
            remove s[left] from regisrar 
        if registrar is fulfilled:
            remove s[left] from registrar
            record the s[left] in res
        if s[right] a needed char in p:
           update the registrar
        right += 1
        """

        left , right = 0, 0
        registrar = {}
        checker = Counter(p)
        char_cnt = 0
        res = []

        def addToRegistrar(ch):
            if ch in registrar:
                registrar[ch] += 1
            else:
                registrar[ch] = 1

        def checkRegistrar():
            for k, v in registrar.items():
                if checker[k] != v:
                    return False
            # total length same, and meet each count for each char
            return True

        for right, c in enumerate(s):
            # right pointed to a non pattern char, break from left
            if c not in p:
                left = right + 1
                char_cnt = 0
                registrar = {}
                continue
            addToRegistrar(c)
            char_cnt += 1
            if len(p) == char_cnt:
                if checkRegistrar():
                    # fully matched
                    res.append(left)
                registrar[s[left]] -= 1
                left += 1
                char_cnt -= 1
        return res

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("cbaebabacd", "abc", [0,6]),
        ("abab", "ab", [0,1,2]),
    ])
    def test_findAnagrams(self, s, p, expected):
        actual = self.solution.findAnagrams(s, p)
        self.assertListEqual(actual, expected)
