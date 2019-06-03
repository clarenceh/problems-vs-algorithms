def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Handle zero value
    if number == 0:
        return 0

    # Use divide and conquer approach
    # - Find the middle value and check it's square value
    # - if larger, then search from the left half, else search from the right half
    left_value = 1
    right_value = number

    # Continue the loop as long as right value larger then left value + 1
    while right_value > left_value + 1:
        mid_value = (left_value + right_value) // 2

        # Check the square value of the middle value
        mid_value_square = mid_value * mid_value

        if mid_value_square > number:
            right_value = mid_value
        elif mid_value_square < number:
            left_value = mid_value
        else:
            return mid_value

    # If no exact match, return the left value which is the floor value
    return left_value


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
