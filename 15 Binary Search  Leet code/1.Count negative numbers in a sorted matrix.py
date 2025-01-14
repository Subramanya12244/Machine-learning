def countNegatives(grid):
    """
    Count the total number of negative numbers in a 2D grid.

    This function takes in a 2D grid where each row is sorted in non-increasing order (i.e., from 
    left to right, the values are decreasing). The function counts how many negative numbers are 
    present in the entire grid using an efficient binary search approach.

    Parameters:
    grid (List[List[int]]): A 2D list of integers (m x n), where each row is sorted in 
                             non-increasing order.

    Returns:
    int: The total count of negative numbers in the grid.

    Example:
    >>> countNegatives([[-1,-1,-1,-1], [-1,-1, 0, 1], [1, 1, 1, 1]])
    4

    Dry Run Example:
    ==================
    Let's dry run the function with an example grid:

    Example Input:
    grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

    We will iterate through each row, applying binary search to count the negative numbers.

    **First Row: [-1, -1, -1, -1]**
    - Binary search starts with `left = 0`, `right = 4` (length of row).
    - We calculate `mid = (0 + 4) // 2 = 2`. Since `row[2] = -1`, which is negative, we move to the left half by updating `right = mid = 2`.
    - Next, `mid = (0 + 2) // 2 = 1`. Again, `row[1] = -1`, so we update `right = mid = 1`.
    - Finally, `mid = (0 + 1) // 2 = 0`. Since `row[0] = -1`, we update `right = mid = 0`.
    - The number of negative numbers in this row is `4 - 0 = 4`.

    **Second Row: [-1, -1, 0, 1]**
    - Binary search starts with `left = 0`, `right = 4`.
    - We calculate `mid = (0 + 4) // 2 = 2`. Since `row[2] = 0`, which is non-negative, we move to the right half by updating `left = mid + 1 = 3`.
    - Next, `mid = (3 + 4) // 2 = 3`. Since `row[3] = 1`, which is non-negative, we update `left = mid + 1 = 4`.
    - The number of negative numbers in this row is `4 - 4 = 0`.

    **Third Row: [1, 1, 1, 1]**
    - Binary search starts with `left = 0`, `right = 4`.
    - We calculate `mid = (0 + 4) // 2 = 2`. Since `row[2] = 1`, which is non-negative, we move to the right half by updating `left = mid + 1 = 3`.
    - Next, `mid = (3 + 4) // 2 = 3`. Since `row[3] = 1`, we update `left = mid + 1 = 4`.
    - The number of negative numbers in this row is `4 - 4 = 0`.

    Final result: The total count of negative numbers in all rows is `4 (from row 1) + 0 (from row 2) + 0 (from row 3) = 4`.

    Helper Function (`count_neg_in_row`):
    ===================================
    The helper function `count_neg_in_row` uses binary search to efficiently find the number of 
    negative numbers in a single row:
    
    - It checks the middle element of the row and adjusts the search bounds (`left` and `right`) based on whether the middle element is negative or not.
    - This allows us to avoid scanning every element in the row, reducing the time complexity to O(log n) for each row.

    Time Complexity:
    ===========================
    The time complexity of the solution is O(m * log n), where:
    - `m` is the number of rows (length of `grid`).
    - `n` is the number of columns (length of each row).

    This is more efficient than a brute force approach, which would have O(m * n) time complexity.
    """
    
    def count_neg_in_row(row):
        """
        Helper function to count the number of negative numbers in a single row using binary search.
        
        Parameters:
        row (List[int]): A list of integers representing a single row in the grid, sorted in 
                         non-increasing order.
        
        Returns:
        int: The count of negative numbers in the row.
        """
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(row) - left

    count = 0
    for row in grid:
        count += count_neg_in_row(row)
    return count
grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
result=countNegatives(grid)
print(result)