



from typing import List
import unittest


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        """The func returns the pivot index where the sum of values on its left side
        equals to the sum of values on its right side

        pseudo code:
        find the sum of the values in the list
        iterate from left to right
           if the cumulative sum of values on the left of current index is not equal to the half of the total - value of current index
              add the index by 1
           else
              return the index
        return -1

        Args:
            nums (List[int]): the set of numbers to check

        Returns:
            int: the index wanted
        """

        total = sum(nums)
        cum = 0
        for i in range(len(nums)):
            expected = total - nums[i]
            if cum * 2 == expected:
                return i
            cum += nums[i]
        return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        """ To find target value index in the given nums list

        pseudo code:
        Find the mid index of current searched range
        if value of mid_index == target value:
            return current mid_index
        if the value at mid_index > target value:
            set the upper boundary index to mid_index - 1
        else the value at mid_index < target value:
            set the lower boundary index to mid_index + 1
        if lower boundary index >= upper boundary index:
            return max(lower boundary index, 0)

        Args:
            nums (List[int]): input list
            target (int): value to be searched/inserted

        Returns:
            int: index where the target value should be inserted
        """

        lower = 0
        upper = len(nums) - 1
        while True:
            mid = lower + (upper - lower) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
            
            if lower > upper:
                return lower if (lower >= len(nums)) or nums[lower] > target else lower + 1 

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @unittest.skip
    def test_pivotIndex(self):
        # https://leetcode.cn/leetbook/read/array-and-string/yf47s/
        self.assertEqual(2, self.solution.pivotIndex([1,2,3,2,1])) 

    def test_searchInsert(self):
        # https://leetcode.cn/leetbook/read/array-and-string/cxqdh/
        self.assertEqual(2, self.solution.searchInsert([1,3,5,6], 5))
        self.assertEqual(1, self.solution.searchInsert([1,3,5,6], 2))
        self.assertEqual(4, self.solution.searchInsert([1,3,5,6], 7))
        self.assertEqual(0, self.solution.searchInsert([1,3,5,6], 0))
        self.assertEqual(1, self.solution.searchInsert([1], 2))
        self.assertEqual(0, self.solution.searchInsert([1], 0))
        self.assertEqual(1, self.solution.searchInsert([1,3], 3))

if __name__ == '__main__':
    unittest.main()
        


