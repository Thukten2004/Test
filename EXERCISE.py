def find_first_repeating_character(s):
    char_count = {}  # Dictionary to store character counts

    for char in s:
        if char in char_count:
            # Character is repeating
            print(f"First repeating character: {char}")
            print(f"Memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1

    # No repeating character found
    print("No repeating character found.")
    return None
# Example usage
input_string = "abca"
find_first_repeating_character(input_string)