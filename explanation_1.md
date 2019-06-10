# Problems vs Algorithms - Problem 1 - Finding the Square Root of an Integer - Explanation

## Logic implemented
Instead of a linear search for the square value, Binary Search algorithm was used to locate the square root value.

The reason is that by adopting Binary Search, in each iteration, the middle value was calculated and it's square value is compared against the target value.

If the result is less than the target value, the result should be less than the middle value, which lies in the "left half" of the middle value. Otherwise, the result should be greater which lies in the "right half" of the middle value.

So in each iteration, half of the values can be eliminated from the search and the efficiency can be greatly increased.

## Run time complexity
The run time complexity is the same as a Binary Search, which is of O(log(n))

## Space complexity
No matter what the value is, everytime we only need to find the mid value and compare the square value with the target. So constant space is used despite of the input value.

As a result, the space complexity is of O(1)