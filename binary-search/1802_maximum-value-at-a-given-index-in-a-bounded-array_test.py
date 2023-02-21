
#  https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/


import unittest
from parameterized import parameterized
from pytest import skip

class Solution:


    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        min_res , max_res = 1, maxSum
        res = 0
        while min_res <= max_res:
            mid_res = min_res + (max_res - min_res) // 2
            if self.testResInSeries(mid_res, index, n, maxSum):
                res = mid_res
                min_res = mid_res + 1
            else:
                max_res = mid_res - 1
        return res 
    

    def testResInSeries(self, maxVal: int, maxValIndex: int, totalLength: int, maxSum: int) -> bool:
        # print(f"testing with {maxVal}...")
        left_length = maxValIndex
        right_length = totalLength - (maxValIndex + 1)
        return maxVal + self.getTotalSum(max(maxVal - 1, 1), left_length) + self.getTotalSum(max(maxVal - 1, 1), right_length) <= maxSum
    
    def getTotalSum2(self, maxVal: int, totalLength: int) -> int:
        ''' we cannot infinitely decrement the element value,
        so need to make the element at position exceeding (maxVal - totalLength) be 1
        '''
        # print(f"getting total sum {maxVal}, {totalLength}")
        total = 0
        ones = (totalLength - maxVal) if totalLength > maxVal else 0
        while maxVal > 0 and totalLength > 0:
            total += maxVal
            maxVal -= 1
            totalLength -= 1
        # print(f"returning {total + ones}, with {maxVal}, {totalLength}\n")
        return total + ones

    def getTotalSum(self, maxVal: int, totalLength: int) -> int:
        if totalLength == 0:
            return 0
        if totalLength > maxVal:
            return (1 + maxVal) * maxVal // 2 + (totalLength - maxVal)
        return (maxVal - totalLength + 1 + maxVal) * totalLength // 2

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    # @parameterized.expand([
    #     (2, 0, 4, 4, False)
    # ])
    # def test_testResInSeries(self, maxVal, maxValIndx, totalLen, maxSum, expected):
    #     print()
    #     actual = self.solution.testResInSeries(maxVal, maxValIndx, totalLen, maxSum)
    #     self.assertEqual(actual, expected)

    @parameterized.expand([
        (4, 0, 4, 1)
    ])
    def test_maxValue(self, n, index, maxSum, expected):
        print()
        actual = self.solution.maxValue(n, index, maxSum)
        self.assertEqual(actual, expected)