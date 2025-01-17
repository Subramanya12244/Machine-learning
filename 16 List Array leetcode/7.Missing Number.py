def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    
    This function finds the missing number in an array of distinct integers 
    that is supposed to represent all the numbers in the range [0, n], but one number is missing.
    The function calculates the expected sum of numbers in the range [0, n] using the formula 
    sum = n * (n + 1) / 2, and compares it with the actual sum of the numbers in the given list. 
    The difference between the expected sum and the actual sum gives the missing number.
    
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range

    Time Complexity:
        - The function iterates through the list once to compute the actual sum.
        - The time complexity for this is O(n), where n is the length of the list.
    
    Space Complexity:
        - The space complexity is O(1) because we are only using a few extra variables for the computation,
          and the space used does not depend on the size of the input.

    Example:
        nums = [3, 0, 1]
        find_missing_number(nums) -> 2
        
        nums = [9, 8, 6, 7, 5, 0, 3, 4]
        find_missing_number(nums) -> 2

    Dry Run:
        Let's dry run the function with the input list: [3, 0, 1].

        1. Input list: [3, 0, 1]
        2. Calculate n = len(nums) = 3 (The expected range is [0, 1, 2, 3])
        3. Calculate the expected sum for the range [0, n]: 
            - expected_sum = n * (n + 1) / 2 = 3 * (3 + 1) / 2 = 6
        4. Calculate the sum of elements in the list:
            - sum = 3 + 0 + 1 = 4
        5. The missing number is: expected_sum - sum = 6 - 4 = 2
        6. Return the missing number: 2
    """
    # Calculate the length of the list
    n = len(nums)
    # Calculate the expected sum of the range [0, n]
    expected_sum = (n * (n + 1)) // 2
    # Calculate the actual sum of the elements in the list
    sum_of_nums = sum(nums)
    # Return the missing number by subtracting the actual sum from the expected sum
    return expected_sum - sum_of_nums


# Example Usage
nums1 = [3, 0, 1]
result1 = find_missing_number(nums1)
print(f"Original list: {nums1}")
print(f"Missing number: {result1}")

