import unittest
import re
from parameterized import parameterized

# https://leetcode.cn/problems/valid-palindrome/

class Solution:

    def isPalindromeWithRegex(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        p1, p2 = 0, len(s)-1
        while(p1 < p2):
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True

    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1
        while(p1 < p2):
            while not s[p1].isalnum() and p1 < p2:
                p1 += 1
            while not s[p2].isalnum() and p1 < p2:
                p2 -= 1
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True



class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome(self):
        s = "amanaplanacanalpanama"
        self.assertTrue(self.solution.isPalindrome(s))
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.solution.isPalindrome(s))
        s = "race a car"
        self.assertFalse(self.solution.isPalindrome(s))
        s = " "
        self.assertTrue(self.solution.isPalindrome(s))
        s = "0P"
        self.assertFalse(self.solution.isPalindrome(s))

    @parameterized.expand([
        ("amanaplanacanalpanama", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
    ])
    def test_isPalindromeWithRegex(self, s, expected):
        self.assertEqual(expected, self.solution.isPalindromeWithRegex(s))