def bubble_sort_2d(arr):
# Number of rows in the 2D array
    n = len(arr)
    m= len(arr[0]) # Number of columns in the 2D array; assumes all rows have equal length
    total_elements = n* m # Total number of elements in the 2D array *
    for i in range(total_elements - 1):
             # Outer loop: goes through all elements in the 2D array
    	 for j in range (total_elements- 1 - i):
            # Inner loop: goes through the elements, reducing the comparison range each time
            # Calculate current position in 2D terms
            row1 = j // m
            col1 = j % m
    # Calculate next position (right next to current position)
    row2 = (j + 1) // m
    col2 = (j + 1) % m
    # Compare and possibly swap elements
    if arr[row1][col1] > arr[row2][col2]:
    # If the current element is greater than the next, swap them
        arr[row1][col1], arr[row2] [col2] = arr[row2] [col2], arr[row1] [col1]
def search_element (arr, element):
    found = False # Initialize a flag to track if the element is found
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                print(f"Element found at position: row = {i}, column {j}")
            found = True
            return # Exit the function after finding the element
    if not found:
        print("Element not found in the given array.")
# Example usage:
arr = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
    ]
print(arr)
bubble_sort_2d(arr)
print(arr)
# Searching for an element
search = int(input("Enter the element to search: "))
search_element (arr, search)