from typing import List
import unittest
from parameterized import parameterized

# https://leetcode.cn/problems/container-with-most-water/



"""
two pointers, points to the start and end of the list
while start < end
    calculate the area and compare with the current max
    find the shorter bar, as no point to keep the shorter one unchanged but shift the longer one because it only make the whole area even less with shorter in length, so:
    shift the pointer of the shorter one to its next (if the height equals, shift any of the two would do)

"""


class Solution:

    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1
        max_area = 0
        while p1 < p2:
            cur_area = (p2 - p1) * min(height[p2], height[p1])
            max_area = max(max_area, cur_area)
            print(f"p1 is {p1}, p2 is {p2}, and max_area is {max_area}")
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return max_area

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,8,6,2,5,4,8,3,7], 49)
    ])
    def test_maxArea(self, height, expected):
        self.assertEqual(expected, self.solution.maxArea(height)) 