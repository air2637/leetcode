# https://leetcode.cn/problems/split-two-strings-to-make-palindrome/

import unittest
from parameterized import parameterized

class Solution:

    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def doSelfPalindromeCheck(s0: str, start: int, end: int):
            while start < end and s0[start] == s0[end]:
                start += 1
                end -= 1
            return start >= end

        def doCheckS1PrefixAgainstS2SuffixForPalindrome(s1: str, s2: str):
            s1_idx = 0
            s2_idx = len(s2) - 1
            while s1_idx < len(s1) and s2_idx < len(s2) and s1[s1_idx] == s2[s2_idx]:
                s1_idx += 1
                s2_idx -= 1
            # still need to check if Self-palindrome between [s1_idx, s2_idx]            
            return doSelfPalindromeCheck(s1, s1_idx, s2_idx) or \
                  doSelfPalindromeCheck(s2, s1_idx, s2_idx)

        return doCheckS1PrefixAgainstS2SuffixForPalindrome(a, b) or doCheckS1PrefixAgainstS2SuffixForPalindrome(b, a) 
    
class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("abdef", "fecab", True),
        ("ulacfd", "jizalu", True),
        ("x", "y", True),
        ("a", "a", True),
        ("fedbba", "acghef", False),
        ("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp", True)
    ])
    def test_checkPalindromeFormation(self, a, b, expected):
        actual = self.solution.checkPalindromeFormation(a, b)
        self.assertEqual(actual, expected)