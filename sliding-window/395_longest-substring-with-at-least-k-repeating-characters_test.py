# https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/

from collections import Counter
import unittest
from parameterized import parameterized

class Solution:


    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        char_count = Counter(s)
        for ch_idx in range(len(s)):
            if char_count[s[ch_idx]] < k:
                left = self.longestSubstring(s[0:ch_idx], k)
                right = self.longestSubstring(s[ch_idx+1:], k)
                return max(left, right)
        return len(s)

    def longestSubstring_NOT_WORKING(self, s: str, k: int) -> int:
        """The function returns the longest substring in which each character occurs at least k times.
        Loop through the characters in s, so we can get a list of characters and their respective occurance times in s.
        Two pointers: left, right 
        if the right points to a character having occurance value less than k:
            record the right - left + 1, against the current max_len
            set left to right + 1
        else:
            move right one more unit: right += 1
        keep above while right not reaching the last character
        Args:
            s (str): string to loopthrough
            k (int): minimum times that occurance required

        Returns:
            int: longest substring length
        """
        char_cnt = Counter(s)
        current_cnt = Counter()
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            current_cnt[s[right]] += 1
            is_qualified = True
            for ele, cnt in current_cnt.items():
                if cnt < k:
                    is_qualified = False
                    break
            if is_qualified:
                max_len = max(max_len, right - left + 1)
                is_qualified = False
            # the current right pointed element won't be able to meet the k occurance at all, give up current accumulated
            if char_cnt[s[right]] < k:
                left = right + 1
                current_cnt = Counter()
            right += 1
        return max_len
                
class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("aaabb", 3, 3),
        ("ababbc",2, 5),
        ("ababacb",3,0),
        ("bbaaacbd",3, 3)
    ])
    def test_longestSubstring(self, s, k, expected):
        actual = self.solution.longestSubstring(s, k)
        self.assertEqual(actual, expected)