def findMin(nums):
    """
    Find the minimum element in a rotated sorted array.

    This function uses binary search to find the minimum element in the rotated sorted array in O(log n) time.

    Parameters:
    nums (List[int]): A rotated sorted array of integers.

    Returns:
    int: The minimum element in the array.

    Example:
    >>> findMin([4,5,6,7,0,1,2])
    0

    >>> findMin([3,4,5,1,2])
    1

    >>> findMin([11,13,15,17])
    11

    Dry Run Example:
    ==================
    Let's dry run the function with an example array:

    Example Input:
    nums = [4, 5, 6, 7, 0, 1, 2]

    We will use binary search to find the minimum element.

    **Initial Values:**
    left = 0, right = 6 (length of the array - 1)

    **First Iteration:**
    mid = (0 + 6) // 2 = 3, nums[mid] = 7
    - Since nums[mid] > nums[right], this means the minimum element lies on the right side.
    - Update left = mid + 1 = 4.

    **Second Iteration:**
    mid = (4 + 6) // 2 = 5, nums[mid] = 1
    - Since nums[mid] < nums[right], this means the minimum element lies on the left side.
    - Update right = mid = 5.

    **Third Iteration:**
    mid = (4 + 5) // 2 = 4, nums[mid] = 0
    - Since nums[mid] < nums[right], again, the minimum element lies on the left side.
    - Update right = mid = 4.

    The loop ends with left = right = 4, which means we have found the minimum element at index 4, which is 0.

    Final result: 0

    Time Complexity:
    ===========================
    The time complexity of the solution is O(log n), where n is the number of elements in the array.
    This is because we are using binary search to find the minimum element.

    Space Complexity:
    ===========================
    The space complexity is O(1), as we are using only a constant amount of extra space.
    """
    
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            # The minimum element must be on the right side
            left = mid + 1
        else:
            # The minimum element must be on the left side
            right = mid

    # At the end of the loop, left == right and it points to the minimum element
    return nums[left]


# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # Output: 0

nums = [3, 4, 5, 1, 2]
print(findMin(nums))  # Output: 1

nums = [11, 13, 15, 17]
print(findMin(nums))  # Output: 11
