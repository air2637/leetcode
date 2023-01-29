# Reflectin for Two-pointers questions

## 3Sum

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

