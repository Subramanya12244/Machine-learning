def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    
    A palindrome is a sequence that reads the same forward and backward.
    This function compares the list with its reverse and returns True if they are equal, 
    indicating that the list is a palindrome. Otherwise, it returns False.
    
    :param lst: List[int] -> List of integers to check.
    :return: bool -> True if the list is a palindrome, False otherwise.

    Time Complexity:
        - The slicing operation `lst[::-1]` takes O(n), where n is the number of elements in the list.
        - The comparison `lst == lst[::-1]` also takes O(n) time because it compares all elements.
        - Therefore, the total time complexity is O(n), where n is the number of elements in the list.

    Space Complexity:
        - The slicing operation creates a new list that is the reverse of `lst`, so the space complexity is O(n),
          where n is the number of elements in the list.
    
    Example:
        lst = [1, 2, 3, 2, 1]
        is_palindrome(lst) -> True
        
        lst = [1, 2, 3, 4, 5]
        is_palindrome(lst) -> False

    Dry Run:
        Let’s dry run the function with the input list: [1, 2, 3, 2, 1]

        1. The list is: [1, 2, 3, 2, 1]
        2. The reverse of the list is: [1, 2, 3, 2, 1]
        3. Compare the original list with its reverse:
            - [1, 2, 3, 2, 1] == [1, 2, 3, 2, 1]
            - The lists are equal, so return True.
        4. The result is True.
    """
    
    # Check if the list is equal to its reverse
    return lst == lst[::-1]
lst1 = [1, 2, 3, 2, 1]
result1 = is_palindrome(lst1)
print(f"Is the list {lst1} a palindrome? {result1}")

lst2 = [1, 2, 3, 4, 5]
result2 = is_palindrome(lst2)
print(f"Is the list {lst2} a palindrome? {result2}")
