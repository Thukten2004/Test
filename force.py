print("Newton's Second Law of Motion")
print("------------------------------------------")

#Determine the missing value
print("Select the missing value")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (f)")
missing_value_choice = input("Enter the option number for the missing value:")

#Promt the user to enter thr other two values
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force(F) "))
    m = F/a
    print(f"Mass (m) = {m}")
    
elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    F = float(input("Enter force(F) "))
    a = F/m
    print(f"Acceleration(a) = {a}")

elif missing_value_choice == "3":
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))
    F = m * a
    print(f"Force (F) = {F}")

else:
    print("Invalid option selected for the missing value")
