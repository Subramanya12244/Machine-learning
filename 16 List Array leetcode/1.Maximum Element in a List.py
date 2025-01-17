def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    
    This function iterates through the entire list and compares each element
    with the current maximum value. It returns the largest value found in the list.

    :param lst: List[int] -> A list of integers. The list must not be empty.
    :return: int -> The maximum element in the list.

    Time Complexity:
        - The function iterates through each element of the list exactly once.
        - Therefore, the time complexity is O(n), where n is the number of elements in the list.
        
    Space Complexity:
        - The space complexity is O(1), as the function only uses a constant amount of extra space
          (i.e., a single variable `maximum`).
    
    Example:
        lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        find_max_element(lst) -> 9
    
    Dry Run:
        Let’s dry run the function with the input list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        
        1. Initialize `maximum = 3` (first element in the list).
        2. Start iterating from the second element (`i = 1`):
            - i = 1: lst[1] = 1, `maximum` is 3. No change.
            - i = 2: lst[2] = 4, `maximum` is 3. Update `maximum` to 4.
            - i = 3: lst[3] = 1, `maximum` is 4. No change.
            - i = 4: lst[4] = 5, `maximum` is 4. Update `maximum` to 5.
            - i = 5: lst[5] = 9, `maximum` is 5. Update `maximum` to 9.
            - i = 6: lst[6] = 2, `maximum` is 9. No change.
            - i = 7: lst[7] = 6, `maximum` is 9. No change.
            - i = 8: lst[8] = 5, `maximum` is 9. No change.
            - i = 9: lst[9] = 3, `maximum` is 9. No change.
        3. After iterating through all elements, the maximum value found is `9`.
        4. Return `9`.
    """
    
    # Edge case: If the list is empty, raise an exception
    if not lst:
        raise ValueError("The list is empty.")
    
    maximum = lst[0]  # Initialize the maximum value with the first element in the list
    
    # Start iterating from the second element (index 1)
    for i in range(1, len(lst)):  
        if lst[i] > maximum:
            maximum = lst[i]  # Update maximum if a larger value is found
    
    return maximum

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
result=find_max_element(lst)
print(result)