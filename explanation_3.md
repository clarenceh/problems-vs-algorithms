# Problems vs Algorithms - Problem 3 - Rearrange Array Digits - Explanation

## Logic implemented
Firstly, heap sort was used to sort the digit array

Afterwards, traverse the sorted list and construct the 2 numbers respectively:
1. Firstly, check whether the number of elements is odd. If yes, then take the last element (which is the largest digit) as the first digit of the first number. Remove the element.
2. Then we traverse the array from last element to the beginning. Which should be in the order of largest digit to smallest digit.
3. For each element, we alternatively append the digit to first and second number respectively. This way will cause the max possible digit to the most significant digit of each number.

The sum of the result 2 numbers should be the largest possible value.

## Run time complexity
The run time complexity is the same as the Heap Sort algorithm, which is of O(nlog(n))

## Space complexity
Firstly, Heap Sort use in-place value comparison and swapping. Heap Sort is of constant space complexity.

Afterwards, the construction of 2 values take a portion of the space of the input array size. 
Afterwards, the construction of the 2 values was done by a single traversal of the array, which grows linearly as the size of input.

As a result, the overall space complexity is of O(n).
