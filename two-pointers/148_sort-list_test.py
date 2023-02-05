

# https://leetcode.cn/problems/sort-list/

"""
Merge Sort a linked list
divide and conquer:
find the mid of the linked list with slow-fast pointer
cut the linked list into half
keep doing this splitting until it is just single node
start merging node bwteen two in order

Time complexity O(NlogN)
Space complexity O(logN) # TODO: why??
"""


from typing import List, Optional
import unittest
from parameterized import parameterized

class ListNode():

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:


    def doMerge(self, left: List[int], right: List[int]) -> List[int]:
        p_left, p_right = 0, 0
        sorted_list = []
        while p_left < len(left) and p_right < len(right):
            if left[p_left] <= right[p_right]:
                sorted_list.append(left[p_left])
                p_left += 1
            else:
                sorted_list.append(right[p_right])
                p_right += 1
        if p_left < len(left):
            sorted_list.extend(left[p_left:])
        else:
            sorted_list.extend(right[p_right:])
        return sorted_list

    def doSplitMerge(self, curHeadNode: ListNode) -> List[int]:
        if curHeadNode.next == None:
            return [curHeadNode.val]
        slowPointer , fastPointer = curHeadNode, curHeadNode.next
        while fastPointer != None and fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next # TODO: check none?
        # now the slowPointer should be at the mid position, do splitting
        headForRightHalf = slowPointer.next
        slowPointer.next = None
        print(f"left head {curHeadNode.val}, right head {headForRightHalf.val}")
        leftHalf = self.doSplitMerge(curHeadNode) # split for the left half
        rightHalf = self.doSplitMerge(headForRightHalf) # split for the right half ,TODO: could be None?
        sortedNodes = self.doMerge(leftHalf, rightHalf) # TODO: the doMerge should return list data type?
        return sortedNodes
    
    def buildListNode(self, vals: List[int]) -> ListNode:
        head = temp = ListNode()
        for i in vals:
            temp.next = ListNode(i)
            temp = temp.next
        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_vals = []
        if head != None:
            print(f"begins with head {head.val}")
            sorted_vals = self.doSplitMerge(head)
        print(sorted_vals)
        return self.buildListNode(sorted_vals)
        

class TestSolution():

    def setUp(self) -> None:
        self.solution = Solution()

    def buildListNode(self, vals: List[int]) -> ListNode:
        head = temp = ListNode()
        for i in vals:
            temp.next = ListNode(i)
            temp = temp.next
        return head.next

    def convertToList(self, head: ListNode) -> List[int]:
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        return result
        
    @parameterized.expand([
        ([1,2], [3,4], [1,2,3,4])
    ])
    def test_doMerge(self, list1, list2, expected):
        outcome = self.solution.doMerge(list1, list2)
        self.assertListEqual(expected, outcome)

    @parameterized.expand([
        ([4,2,1,3], (1,2,3,4))
    ])
    def test_sortList(self, unsortd, expected):
        head = self.solution.buildListNode(unsortd)
        head = self.solution.sortList(head)
        actual = self.convertToList(head)
        self.assertTupleEqual(expected, tuple(actual))