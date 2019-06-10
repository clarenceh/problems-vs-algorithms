# Problems vs Algorithms - Problem 6 - Unsorted Integer Array - Explanation

## Logic implemented
Maintain 2 variables for the min/max values.

To find the min/max value in an un-sorted array, Linear Search algorithm was used:
1. Traverse the array from first to last index
1. For each element, compare against the current min/max value, and if smaller than the min value, update the current min value with the value at this index. If larger than the current max value, update the current max value.
1. Upon completion, return the min/max values as the result.

## Run time complexity
The logic completes in a single traversal, which is of O(n)

## Space complexity
Linear search with in-place comparison was done in this algorithm. Constant space was used.

As a result, the space complexity if of O(1).
