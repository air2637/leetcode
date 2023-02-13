# Reflectin for Two-pointers questions

## Questions attempted
1. [15_Sum](#15_3sum)
1. [870_advantage-suffle](#870_advantage-shuffle)

## 11_container-with-most-water

Question is to find the max area between 2 bars that can be formed in a given list of bar heights.

```python
Two pointers set to the beginning and end of the list, say left, right
While left < right:
    find the area = (right - left) * min(left, right)
    update the max area if current area is bigger
    shift the pointer that at shorter height to one index inward (As no point shifting the longer one since the shorter one is the current bottleneck) 
return the max area
```


## 15_3Sum / 18_4Sum

1. To convert the question to Two-pointers questions:

    The questions can be thought as fixing the first index and find the remaining 2 pointers that fulfill the target sum.

2. To understand the logic of removing duplicate result set:

    When iterating the value for same position (e.g. 2nd number), we need `if i > start and nums[i] == nums[i-1]` to remove the duplicate value as the candicate for **same** position
```python
recursive_N_sum(4, 0, len(nums) - 3, N)
# note the end_pos is exclusive, hence the max value for 1st postion can be taken up to index len(nums) - 4
```
```python
sort nums
per_combo = []
res = []
recursive_N_sum(k , start_pos, end_pos, target):
        if k != 2:
            # not base range - last 2 postions
            for i in nums[start_pos:end_pos]:
                if i > start and nums[i] == nums[i-1]:
                    # to skip the same value as previous for same position
                    continue
                per_combo.append(i)
                recursive_N_sum(k-1, start_pos + 1, end_pos + 1, target)
                per_combo.pop()
        else:
            left , right = start_pos, end_pos
            while left < right:
                if target < sum (per_combo , nums[left], nums[right]):
                    left += 1
                elif target > sum (per_combo , nums[left], nums[right]):
                    right -= 1
                else:
                    res.append(per_combo , nums[left], nums[right])
                    while nums[left] == nums[left + 1]:
                        # avoid the duplicate in 2nd last postion of the per_combo
                        left += 1
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
