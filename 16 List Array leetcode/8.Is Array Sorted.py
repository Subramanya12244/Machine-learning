def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.

    This function checks whether the input array `arr` is sorted in non-decreasing order. 
    The array is considered sorted if each element is less than or equal to the next one.

    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted in non-decreasing order, False otherwise

    Time Complexity:
        - The function iterates through the list once, comparing each pair of adjacent elements.
        - The time complexity is O(n), where n is the number of elements in the list.

    Space Complexity:
        - The space complexity is O(1) because the function uses a constant amount of extra space.

    Example:
        arr = [1, 2, 2, 3, 5]
        is_sorted(arr) -> True
        
        arr = [1, 3, 2, 4]
        is_sorted(arr) -> False

    Dry Run:
        Let's dry run the function with the input list: [1, 2, 3, 5, 4].

        1. Input list: [1, 2, 3, 5, 4]
        2. Start checking each adjacent pair:
            - Compare arr[0] (1) with arr[1] (2): 1 <= 2, continue.
            - Compare arr[1] (2) with arr[2] (3): 2 <= 3, continue.
            - Compare arr[2] (3) with arr[3] (5): 3 <= 5, continue.
            - Compare arr[3] (5) with arr[4] (4): 5 > 4, return False.
        3. The array is not sorted, so the function returns False.

    Example 2: [1, 2, 2, 3, 4]
    1. Input list: [1, 2, 2, 3, 4]
    2. Start checking each adjacent pair:
        - Compare arr[0] (1) with arr[1] (2): 1 <= 2, continue.
        - Compare arr[1] (2) with arr[2] (2): 2 <= 2, continue.
        - Compare arr[2] (2) with arr[3] (3): 2 <= 3, continue.
        - Compare arr[3] (3) with arr[4] (4): 3 <= 4, continue.
    3. All elements are in non-decreasing order, so the function returns True.
    """
    # Iterate through the array, checking each adjacent pair of elements
    for i in range(len(arr) - 1):
        # If any element is greater than the next one, return False
        if arr[i] > arr[i + 1]:
            return False
    # If no such pair is found, the array is sorted in non-decreasing order
    return True


# Example Usage
arr1 = [1, 2, 2, 3, 5]
result1 = is_sorted(arr1)
print(f"Original list: {arr1}")
print(f"Is the list sorted? {result1}")

arr2 = [1, 3, 2, 4]
result2 = is_sorted(arr2)
print(f"Original list: {arr2}")
print(f"Is the list sorted? {result2}")
