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