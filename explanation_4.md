# Problems vs Algorithms - Problem 4 - Dutch National Flag Problem - Explanation

## Logic implemented
Maintain 3 indexes to keep track of the last index of low (0), middle (1), and bottom of high (2) values

Traverse the array and depends on the value at 1's index, perform swapping of values and update the corresponding index accordingly.

## Run time complexity
The logic completes in a single traversal, which is of O(n)

## Space complexity
In place comparison and swapping was done in this algorithm. No additional space was required.

As a result, the space complexity if of O(n).
