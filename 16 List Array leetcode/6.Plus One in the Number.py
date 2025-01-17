def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    
    This function takes a list of digits representing a large integer (e.g., [1, 2, 3] represents the integer 123),
    and increments the integer by 1. It handles the carry-over for cases where a digit is 9, such as when 
    incrementing [1, 9, 9] would result in [2, 0, 0].
    
    The function processes the digits from right to left, starting from the least significant digit. If the current 
    digit is less than 9, it is simply incremented by 1, and the result is returned. If the current digit is 9, 
    it is set to 0, and the carry is propagated to the next more significant digit. If a carry remains after 
    processing all digits, a 1 is added at the beginning of the list.
    
    :param digits: List[int] -> List of digits representing the large integer.
    :return: List[int] -> The list representing the integer after incrementing by one.

    Time Complexity:
        - The function iterates through the list of digits from right to left.
        - In the worst case, it iterates through all the digits (if there's a carry-over for each digit).
        - Therefore, the time complexity is O(n), where n is the number of digits in the list.
    
    Space Complexity:
        - The space complexity is O(1) since the operation is performed in-place on the input list.
        - The only extra space used is for the result in case of a carry-over, which is constant.
        - Hence, the space complexity is O(1).

    Example:
        digits = [1, 2, 3]
        plus_one(digits) -> [1, 2, 4]
        
        digits = [9, 9, 9]
        plus_one(digits) -> [1, 0, 0, 0]
    
    Dry Run:
        Let's dry run the function with the input list: [1, 9, 9] and digits = [1, 2, 3].

        Example 1: digits = [1, 2, 3]
        1. Input list: [1, 2, 3]
        2. Start from the rightmost digit:
            - Check digits[2] (3): It's less than 9, so increment it by 1.
        3. Return the updated list: [1, 2, 4]
        
        Example 2: digits = [9, 9, 9]
        1. Input list: [9, 9, 9]
        2. Start from the rightmost digit:
            - Check digits[2] (9): It's 9, so set it to 0, and carry over 1 to the next digit.
            - Check digits[1] (9): It's 9, so set it to 0, and carry over 1 to the next digit.
            - Check digits[0] (9): It's 9, so set it to 0, and carry over 1 to a new digit at the beginning.
        3. Add a new 1 at the beginning: [1, 0, 0, 0]
        4. Return the updated list: [1, 0, 0, 0]
    """
    # Start iterating from the rightmost digit
    for i in range(len(digits) - 1, -1, -1):
        # If the current digit is less than 9, just increment and return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the current digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0
    
    # If all digits were 9, we need to add 1 at the beginning
    return [1] + digits


# Example Usage
digits1 = [1, 2, 3]
print(f"Original list: {digits1}")
result1 = plus_one(digits1)
print(f"List after incrementing: {result1}")

digits2 = [9, 9, 9]
print(f"Original list: {digits2}")
result2 = plus_one(digits2)
print(f"List after incrementing: {result2}")
