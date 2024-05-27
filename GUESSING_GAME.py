import random 
secret_num = random.randint (0,10)
max_attempt= 3
def welcome_message():
    print("\nwelcome to the Number Guesssing Game!!!1")
    print(f"You have {max_attempt} attempts to guess the correct answer!!")

def guess_recursive(attempts_left):
    guess= int(input("\nGuess the number between(1-10)---->>>"))
    if guess ==secret_num :
        print("congratulations you got it right!!")
    else:
        print(f"wrong guess!! attempts remaining:{attempts_left-1}")
        if attempts_left > 1:
            guess_recursive(attempts_left -1)
        else:
            print(f"\nsorry,You couldn't guess the number. The correct number was{secret_num}.")
welcome_message()
guess_recursive(max_attempt)
print(f"Memory address of secret number{secret_num} is : {id(secret_num)}")