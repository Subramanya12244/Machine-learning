def rotate_left(arr, d):
    """
    Function to rotate the list to the left by D positions.
    
    This function takes an input list `arr` and rotates it to the left by `d` positions. 
    The function handles the case where `d` is greater than the length of the list by 
    taking the modulus of `d` with the length of the list. The function then splits the 
    list into two parts and concatenates them in reverse order to achieve the left rotation.

    :param arr: List[int] -> The list of integers to rotate.
    :param d: int -> The number of positions to rotate the list to the left.
    :return: List[int] -> The rotated list.

    Time Complexity:
        - The function slices the list into two parts and concatenates them. 
        - Both slicing and concatenation operations take O(n) time, where n is the number of elements in the list.
        - Therefore, the time complexity is O(n), where n is the number of elements in the list.

    Space Complexity:
        - A new list is created as a result of the concatenation operation.
        - The space complexity is O(n), where n is the number of elements in the list.
    
    Example:
        arr = [1, 2, 3, 4, 5]
        d = 2
        rotate_left(arr, d) -> [3, 4, 5, 1, 2]
    
    Dry Run:
        Let's dry run the function with the input list: [1, 2, 3, 4, 5] and d = 2.

        1. Input list: [1, 2, 3, 4, 5], d = 2
        2. Calculate d % n: d = 2 % 5 = 2 (since n = len(arr) = 5)
        3. Split the list into two parts:
            - arr[d:] = arr[2:] = [3, 4, 5]
            - arr[:d] = arr[:2] = [1, 2]
        4. Concatenate the two parts: [3, 4, 5] + [1, 2] = [3, 4, 5, 1, 2]
        5. Return the rotated list: [3, 4, 5, 1, 2]
    """
    # Get the length of the list
    n = len(arr)
    # Adjust the number of rotations in case d is greater than n
    d = d % n
    # Return the rotated list by slicing
    return arr[d:] + arr[:d]


# Example Usage
arr = [1, 2, 3, 4, 5]
d = 2
result = rotate_left(arr, d)
print(f"Original list: {arr}")
print(f"List after rotating {d} positions to the left: {result}")
