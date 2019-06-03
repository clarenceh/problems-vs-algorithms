def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

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


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
