# Reflectin for Two-pointers questions

## Questions attempted
1. [15_Sum](#15_3sum)
1. [870_advantage-suffle](#870_advantage-shuffle)

## 15_3Sum

Two challenges are there:
1. To convert the question to Two-pointers questions:

    The questions can be thought as fixing the first index and find the remaining 2 pointers that fulfill the target sum.

2. To understand the logic of removing duplicate result set:

    For 1st index p1, need to skip if `nums[p1] == nums[p1-1]`, as it means the same value has been processed before as the 1st value of the candidate result set.

    For 2nd index p2, 3rd index p3, need to skip if `nums[p2] == nums[p2+1]`. Noticing here we are comparing the current index value against the value of its next index, this is because we want to standardise the action of 
    ```
    p2 += 1
    p3 -= 1
    ```
    no matter whether there is a equivalent value in adjacent or not, we both need to shift the index for one more place left/right. (We need further check if we do `nums[p2] == nums[p2-1]`, as we should not shift the p2 anymore once breaking out from the `while` loop)

    In addition, we add the result set upon its first occourance, to be working together with `nums[p2] == nums[p2+1]`:

    ```python
    the_result.append([nums[p1], nums[p2], nums[p3]])
    ``` 


## 870_advantage-shuffle

Two apporaches:
1. For each number in nums2, find the minimum number in nums1 that is greater than the value.

    - iterate over nums2
    - binary search in nums1
        - boundary indices are inclusive, e.g. `left = mid`
        - loop rather than recursive call, e.g. `while left + 1 < right`
    - if no satisfied value, return the minimum number

2. Assign minimum number in num1 that can be greater than the minimum number in num2.

    - get the order of values in nums2 without modifying their position, e.g. `sorted(range(n), lambda i: nums2[i])` 
    - sort nums1
    - iterate over nums1
        - if the current iterated nums1 is greater that the current minimum nums2, assign; 
        - else assign it to the biggest value of nums2
