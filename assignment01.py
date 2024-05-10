################################
# Your Name
# Your Section
# Your Student ID Number
################################

################################
# REFERENCES
# No references were used in this solution.
################################

################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################

# Function to read the input file
f = open('trauma/input_9_cap1.txt', 'r')
print(f.read())
f.close()

# Function to calculate the score for a single round
def calculate_round_score(opponent, desired_outcome):
    shape_scores = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3  # Scissors
    }

    outcome_scores = {
        "X": 0,  # Lose
        "Y": 3,  # Draw
        "Z": 6   # Win
    }

    opponent_score = shape_scores[opponent]

    if desired_outcome == "Y":
        your_shape = opponent
    elif (opponent, desired_outcome) in [("A", "Z"), ("B", "X"), ("C", "Y")]:
        your_shape = "B" if opponent == "A" else "C" if opponent == "B" else "A"
    else:
        your_shape = "C" if opponent == "A" else "A" if opponent == "B" else "B"

    your_score = shape_scores[your_shape]

    return your_score + outcome_scores[desired_outcome]

# Function to calculate the total score
def calculate_total_score(file_name):
    data = "trauma/input_9_cap1.txt"
    total_score = sum(calculate_round_score(opponent, desired_outcome) for opponent, desired_outcome in data)
    return total_score

# Your Student ID Number
student_number = 'trauma/input_9_cap1.txt'

# Input file name
input_file_name = f"input_{student_number}_cap1.txt"

# Calculate the total score
total_score = calculate_total_score(input_file_name)

# Print the total score
print(f"Your total score is: {total_score}")