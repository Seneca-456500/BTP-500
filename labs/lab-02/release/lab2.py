#
# Author: Eren Kilinc
# Student Number: 177067238
#
# Place the code for your lab 2 here.  Read the specs carefully.
#
# To test, run the following command:
#     python3 lab2_tester.py
#

# Write the following 3 functions recursively

def factorial(number):
    # Base case
        if number == 0:
            return 1

    # Recursive case
        return number * factorial(number - 1)



def linear_search(list, key):
    def search(index):
        # Key was not found
        if index == len(list):
            return -1

        # Key was found
        if list[index] == key:
            return index

        # Check next position
        return search(index + 1)

    return search(0)



def binary_search(list, key):
    def search(low, high):
        # Key was not found
        if low > high:
            return -1

        middle = (low + high) // 2

        # Key was found
        if list[middle] == key:
            return middle

        # Search left half
        if key < list[middle]:
            return search(low, middle - 1)

        # Search right half
        return search(middle + 1, high)

    return search(0, len(list) - 1)
