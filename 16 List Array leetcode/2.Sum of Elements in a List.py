def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.

    This function iterates through the list and adds each element to a running total.
    It returns the sum of all elements in the list.

    :param lst: List[int] -> A list of integers.
    :return: int -> The sum of all elements in the list.

    Time Complexity:
        - The function iterates over each element of the list exactly once.
        - Therefore, the time complexity is O(n), where n is the number of elements in the list.
        
    Space Complexity:
        - The space complexity is O(1), as the function uses only a constant amount of extra space
          (i.e., a single variable `sum`).

    Example:
        lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        sum_of_elements(lst) -> 39

    Dry Run:
        Let’s dry run the function with the input list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

        1. Initialize `sum = 0`.
        2. Start iterating through the list:
            - i = 3, add to sum -> sum = 0 + 3 = 3
            - i = 1, add to sum -> sum = 3 + 1 = 4
            - i = 4, add to sum -> sum = 4 + 4 = 8
            - i = 1, add to sum -> sum = 8 + 1 = 9
            - i = 5, add to sum -> sum = 9 + 5 = 14
            - i = 9, add to sum -> sum = 14 + 9 = 23
            - i = 2, add to sum -> sum = 23 + 2 = 25
            - i = 6, add to sum -> sum = 25 + 6 = 31
            - i = 5, add to sum -> sum = 31 + 5 = 36
            - i = 3, add to sum -> sum = 36 + 3 = 39
        3. After iterating through all elements, the sum is `39`.
        4. Return `39`.
    """
    sum = 0
    for i in lst:  # Iterate over each element in the list
        sum += i  # Add the element to the sum
    return sum
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result=sum_of_elements(lst)
print(result)