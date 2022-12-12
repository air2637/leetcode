



from collections import deque
import queue
from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """ Pseudo Code:

        Create a queue with (lower, upper, parent_node, is_left_node) as an element

        while queue is not empty:
            1. poll from queue
            2. get the median of the range lower->upper
            3. assign the median value to parent_node, based on the direction flag is_left_node
            4. queue up (lower, median - 1, median_node, is_left_node=true), if median - 1 >= lower
            5. queue up (median + 1, upper, median_node, is_left_node=false), if upper >= median + 1

        Args:
            nums (List[int]): ordered list

        Returns:
            Optional[TreeNode]: Top node in BST
        """

        q = deque()
        q.append((0, len(nums)-1, None, False))
        top_node = None
        while q:
            ele = q.popleft()
            lower, upper, parent_node, is_left = ele[0], ele[1], ele[2], ele[3]
            median_index = lower + (upper-lower)//2
            median = nums[median_index]
            median_node = TreeNode(median)
            if not parent_node:
                top_node = median_node
            elif is_left:
                parent_node.left = median_node
            else:
                parent_node.right = median_node

            if median_index - 1 >= lower:
                q.append((lower, median_index -1, median_node, True))
            if upper >= median_index + 1:
                q.append((median_index + 1, upper, median_node, False))
        return top_node

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_(self):
        # https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
        pass

if __name__ == '__main__':
    unittest.main()
        


