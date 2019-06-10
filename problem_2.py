def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # Handle non-list input
    if not isinstance(input_list, list):
        return -1

    # Handle empty array
    if len(input_list) == 0:
        return -1

    left_index = 0
    right_index = len(input_list) - 1

    while right_index > left_index + 1:
        middle_index = (right_index + left_index) // 2

        middle_value = input_list[middle_index]

        # Check the value at middle and compare and identify which portion to search next
        if middle_value == number:
            return middle_index

        # Check the data sequence and determine which portion to search next

        # Case 1: left_value < middle_value < right_value
        if input_list[left_index] < middle_value < input_list[right_index]:
            if number > middle_value:
                left_index = middle_index
            else:
                right_index = middle_index
        # Case 2: middle_value > left_value and middle_value > right_value
        elif middle_value > input_list[left_index] and middle_value > input_list[right_index]:
            if input_list[left_index] <= number < middle_value:
                right_index = middle_index
            else:
                left_index = middle_index
        # Case 3: middle_value < left_value and middle_value < right value
        elif middle_value < input_list[left_index] and middle_value < input_list[right_index]:
            if middle_value < number <= input_list[right_index]:
                left_index = middle_index
            else:
                right_index = middle_index

    # At this point, either 1 or 2 values left, perform final comparison
    if input_list[left_index] == number:
        return left_index
    elif input_list[right_index] == number:
        return right_index
    else:
        return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test case 1 - array with non-rotated values
print("Calling function with non-rotated array: [1, 2, 3, 4], target value = 3")
# Should print Pass as the index should be 2
test_function([[1, 2, 3, 4], 3])

# Test case 2 - array with rotated values
print("Calling function with rotated array: [6, 7, 8, 9, 10, 1, 2, 3, 4], target value = 1")
# Should print Pass as the index should be 5
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# Test case 3 - array without the target value
print("Calling function with array: [6, 7, 8, 9, 10, 1, 2, 3, 4], non-exist target value = 5")
# Should print Pass as the index should be -1
test_function([[6, 7, 8, 1, 2, 3, 4], 5])

# Test case 4 - empty array
print("Calling function with empty array: [], target value = 5")
# Should print Pass as the index should be -1
test_function([[], 5])

# Test case 5 - non-list inut
print("Calling function with non-list input: 10, target value = 5")
# Should print Pass as the index should be -1
test_function([[], 5])
