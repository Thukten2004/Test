Age=int(input("Enter your age: \n"))
yn=input("Are you student? (yes/no): \n")

if Age<12 or Age==12:
    print("You are eligible for discount on the movie ticket")
elif Age>=13 and Age<18 and yn=="yes":
  
    print("You are  eligible for the discount")
else:
    print("you are not eligible")
