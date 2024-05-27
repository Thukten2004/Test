def reverse_string(s):
    # Base case: if the string is empty or contains only one character, return the string
    if len(s) <= 1:
        return s
    else:
        # Recursive case: separate the first character from the rest of the string
        first_char = s[0]
        remaining_chars = s[1:]
        # Recursively call reverse_string on the remaining characters
        reversed_remaining = reverse_string(remaining_chars)
        # Append the first character to the end of the reversed remaining characters
        return reversed_remaining + first_char

# Take input from the user
user_input = input("Enter a string: ")

# Call the reverse_string function with user input
reversed_string = reverse_string(user_input)

# Print the reversed string
print("Reversed string:", reversed_string)