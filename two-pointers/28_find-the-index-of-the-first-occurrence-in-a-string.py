


# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/


import unittest
from parameterized import parameterized

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        p = 0
        i = 0
        res = -1
        matched_before = False
        while i < len(haystack):
            h = haystack[i]
            # print(f"haystack with i {i}, h {h}")
            if h == needle[p]:
                if p == 0:
                    matched_before = True
                    res = i
                # print(f"matched at p {p}, res is {res}")
                p += 1
            elif matched_before:
                i = res # point the haystack pointer back to the beginning
                p = 0
                matched_before = False
            # print(f"now p is {p}, and len needle is {len(needle)}")
            if p == len(needle):
                return res
            i += 1
        return -1
            

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
         ("sadbutsad", "sad", 0)
         ,("leetcode", "leeto", -1)
         ,("leetcodeto", "eto", 7)
        ,("aaa", "aaaa", -1)
        ,("mississippi", "issip", 4)
    ])
    def test_strStr(self, haystack, needle, expected):
        self.assertEqual(expected, self.solution.strStr(haystack, needle))