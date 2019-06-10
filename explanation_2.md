# Problems vs Algorithms - Problem 2 - Search in a Rotated Sorted Array - Explanation

## Logic implemented
Binary Search technique was used to locate the value within the rotated sorted array.

For each iteration, the element in the "middle" was located and compare to the target value. However, as the array is sorted and rotated, there are 3 possible cases, depends on rotated status of the array:
1. The array was not rotated (i.e. the value at the middle is larger then the first element, smaller than the last element)
- In this case, a normal comparison was done. If the search value is greater than the mid value, then the result should lies in the "right half". Proceed the search with the right portion. Otherwise proceed the search in the left portion.
1. The array was rotated in such a way that the mid value is larger than both the left and right value.
- In this case, we first check whether the search value lies in the left portion (i.e. left value < search value < mid value). If yes, the search value should lies in the left portion and we proceed the search in the left half. Otherwise, proceed the search in the right part.
1. The array was rotated in such a way that the mid value is smaller than both the left and right value.
- In this case, we first check whether the search value lies in the right portion (i.e. mid value < search value < right value). If yes, the search value should lies in the right portion and we proceed the search in the right half. Otherwise, proceed the search in the left part.

## Run time complexity
The run time complexity is the same as a Binary Search, which is of O(log(n))

## Space complexity
Binary Search takes constant space, as the space taken by the algorithm is the same for any number of elements in the array.

As a result, the space complexity if of O(1)
