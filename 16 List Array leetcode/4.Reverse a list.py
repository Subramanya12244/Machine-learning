def reverse_with_slicing(lst):
    """
    Function to reverse a list using slicing.
    
    This function uses Python's slicing technique to reverse the list. 
    The syntax `lst[::-1]` returns a new list that is the reversed version of the original list.
    
    :param lst: List[int] -> List of integers to reverse
    :return: List[int] -> The reversed list

    Time Complexity:
        - The slicing operation creates a new list and iterates over the original list once.
        - Therefore, the time complexity is O(n), where n is the number of elements in the list.

    Space Complexity:
        - A new list is created to store the reversed list, which requires additional space.
        - Therefore, the space complexity is O(n), where n is the number of elements in the list.
    
    Example:
        lst = [1, 2, 3, 4, 5]
        reverse_with_slicing(lst) -> [5, 4, 3, 2, 1]
    
    Dry Run:
        1. Input list: [1, 2, 3, 4, 5]
        2. Reverse using slicing: lst[::-1] results in [5, 4, 3, 2, 1]
        3. Return the reversed list [5, 4, 3, 2, 1]
    """
    return lst[::-1]


def reverse_inplace(lst):
    """
    Function to reverse a list in-place using the reverse() method.
    
    This function uses Python's built-in `reverse()` method, which reverses the list in place 
    (modifies the original list). This approach doesn't create a new list but instead 
    directly changes the order of elements in the original list.
    
    :param lst: List[int] -> List of integers to reverse
    :return: List[int] -> The reversed list (reversed in-place)

    Time Complexity:
        - The `reverse()` method iterates over the list once to reverse it.
        - Therefore, the time complexity is O(n), where n is the number of elements in the list.
        
    Space Complexity:
        - The `reverse()` method reverses the list in place without using any extra space.
        - Therefore, the space complexity is O(1).
    
    Example:
        lst = [1, 2, 3, 4, 5]
        reverse_inplace(lst) -> [5, 4, 3, 2, 1]
    
    Dry Run:
        1. Input list: [1, 2, 3, 4, 5]
        2. Call `lst.reverse()` which reverses the list in place.
        3. The list after reversing: [5, 4, 3, 2, 1]
        4. Return the reversed list [5, 4, 3, 2, 1]
    """
    lst.reverse()
    return lst


def reverse_manual(lst):
    """
    Function to reverse a list manually (without slicing or the reverse() method).
    
    This function manually constructs a reversed list by iterating through the input list 
    and inserting each element at the beginning of a new list.
    
    :param lst: List[int] -> List of integers to reverse
    :return: List[int] -> The reversed list

    Time Complexity:
        - The function uses the `insert(0, item)` method, which takes O(n) time for each insertion 
          (because it shifts all elements to the right).
        - Therefore, the time complexity is O(n^2), where n is the number of elements in the list.
        
    Space Complexity:
        - A new list is created to store the reversed elements.
        - Therefore, the space complexity is O(n), where n is the number of elements in the list.
    
    Example:
        lst = [1, 2, 3, 4, 5]
        reverse_manual(lst) -> [5, 4, 3, 2, 1]
    
    Dry Run:
        1. Input list: [1, 2, 3, 4, 5]
        2. Initialize `reversed_lst = []`.
        3. Insert elements in reverse order:
            - Insert 1 at index 0 -> reversed_lst = [1]
            - Insert 2 at index 0 -> reversed_lst = [2, 1]
            - Insert 3 at index 0 -> reversed_lst = [3, 2, 1]
            - Insert 4 at index 0 -> reversed_lst = [4, 3, 2, 1]
            - Insert 5 at index 0 -> reversed_lst = [5, 4, 3, 2, 1]
        4. Return the reversed list [5, 4, 3, 2, 1]
    """
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)  # Insert each element at the start of the new list
    return reversed_lst


# Example Usage
lst = [1, 2, 3, 4, 5]

# Reversing using slicing
print("Reversed with slicing:", reverse_with_slicing(lst))

# Reversing in-place using reverse()
print("Reversed in-place with reverse():", reverse_inplace(lst.copy()))  # copy to avoid in-place modification

# Reversing manually using loop
print("Reversed manually:", reverse_manual(lst))
