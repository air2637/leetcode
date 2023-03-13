# https://leetcode.cn/problems/replace-the-substring-for-balanced-string/

from collections import Counter, defaultdict
import unittest
from parameterized import parameterized

class Solution:


    def balancedString(self, s: str) -> int:
        char_freq = Counter(s)
        unique_chars = set(char_freq)
        average_cnt = len(s) / 4
        to_search = { x: (char_freq[x] - average_cnt) for x in unique_chars if char_freq[x]> average_cnt}
        # print(f"to search {to_search}")
        if not to_search:
            return 0
        # "WWEQERQWQWWRWWERQWEQ"
        recorded = defaultdict(int)
        left = right = 0
        min_length = len(s)
        while right < len(s):
            recorded , notFulfilled = self.notFulfillSearch(s[right], True, to_search, recorded)
            if notFulfilled: 
                right += 1
                continue
            # print(f"fulfilled string is {s[left: right + 1]}, with left = {left}, right = {right}")
            min_length = min(min_length, right - left + 1)
            left += 1
            recorded, notFulfilled = self.notFulfillSearch(s[left-1], False, to_search, recorded)
            while not notFulfilled: 
                # print(f"2-fulfilled string is {s[left: right + 1]}, with left = {left}, right = {right}")
                min_length = min(min_length, right - left + 1)
                left += 1
                recorded, notFulfilled = self.notFulfillSearch(s[left-1], False, to_search, recorded)
            # print(f"breaking fulfilling, with left = {left}")
            right += 1
        return min_length
    
    def notFulfillSearch(self, ch: str, isAppend: bool, to_search: dict, recorded: dict) -> bool:
        fulfilled = True
        if isAppend:
            recorded[ch] += 1
        else:
            recorded[ch] -= 1
        for x in to_search:
            if recorded[x] < to_search[x]:
                fulfilled = False
                break
        return (recorded, not fulfilled)

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("WWEQERQWQWWRWWERQWEQ", 4),
        ("QWER", 0),
        ("QQWE", 1),
        ("QQQW", 2),
        ("QQQQ", 3),
        ("WQWRQQQW",3)
    ])
    def test_balancedString(self, s, expected):
        print()
        actual = self.solution.balancedString(s)
        self.assertEqual(actual, expected)



        