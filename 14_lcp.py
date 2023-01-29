#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        v1 = strs[0]
        longestCommonPrefix = ""
        for i in range(len(v1)):
            charToCheck = v1[i]
            
            for s in strs[1:]:
                if i >= len(s):
                    return longestCommonPrefix
                if s[i] != charToCheck:
                    return longestCommonPrefix
            longestCommonPrefix += charToCheck
        return longestCommonPrefix

    def findLCPOfTwo(self, str1: str, str2: str) -> str:
        lcp = ""
        print(f"str1 {str1}, and str2 {str2}")
        for i in range(len(str1)):
            if i > len(str2) - 1:
                return lcp
            if str1[i] == str2[i]:
                lcp += str1[i]
            else:
                return lcp
        return lcp

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        longestCommonPrefix = strs[0]
        for i in range(len(strs)):
            longestCommonPrefix = self.findLCPOfTwo(longestCommonPrefix, strs[i])

        return longestCommonPrefix

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_(self):
        self.assertEqual("a", self.solution.longestCommonPrefix2(["a", "ab"]))
        self.assertEqual("ab", self.solution.longestCommonPrefix2(["ab", "abcd", "abc"]))
        self.assertEqual("", self.solution.longestCommonPrefix2(["ab", "d", "c"]))

# @lc code=end

