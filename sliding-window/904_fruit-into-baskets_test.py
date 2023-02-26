# https://leetcode.cn/problems/fruit-into-baskets/

from typing import List
import unittest
from parameterized import parameterized

class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        fruit_basket = {}
        pointer_remove_fruit, pointer_add_fruit = 0, 0
        fruit_counter = 0
        max_fruits = 0
        while pointer_add_fruit < len(fruits):
            if fruits[pointer_add_fruit] in fruit_basket \
                or len(fruit_basket) < 2:
                # print(f"adding {fruits[pointer_add_fruit]}")
                if fruits[pointer_add_fruit] not in fruit_basket:
                    fruit_basket[fruits[pointer_add_fruit]] = 1
                else:
                    fruit_basket[fruits[pointer_add_fruit]] += 1
                fruit_counter += 1
                pointer_add_fruit += 1
                max_fruits = max(max_fruits, fruit_counter)
            else:
                while True:
                    print(f"removing fruit {fruits[pointer_remove_fruit]}")
                    fruit_basket[fruits[pointer_remove_fruit]] -= 1
                    fruit_counter -= 1
                    if fruit_basket[fruits[pointer_remove_fruit]] == 0:
                        # print(f"fruit {fruits[pointer_remove_fruit]} is permanently removed")
                        fruit_basket.pop(fruits[pointer_remove_fruit])
                        pointer_remove_fruit += 1
                        break
                    pointer_remove_fruit += 1
        return max_fruits
    
class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    @parameterized.expand([
        ([1,2,1], 3),
        ([0,1,2,2], 3),
        ([1,2,3,2,2],4),
        ([3,3,3,1,2,1,1,2,3,3,4],5)
    ])
    def test_totalFruit(self, fruits, expected):
        print()
        actual = self.solution.totalFruit(fruits)
        self.assertEqual(actual, expected)
                