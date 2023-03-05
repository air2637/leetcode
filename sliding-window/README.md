# Reflection for sliding window questions

> Sliding window is always moving two pointers in the same direction, and it is optimize for brute force solutions. ==TODO: Think when to apply this technique!==


## Details

### [395 Longest substring with at least k repeating characters](395_longest-substring-with-at-least-k-repeating-characters_test.py)

Solved by recursive apporach.

Keep dividing the string into substring, and the delimiter is an arbitrary character which has overall frequency less than k. If no such character and the length of the substring is > k, means the entire substring fufills the condition; if the total length is already less than k, directly return 0. Keep return the max value between the left portion and right portion.

### [424 Longest repeating character replacement](424_longest-repeating-character-replacement_test.py)

What I did was treating it as a replacement to a specific character and see the longest length can be achieved. Iterating each character and take it as the target value after replacement, if the character before replacing is not the target character. Then using sliding windown keep checking:
- if the 'quota' still available, keep moving right pointer to its next index
- if the 'quota' used out, move left pointer to its next index (alteratively, I think I can directly jump to the first index occupying the quota), unitl we have the 'quota' again.

**While, there is a smart way with one iteration.** 

We just need to know if the right pointed character is the target character, and the target character I meant here is the character of majority in the substring:
- Instead of tracking 'quota', we just need to compare `right - left + 1` vs `the current freq of the target character + k`, if the former is smaller, means we still have the quota.
- A key understanding - **We don't need to keep tracking which character becomes the target character along with poping left indexed character, adding right indexed character. Instead, we care if the added right indexed character would help expand the `current freq of the target character + k`**:
    - if not, pop left indexed character, and update the frequency table
        - so here looks normal operation, but is quite significant: it decrement the popped out character's frequency: if the popped out character is same as the added in one, the freq of right won't be changed -> the windown width will not be changed; if the popped out character is different from the added in one, we keep the freq updated with correct statistics of current sliding window.
    - else skip the poping left, but continue with adding next right.

### [438 Find all anagrams in a string](438_find-all-anagrams-in-a-string_test.py)

Sliding window. When the length between (right - left + 1) is the length of pattern 'p', do check if the frequency of chars are fully matched. If the scanned ch not in 'p', left will jump to right + 1; if the ch in 'p', continue.

### [904 Fruit into baskets](904_fruit-into-baskets_test.py)

Sliding window with 2 pointers - pointer for adding the fruit into basket, pointer for removing the fruit from basket. If the fruits added so far are less than 2 kinds, or the to be added fruit is of one kind of the added fruits, add it. Otherwise, shift the pointer for removing the fruits all the way till only one kind left.