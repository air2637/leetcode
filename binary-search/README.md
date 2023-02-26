# Reflectin for Two-pointers questions

## Questions
[minimum operation to reduce x to zero](#1658_minimum-operations-to-reduce-x-to-zero_testpy)

## Details
### [1658_minimum-operations-to-reduce-x-to-zero_test.py](1658_minimum-operations-to-reduce-x-to-zero_test.py)

Sliding window question. 

You may wonder how two pointers at the two ends of the list can solve the question - **this might not be how sliding window works** - since moving either end inward represents "reducing the sum of values between the 2 pointers".

But how about both pointers on the head of the list - represents "All values are belong to the tail portion, and definitely greater than target X", hence:
- tail pointer moves to right: decrement the sum with minimum value
- head pointer moves to right: increment the sum with minimum value

we keeps moving the tail pointer to the right until `head_sum + tail_sum <= X`, we can calulate the head and tail length, then move head pointer one unit right, so increment `head_sum` with minimum value. 

Continue above steps until both head, tail pinters reachign the end.

***So I think important feature of sliding window problem is move one end to make the outcome larger, moveing the other end to make the outcome smaller***

---
### [300_longest-increasing-subsequence_test.py](300_longest-increasing-subsequence_test.py)

Dynamic programming question!

Keep the state and transfer it, so next step can leverage on.

Iterate over the list, and keeps the longest increasing subsequence it can be achieved up to the step. The next step will determine its own 'state' after doing the comparison logic aginst its previous state / **states** - which happens in our case, that each element being interated on, needs to check against **all its preceeding numbers and build its own state based on the overall best outcome**.

(To the future me, hope you can know what I am saying and probably can add more regarding the understanding about DP!)

---
### [718 maximum length of repeated subarray](718_maximum-length-of-repeated-subarray_test.py)

Dynamic programming question, again!

From the question, not hard to realize that the 'state' exists! Build a 2D array say Outcome[i][j] representing when pointer i in nums1, and pointer j in nums2, what is the best outcome it can achieve! Once that is determined, Outcome[i+1][j+1] will be either 0 / Outcome[i][j] + 1 !

---

### [754 reach a number](754_reach_a_number.py)

Greedy question?

Let us just keep moving right (positive num) until either:
1. the cumulative sum equals to the target 
2. the cumulative sum greater than the target

Case #1 is fine, that means we need to move n steps, where $\frac{(1 + n)*n}{2} = target$;

Case #2, means we have exceed the target slightly:
- if the delta = the_sum - target, and delta is dividable by 2 (the delta is an even number), it means we just need to toggle the direction of step $\frac{delta}{2}$ (it is an non zero integer) to make the new sum becomes target. **Why it is $\frac{delta}{2}$ , go think idiot!** So the steps need to take is still equivalent to the number of steps took,namely n.

- if the delta is not dividable by 2, it means we can move:
    1. one step to the left of current step n
    2. then one step right -> so here we can effective movement of - $n - 1 + n$, which is 1 unit right -> it means 2 steps taken, and these 2 steps taken, and be substracted from the_sum, will make the delta become an even.
    3. **but any way to make 1 step rather than 2 like #2 saying?** - Yes! the answer is that it happens when after moving the move, the new delta becomes an even, namely:
        $$
        \frac{the\_sum + (n + 1)}{2}
        $$



---

### [754 reach a number](754_reach_a_number.py)

Greedy question?

Let us just keep moving right (positive num) until either:
1. the cumulative sum equals to the target 
2. the cumulative sum greater than the target

Case #1 is fine, that means we need to move n steps, where $\frac{(1 + n)*n}{2} = target$;

Case #2, means we have exceed the target slightly:
- if the delta = the_sum - target, and delta is dividable by 2 (the delta is an even number), it means we just need to toggle the direction of step $\frac{delta}{2}$ (it is an non zero integer) to make the new sum becomes target. **Why it is $\frac{delta}{2}$ , go think idiot!** So the steps need to take is still equivalent to the number of steps took,namely n.

- if the delta is not dividable by 2, it means we can move:
    1. one step to the left of current step n
    2. then one step right -> so here we can effective movement of - $n - 1 + n$, which is 1 unit right -> it means 2 steps taken, and these 2 steps taken, and be substracted from the_sum, will make the delta become an even.
    3. **but any way to make 1 step rather than 2 like #2 saying?** - Yes! the answer is that it happens when after moving the move, the new delta becomes an even, namely:
        $$
        \frac{the\_sum + (n + 1)}{2}
        $$



---
### [162 find peak element](162_find-peak-element_test.py)

Binary search problem.

Need to pay attention to `对于所有有效的 i 都有 nums[i] != nums[i + 1]` that ensures 2 adjacement values definitely unequal - so must be one bigger and one smaller value. So we just need to continue search on the bigger side where must be a peak on its side. Picture it with a wave graph, dude!

---
### [1101 capacity to ship packages within d days](1101_capacity-to-ship-packages-within-d-days_test.py)

Binary search for a boundary value - rather than searching for a exact number, but a minimum threshold/boundary number!

We know the minimum capacity that fulfills the delivering within `n` days requirement, and we also can tell the maximum capacity, be `max(weights)` and `sum(weights)`. So we can do a binary search between that range for a minimum weight value that fufill the days limit.

---
### [1802 Maximum value at a given index in a bounded array](1802_maximum-value-at-a-given-index-in-a-bounded-array_test.py)

Greedy + Binary search.

Greedy approach in terms of thinking the objective is to get the maximum number at a given index in the array, and given the absolute difference between 2 adjacement numbers can't be greater than 1, we need to try the best to minimize the rest numbers not at the index.
In other words, we **just need to find the max number at the index, infer the rest, and ensure the contraint max sum is not exceeded**.

Binary search suits for problems that the outcome is proportional to the inputs, regardless it is postive proportional or negative proportional. With one input, we should be advised from the outcome for the next optional input.

So we just need to find an max input between 1 and the maxSum, that fulfill the maxSum constraint.

### [1608 Special array with x elements greater than or equal x](1608_special-array-with-x-elements-greater-than-or-equal-x_test.py)

I did it with binary search, but it can be a linear O(n) solution, if I had a smart brain :blush:.

Binary search, is because there are **proportional** relation between the `x` and `number of elements >= x`: if `x` increases, less `number of elements >= x`; if `x` decreases, more `number of elements >= x`. So the question becomes, a binary search question, to keep adjusting until you find the x, and it make `number of elements >= x` be x too! One function for this binary search, the other function for returning the `number of elements >= x`. If the latter returns more then `x`, you need to increment `x`, vice versa.

But If you are smart, the question becomes, sorting the nums in descending order, and find `nums[i - 1]` (it is at `i`th in nums) and it should >= i, and its next value `nums[i]` should strictly < i.