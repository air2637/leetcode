
# https://leetcode.cn/problems/reach-a-number/



class Solution():

    def reachNumber(self, target:int) -> int:
        target = abs(target)
        cur_sum = 0
        counter = 0
        while cur_sum < target:
            counter += 1
            cur_sum += counter 
        if (cur_sum - target) % 2 == 0:
            return counter
        if ((cur_sum + counter + 1) - target) % 2 == 0:
            return counter + 1
        return counter + 2
