


# https://leetcode.cn/problems/reverse-words-in-a-string/




import unittest
from parameterized import parameterized

class Solution():

    def reverseWords2(self, s: str) -> str:
        return " ".join(s.split()[::-1])

    def reverseWords(self, s: str) -> str:
        words_without_space = []
        words = s.strip().split()
        i, j = 0, len(words) - 1
        while j > i:
            if words[i] == '':
                i += 1
                continue
            if words[j] == '':
                j -= 1
                continue
            if j <= i:
                break
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        return ' '.join(words)


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ('the sky is blue', 'blue is sky the'),
        ('  hello world  ', 'world hello'),
        ("a good   example", "example good a")
    ])
    def test_reverseWords(self, words, expected):
        actual = self.solution.reverseWords(words)
        self.assertEqual(actual, expected)
