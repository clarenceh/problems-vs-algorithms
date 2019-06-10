# Problems vs Algorithms - Problem 4 - Dutch National Flag Problem - Explanation

## Logic implemented
Maintain 3 indexes to keep track of the last index of low (0), middle (1), and bottom of high (2) values

Traverse the array and depends on the value at 1's index, perform swapping of values and update the corresponding index accordingly.

The algorithm is similar to Quick Sort, such that in each iteration, we use the element at 1's index as the pivot. And depends the pivot value, we swap the value as follows:
1. If the value is 2, then we swap the value with the one at the bottom of 2, and decrement the bottom 2's index. We then proceed to next iteration
1. If the value is 0, then we swap the value with the one at the top of 0, and then increment the top 0's index. Then we move the 1's index one step forward and use it as the pivot.
1. If the value is 1, don't need to do any swapping, just move the 1's index one step forward and use it as the pivot. At the end after we swap all 0 and 2 values, all 1 values will be at it's right place.

## Run time complexity
The logic completes in a single traversal, which is of O(n)

## Space complexity
In place comparison and swapping was done in this algorithm. No additional space was required.

As a result, the space complexity if of O(n).
