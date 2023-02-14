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
