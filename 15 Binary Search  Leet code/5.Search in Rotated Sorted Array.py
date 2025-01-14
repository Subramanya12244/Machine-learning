def search(nums, target):
    """
    Search for a target value in a rotated sorted array.

    This function performs a binary search to find the target value in the rotated sorted array in O(log n) time.

    Parameters:
    nums (List[int]): A rotated sorted array of integers.
    target (int): The target value to search for.

    Returns:
    int: The index of the target in the array if it exists, otherwise -1.

    Example:
    >>> search([4, 5, 6, 7, 0, 1, 2], 0)
    4

    >>> search([3, 4, 5, 1, 2], 1)
    3

    >>> search([11, 13, 15, 17], 15)
    2

    Dry Run Example:
    ==================
    Let's dry run the function with an example array:

    Example Input:
    nums = [4, 5, 6, 7, 0, 1, 2], target = 0

    **Initial Values:**
    left = 0, right = 6 (length of array - 1)

    **First Iteration:**
    mid = (0 + 6) // 2 = 3, nums[mid] = 7
    - Since nums[mid] > nums[right], the minimum element must be on the right half of the array.
    - Update left = mid + 1 = 4.

    **Second Iteration:**
    mid = (4 + 6) // 2 = 5, nums[mid] = 1
    - Since nums[mid] < nums[right], the target could be on the left side.
    - Update right = mid - 1 = 4.

    **Third Iteration:**
    mid = (4 + 4) // 2 = 4, nums[mid] = 0
    - We found the target at index 4.

    Final result: 4

    Time Complexity:
    ===========================
    The time complexity of the solution is O(log n), where n is the number of elements in the array.
    This is because we are using binary search.

    Space Complexity:
    ===========================
    The space complexity is O(1), as we are using only a constant amount of extra space.

    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# Example usage:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))  # Output: 4

nums = [3, 4, 5, 1, 2]
target = 1
print(search(nums, target))  # Output: 3

nums = [11, 13, 15, 17]
target = 15
print(search(nums, target))  # Output: 2
