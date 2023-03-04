# https://leetcode.cn/problems/longest-repeating-character-replacement/

from collections import Counter
import unittest
from parameterized import parameterized

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        left, right = 0, 0
        max_length = 0
        main_ch_count = 0
        while right < len(s):
            freq[s[right]] += 1
            # only when the ch's frequency within the window reaches new 'highest score', we can continue expand the window width
            main_ch_count = max(main_ch_count, freq[s[right]])
            if right - left + 1 > main_ch_count + k:
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

    def characterReplacement2(self, s: str, k: int) -> int:
        unique_chars = set(s)
        max_lenth = 0
        for ch in unique_chars:
            left, right = 0, 0
            quota = k
            char_index_replaced = set()
            while right < len(s):
                if s[right] != ch:
                    if quota > 0:
                        char_index_replaced.add(right)
                        quota -= 1
                    else:
                        max_lenth = max(max_lenth, right - left)
                        if k == 0:
                            right += 1
                            left = right
                            continue
                        while left not in char_index_replaced:
                            left += 1
                        char_index_replaced.remove(left)
                        left += 1
                        quota += 1
                        continue
                right += 1
            max_lenth = max(max_lenth, right - left)
        return max_lenth





class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ('ABAB', 2, 4),
        ('AABABBA',1,4),
        ('AAAB', 0, 3)
    ])
    def test_characterReplacement(self, s, k, expected):
        actual = self.solution.characterReplacement(s, k)
        self.assertEqual(actual, expected)