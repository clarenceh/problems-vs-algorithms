# Problems vs Algorithms - Problem 3 - Rearrange Array Digits - Explanation

## Logic implemented
Firstly, heap sort was used to sort the digit array

Afterwards, traverse the sorted list and construct the 2 numbers respectively.

## Run time complexity
The run time complexity is the same as the Heap Sort algorithm, which is of O(nlog(n))

## Space complexity
Firstly, Heap Sort use in-place value comparison and swapping. 

Afterwards, the construction of 2 values take a portion of the space of the input array size.

As a result, the space complexity is of O(n).
