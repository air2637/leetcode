
# https://leetcode.cn/problems/compare-version-numbers/




"""
split the version into list by delimiter '.'
compare each pair of str from v1, v2:
    convert the str to integer with ignoring the 0s in front of any significant number
    compare the converted integer
if any version has extra element:
    still equivalent if they only contains 0
else:
    it is surely bigger
"""

import unittest
from parameterized import parameterized

class Solution:

    def convertStrToInt(self, input: str) -> int:
        i = 0
        while i < len(input) and input[i] == '0':
            i += 1
        return int(input[i:]) if i < len(input) else 0

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = min(len(v1), len(v2)) 
        for i in range(n):
            k1 = self.convertStrToInt(v1[i])
            k2 = self.convertStrToInt(v2[i])
            if k1 != k2:
                return 1 if k1 > k2 else -1
        remaining = v1 if len(v1) > len(v2) else v2
        for i in remaining[n:]:
            if self.convertStrToInt(i) != 0:
                return 1 if len(v1) > len(v2) else -1
        return 0

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("001", 1),
        ("01", 1),
        ("00", 0),
    ])
    def test_convertStrToInt(self, input, expected):
        self.assertEqual(self.solution.convertStrToInt(input), expected)

    @parameterized.expand([
        ("1.01", "1.001", 0),
        ("1.0", "1.00.00", 0),
        ("0.1", "1.1", -1),
        ("1.1", "1.1", 0),
    ])
    def testCompareVersion(self, v1, v2, expected):
        actual = self.solution.compareVersion(v1, v2)
        self.assertEqual(actual, expected)