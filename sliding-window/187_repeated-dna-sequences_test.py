# https://leetcode.cn/problems/repeated-dna-sequences/

from collections import defaultdict, deque
from typing import List
import unittest
from parameterized import parameterized

class Solution:

    L = 10
    bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= Solution.L:
            return []
        ans = []
        x = 0
        for ch in s[:Solution.L - 1]:
            x = (x << 2) | Solution.bin[ch]
        cnt = defaultdict(int)
        for i in range(n - Solution.L + 1):
            x = ((x << 2) | Solution.bin[s[i + Solution.L - 1]]) & ((1 << (Solution.L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + Solution.L])
        return ans

        # n = len(s)
        # if n <= Solution.L:
        #     return []
        # ans = []
        # x = 0
        # # get 1st 10 chars
        # for ch in s[:Solution.L-1]:
        #     x = (x << 2) | bin[ch]
        # cnt = defaultdict(int)
        # for i in range(n - Solution.L + 1):
        #    x = (x << 2) | bin[s[i + Solution.L - 1]] & (1 << 2 * Solution.L - 1)
        #    cnt[x] += 1
        #    if cnt[x] == 2:
        #        ans.append(s[i: i + Solution.L])
        # return ans

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        left, right = 0, 0
        char_list = deque()
        sequence_list = set()
        res = set()
        while right < len(s):
            if right - left < 9:
                char_list.append(s[right])
                right += 1
                continue
            char_list.append(s[right])
            cur_seq = "".join(char_list)
            if cur_seq not in sequence_list:
                sequence_list.add(cur_seq)
            elif cur_seq not in res:
                res.add(cur_seq)
            char_list.popleft()
            right += 1
        return list(res)

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", {"AAAAACCCCC","CCCCCAAAAA"})
    ]) 
    def test_findRepeatedDnaSequences(self, s, expected):
        actual = self.solution.findRepeatedDnaSequences(s)
        self.assertSetEqual(set(actual), expected)

    


