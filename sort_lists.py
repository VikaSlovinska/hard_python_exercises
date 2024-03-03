
"""
"Write a Python program to sort a list using the bubble sort algorithm from scratch. The program should ask the user to input a list of numbers and then sort them in ascending order. Here are some hints to get you started:

 Create a function called 'bubble_sort' that takes a single parameter, the list to be sorted.
 Inside the bubble_sort function, use two nested loops to compare adjacent elements in the list and swap them if they are in the wrong order.
 Use a 'while' loop to continue running the loops until no more swaps are necessary (i.e., the list is fully sorted).
 Finally, return the sorted list.
"""

example = [3, 2, 7, 1333, 45, 66, 222, 78]
def sort_list(lis):
    """
    Function to sorts a list of numbers in ascending order using the bubble sort algorithm.

    Args:
        lis (list): A list of numbers to be sorted.

    Returns:
        list: A sorted list of numbers in ascending order.
    """
    for i in range(len(lis)):
        """
        Outer loop iterates over each element of the list.
        """
        for j in range(len(lis) - i - 1):
            """
            Inner loop compares adjacent elements and swaps them if necessary.
            """
            if lis[j] > lis[j + 1]:
                """
                If the current element is greater than the next one, swap them.
                """
                tem = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = tem
            else:
                """
                If the elements are already in the correct order, do nothing.
                """
                pass
    return lis

"""
Prints the sorted list.
"""
print(sort_list(example))
