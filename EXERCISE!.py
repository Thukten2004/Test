def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement
    return arr

# Prompt the user to input an array of integers
input_array = input("Enter an array of integers separated by spaces: ").split()
array = [int(num) for num in input_array]

# Sort the array using quick sort algorithm
sorted_array = quick_sort(array)

# Display the sorted array
print("Sorted array:", sorted_array)

# Allow the user to specify a target element to search for
target = int(input("Enter the target element to search for: "))

# If the target element is found, prompt the user to input a replacement element
if target in sorted_array:
    replacement = int(input("Enter the replacement element: "))
    # Replace all occurrences of the target element with the replacement element in the array
    modified_array = replace_elements(sorted_array, target, replacement)
    # Display the modified array after replacing the elements
    print("Modified array after replacement:", modified_array)
else:
    print("Target element not found in the sorted array.")