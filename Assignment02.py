################################
# Thukten Yezer
# 1. Electrical
# 02230089
################################
# REFERENCES
# @CHAT_GPT
# @DQ-Logo
################################
# SOLUTION
# Your Solution Score: 36409
# Put your number here
# trauma/input_9_cap1.txt(36409)
################################

# Read the input.txt file
def read_input(Input_your_file_name):
    x = []
    with open(Input_your_file_name, 'r') as files:
        for y in files:
            opponent_choice, outcome = y.split()
            x.append((opponent_choice, outcome))
    return x

# To Calculate the score for each round
def calculate_score(Total_Number_of_rounds):
    Score = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # You need to lose
            if opponent_choice == 'A':
                Score += 6  # if Paper defeats Rock
            elif opponent_choice == 'B':
                Score += 1  # if Scissors defeats Paper
            elif opponent_choice == 'C':
                Score += 3  # if Rock defeats Scissors
        elif outcome == 'Y':  # You need to draw
            if opponent_choice == 'A':
                Score += 4  # if Rock draws with Rock
            elif opponent_choice == 'B':
                Score += 5  # if Paper draws with Paper
            elif opponent_choice == 'C':
                Score += 3  # if Scissors draws with Scissors
        elif outcome == 'Z':  # You need to win
            if opponent_choice == 'A':
                Score += 1  # if Paper loses to Rock
            elif opponent_choice == 'B':
                Score += 3  # if Scissors loses to Paper
            elif opponent_choice == 'C':
                Score += 7  # if Rock loses to Scissors
    print(f"The total score is:{Score}")

# To run a program
Input_your_file_name = "trauma/input_9_cap1.txt"  # Change this according to your student number
calculate_score(read_input(Input_your_file_name))

