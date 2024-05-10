def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    modified_arr = [replacement if x == target else x for x in arr]
    return modified_arr

def main():
    # Prompt user for input
    input_str = input("Enter an array of integers (comma-separated): ")
    arr = [int(x) for x in input_str.split(",")]

    # Sort the array using quick sort
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")

    # Prompt user for target element
    target = int(input("Enter the target element to search for: "))

    # Check if target exists in the sorted array
    if target in sorted_arr:
        replacement = int(input(f"Enter the replacement element for {target}: "))
        modified_arr = replace_elements(sorted_arr, target, replacement)
        print(f"Modified array after replacing {target} with {replacement}: {modified_arr}")
    else:
        print(f"{target} not found in the array.")

if __name__ == "__main__":
    main()