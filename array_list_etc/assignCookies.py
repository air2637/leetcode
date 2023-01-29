# https://leetcode.cn/problems/assign-cookies/

from typing import List
import unittest


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """ Pseudo Code:

        ideally, match kid with target amount same as the cookies' size?

        sort the target values in ascending order
        sort the cookie sizes in ascending order
        ans = 0
        while cookie_index not reaching the end:
            if  s[cookie_index] >= target[kid_index]:
                kid_index += 1
                cookie_index += 1
                ans += 1
            else:
                cookie_index += 1
        return ans

        Args:
            g (List[int]): target amount to fulfill
            s (List[int]): cookie sizes

        Returns:
            int: the Max number of target can be fulfilled
        """

        g.sort()
        s.sort()
        ans = 0
        cookie_idx = kid_idx = 0
        while cookie_idx < len(s) and kid_idx < len(g):
            if s[cookie_idx] >= g[kid_idx]:
                cookie_idx += 1
                kid_idx += 1
                ans += 1
            else:
                cookie_idx += 1
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_findContentChildren(self):
        g = [1,2,3]
        s = [2,3,4]
        self.assertEqual(3, self.solution.findContentChildren(g, s))

        g = [3,4,5]
        s = [2,3,4]
        self.assertEqual(2, self.solution.findContentChildren(g, s))

        g = [3,4,5]
        s = [1,5,5]
        self.assertEqual(2, self.solution.findContentChildren(g, s))

if __name__ == '__main__':
    unittest.main()