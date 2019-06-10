def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Handle non-integer inputs
    try:
        int(number)
    except ValueError:
        return None

    # Handle negative integer
    if number < 0:
        return None

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


# Test case 1 - normal case
print("Calling function with value 9")
# Should print pass as the square root is exactly 3
print ("Pass" if  (3 == sqrt(9)) else "Fail")

# Test case 2 - zero value
print("Calling function with value 0")
# Should print pass as the square root is 0
print ("Pass" if  (0 == sqrt(0)) else "Fail")

# Test case 3 - floor value
print("Calling function with value 27")
# Should print pass as the square root's floor value is 5
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Test case 4 - negative value
print("Calling function with negative value -10")
# Should print pass as the function should return None
print ("Pass" if  (None == sqrt(-10)) else "Fail")

# Test case 5 - float value
print("Calling function with float value 10.1")
# Should print pass as the function should return None
print ("Pass" if  (None == sqrt(10.1)) else "Fail")

# Test case 6 - non numeric
print("Calling function with non-numeric value abc")
# Should print pass as the function should return None
print ("Pass" if  (None == sqrt('abc')) else "Fail")
