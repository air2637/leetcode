



import queue
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
        
    def searchInsertStandardAns(self, nums: List[int], target: int) -> int:

        lower, upper, ans = 0, len(nums) - 1, len(nums)
        while (lower <= upper):
            mid = lower + (upper - lower) // 2
            if nums[mid] >= target:
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return ans

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ What is the condition fulfilling a overlap between 2 intervals?

        interval A: [a1, a2]
        interval B: [b1, b2]
        
            a1           a2
            |------------|
                b1             b2
                |--------------|
                b1     b2
                |-------|
        b1          b2
        |------------|
        b1                      b2
        |------------------------|


        sort the intervals based on their index 0 value in ascending order

        create a temporary interval variable, e.g. temp = intervals[0]

        for interval from index 1 onwards:
            if there is overlap between interval iterated and temp:
                update the temp boundary
            else:
                insert the temp into result interval
                set temp to interval iterated

        add the temp into result interval

        Args:
            intervals (List[List[int]]): assuming it is an set of unordered intervals

        Returns:
            List[List[int]]: a set of intervals with on overlap
        """
        
        intervals = self.sortIntervalBasedonIndexZero(intervals)
        temp = intervals[0].copy()
        result = list()
        for iterv in intervals[1:]:
            if temp[1] >= iterv[0]:
                temp[1] = max(temp[1], iterv[1])
            else:
                result.append(temp)
                temp = iterv
        result.append(temp)
        return result


    def sortIntervalBasedonIndexZero(self, intervals:List[List[int]]) -> List[List[int]]:
        sorted = list()
        sorted.append(intervals[0])
        for to_insert in intervals[1:]:
            sorted.append(to_insert)
            for i in range(len(sorted)-2 , -1 , -1):
                if to_insert[0] <= sorted[i][0]:
                    sorted[i+1] = sorted[i]
                    sorted[i] = to_insert
                else:
                    sorted[i+1] = to_insert
                    break
        return sorted


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @unittest.skip
    def test_pivotIndex(self):
        # https://leetcode.cn/leetbook/read/array-and-string/yf47s/
        self.assertEqual(2, self.solution.pivotIndex([1,2,3,2,1])) 

    @unittest.skip
    def test_searchInsert(self):
        # https://leetcode.cn/leetbook/read/array-and-string/cxqdh/
        self.assertEqual(2, self.solution.searchInsertStandardAns([1,3,5,6], 5))
        self.assertEqual(1, self.solution.searchInsertStandardAns([1,3,5,6], 2))
        self.assertEqual(4, self.solution.searchInsertStandardAns([1,3,5,6], 7))
        self.assertEqual(0, self.solution.searchInsertStandardAns([1,3,5,6], 0))
        self.assertEqual(1, self.solution.searchInsertStandardAns([1], 2))
        self.assertEqual(0, self.solution.searchInsertStandardAns([1], 0))
        self.assertEqual(1, self.solution.searchInsertStandardAns([1,3], 3))

    # @unittest.skip
    def test_sortIntervalBasedonIndexZero(self):
        # unsorted = [[1,3],[2,6],[8,10],[15,18]]
        # result = self.solution.sortIntervalBasedonIndexZero(unsorted)
        # expected = [[1,3],[2,6],[8,10],[15,18]]
        # self.assertEqual(expected, result)

        # unsorted = [[1,3],[8,10],[15,18],[2,6]]
        # result = self.solution.sortIntervalBasedonIndexZero(unsorted)
        # expected = [[1,3],[2,6],[8,10],[15,18]]
        # self.assertEqual(expected, result)

        unsorted = [[1,3],[1,4]]
        result = self.solution.sortIntervalBasedonIndexZero(unsorted)
        expected = [[1,4],[1,3]]
        self.assertEqual(expected, result)

    # @unittest.skip
    def test_merge(self):
        # https://leetcode.cn/leetbook/read/array-and-string/c5tv3/
        # input = [[1,3],[2,6],[8,10],[15,18]]
        # expected = [[1,6],[8,10],[15,18]]
        # self.assertEqual(expected, self.solution.merge(input))

        input = [[1,4],[1,5]]
        expected = [[1,5]]
        self.assertEqual(expected, self.solution.merge(input))


if __name__ == '__main__':
    unittest.main()
        


