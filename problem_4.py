def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # Indexes to keep track of the last index of low (0), middle (1), and bottom of high (2) values
    top_of_zero_idx = 0                     # top index of 0
    one_idx = 0                             # index of 1
    bottom_of_2_idx = len(input_list) - 1   # bottom index of 2

    # Continue to loop while index of 1 is less than bottom index of 2
    while one_idx <= bottom_of_2_idx:
        # if value at 1 index is 0, then swap the value with the value at top of 0 index
        # also increment top of 0 index and 1 index
        if input_list[one_idx] == 0:
            input_list[one_idx], input_list[top_of_zero_idx] = input_list[top_of_zero_idx], input_list[one_idx]
            top_of_zero_idx += 1
            one_idx += 1
        # if value at 1 index is 1, nothing to do. Increment 1 index
        elif input_list[one_idx] == 1:
            one_idx += 1
        # if value at 1 index is 2, swap the value with the value at bottom of 2 index
        # also decrement bottom of 2 index
        elif input_list[one_idx] == 2:
            input_list[one_idx], input_list[bottom_of_2_idx] = input_list[bottom_of_2_idx], input_list[one_idx]
            bottom_of_2_idx -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test case 1 - unsorted array
print("Calling function with un-sorted array: [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]")
# Should print [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Should print Pass as the result array should be a correctly sorted array
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# Test case 2 - sorted array
# Should print [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print("Calling function with sorted array: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]")
# Should print Pass as the result array should be the same sorted array
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case 3 - array with only a single element
# Should print [0]
print("Calling function with sorted array: [0]")
# Should print Pass as the result array should be the same array
test_function([0])
