def searchRange(nums, target):
    """
    Find the starting and ending positions of a given target value in a sorted array.

    This function performs a binary search twice. First, it finds the first occurrence
    of the target value using binary search, and second, it finds the last occurrence 
    of the target value. Both of these are done efficiently in O(log n) time, where 
    n is the length of the array.

    Parameters:
    nums (List[int]): A sorted list of integers.
    target (int): The target value to search for.

    Returns:
    List[int]: A list containing the starting and ending indices of the target. 
               If the target is not found, returns [-1, -1].

    Example:
    >>> searchRange([5, 7, 7, 8, 8, 10], 8)
    [3, 4]

    >>> searchRange([5, 7, 7, 8, 8, 10], 6)
    [-1, -1]

    >>> searchRange([5, 7, 7, 8, 8, 10], 10)
    [5, 5]
    """
    result = []

    # Helper function to find the first occurrence of the target.
    def firstOccurrence(nums, target):
        left, right = 0, len(nums) - 1
        found = -1  # If not found, we return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found = mid
                right = mid - 1  # Continue searching to the left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return found

    # Helper function to find the last occurrence of the target.
    def lastOccurrence(nums, target):
        left, right = 0, len(nums) - 1
        found = -1  # If not found, we return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found = mid
                left = mid + 1  # Continue searching to the right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return found

    # Perform the search for both the first and last occurrence
    first = firstOccurrence(nums, target)
    last = lastOccurrence(nums, target)

    if first == -1:  # If the target is not found, return [-1, -1]
        result.append(-1)
        result.append(-1)
    else:
        result.append(first)
        result.append(last)

    return result


# Example usage
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]

target = 6
print(searchRange(nums, target))  # Output: [-1, -1]

target = 10
print(searchRange(nums, target))  # Output: [5, 5]


# ===================== Dry Run =====================

# Input:
# nums = [5, 7, 7, 8, 8, 10]
# target = 8

# Step 1: First Occurrence (Binary Search)
# Initial Variables: left = 0, right = 5 (length of nums - 1)
# First Iteration:
#   mid = (0 + 5) // 2 = 2
#   nums[mid] = 7, since nums[mid] < target, move left = mid + 1 = 3.
# Second Iteration:
#   mid = (3 + 5) // 2 = 4
#   nums[mid] = 8, since nums[mid] == target, set found = mid = 4, and move right = mid - 1 = 3.
# Third Iteration:
#   mid = (3 + 3) // 2 = 3
#   nums[mid] = 8, since nums[mid] == target, set found = mid = 3, and move right = mid - 1 = 2.
# Loop ends with left = 3, right = 2, first occurrence of target is found at index 3.

# Step 2: Last Occurrence (Binary Search)
# Initial Variables: left = 0, right = 5 (length of nums - 1)
# First Iteration:
#   mid = (0 + 5) // 2 = 2
#   nums[mid] = 7, since nums[mid] < target, move left = mid + 1 = 3.
# Second Iteration:
#   mid = (3 + 5) // 2 = 4
#   nums[mid] = 8, since nums[mid] == target, set found = mid = 4, and move left = mid + 1 = 5.
# Third Iteration:
#   mid = (5 + 5) // 2 = 5
#   nums[mid] = 10, since nums[mid] > target, move right = mid - 1 = 4.
# Loop ends with left = 5, right = 4, last occurrence of target is found at index 4.

# Final Output:
# The first occurrence is at index 3, and the last occurrence is at index 4.
# Therefore, the result is [3, 4].

# ===================== Time and Space Complexity =====================

# Time Complexity:
# - First occurrence binary search takes O(log n)
# - Last occurrence binary search also takes O(log n)
# So, the overall time complexity is O(log n).

# Space Complexity:
# - The space complexity is O(1) because we are using a constant amount of space for the variables and the result list.
