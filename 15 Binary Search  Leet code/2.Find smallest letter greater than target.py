def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Binary search initialization
    left, right = 0, len(letters)
    
    # Perform binary search
    while left < right:
        mid = (left + right) // 2
        
        if letters[mid] <= target:
            left = mid + 1  # Move right since target is greater or equal to mid
        else:
            right = mid  # Narrow the search to the left half
    
    # At the end of the binary search, left will point to the smallest element greater than target
    return letters[left % len(letters)]  # Wrap around if no such element is found


# Dry Run Example:
letters = ["c", "f", "j"]
target = "a"

# The function will now start processing this input.

# Step 1: Initial values
# left = 0, right = 3 (since there are 3 characters in "letters")

# Step 2: First iteration of while loop
# mid = (0 + 3) // 2 = 1
# letters[mid] = "f", which is greater than "a" (target)
# So, we move the right boundary to mid: right = 1

# Step 3: Second iteration of while loop
# mid = (0 + 1) // 2 = 0
# letters[mid] = "c", which is greater than "a"
# So, we move the right boundary to mid: right = 0

# Step 4: The while loop terminates since left == right (both are 0)

# Step 5: The return statement
# At this point, left = 0, which is the index of the smallest character in the list ("c")
# We return letters[left % len(letters)], which is letters[0 % 3] = "c"

# Expected output: "c"

# Testing with more examples:
print(next_greatest_letter(["c", "f", "j"], "a"))  # Output: "c"
print(next_greatest_letter(["c", "f", "j"], "c"))  # Output: "f"
print(next_greatest_letter(["c", "f", "j"], "d"))  # Output: "f"
print(next_greatest_letter(["c", "f", "j"], "j"))  # Output: "c" (wraps around)

