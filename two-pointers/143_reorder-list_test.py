

# https://leetcode.cn/problems/reorder-list/

"""
Solve the problem recursively
doLink(front, end) where front is the 1st node, end is a position following

"""

from typing import Optional
import unittest
from parameterized import parameterized

class ListNode():

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution():

    def getMid(self, start):
        slow , fast = start, start.next
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseFrom(self, b):
        a = None
        while b != None:
           c = b.next
           b.next = a
           a = b
           b = c
        return a
    
    def doMerge(self, h1, h2):
        dummy = current = ListNode()
        while h2 != None:
            current.next = h1
            # print(f"current is {current.val}, links to {h1.val}")
            current = current.next
            h1 = h1.next
            current.next = h2
            # print(f"current is {current.val}, links to {h2.val}")
            current = current.next
            h2 = h2.next
        if h1 != None:
            current.next = h1
        return dummy.next


    def doMerge2(self, n1, n2):
        res = n1
        while n2 != None:
            print(f"n1 {n1.val}, n2 {n2.val}")
            temp_n1 = n1.next
            n1.next = n2
            # print(f"n1 {n1.val} links to n2 {n2.val}")
            temp_n2 = n2.next
            n2.next = temp_n1 
            # print(f"n2 {n2.val} links to {temp_n1.val}")
            n1 = temp_n1
            n2 = temp_n2
        return res

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.getMid(head)
        reversed_head = self.reverseFrom(mid.next)
        mid.next = None
        head = self.doMerge2(head, reversed_head)

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def buildListNode(self, inputs):
        head = temp = ListNode()
        for i in inputs:
            temp.next = ListNode(i)
            temp = temp.next
        return head.next

    def serialize(self, head: ListNode):
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        return result

    @parameterized.expand([
        ([1,2,3,4,5], [1,5,2,4,3]),
        ([1,2,3,4], [1,4,2,3])
    ])
    def test_reorderList(self, inputs, expected):
        head = self.buildListNode(inputs)
        self.solution.reorderList(head)
        actual = self.serialize(head)
        self.assertListEqual(actual, expected)

    @parameterized.expand([
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2,3,4], [4,3,2,1]),
        ([1], [1])
    ])
    def test_reverseFrom(self, inputs, expected):
        head = self.buildListNode(inputs)
        head = self.solution.reverseFrom(head)
        actual = self.serialize(head)
        self.assertListEqual(actual, expected)

    @parameterized.expand([
        ([1,3,5], [2,4,6], [1,2,3,4,5,6]),
        ([1,3,5], [2,4], [1,2,3,4,5])
    ])
    def test_doMerge(self, l1, l2, expected):
        h1 = self.buildListNode(l1)
        h2 = self.buildListNode(l2)
        new_head = self.solution.doMerge(h1, h2)
        actual = self.serialize(new_head)
        self.assertListEqual(actual, expected)

    @parameterized.expand([
        ([1,3,5], [2,4,6], [1,2,3,4,5,6]),
        ([1,3,5], [2,4], [1,2,3,4,5])
    ])
    def test_doMerge2(self, l1, l2, expected):
        h1 = self.buildListNode(l1)
        h2 = self.buildListNode(l2)
        new_head = self.solution.doMerge2(h1, h2)
        actual = self.serialize(new_head)
        self.assertListEqual(actual, expected)