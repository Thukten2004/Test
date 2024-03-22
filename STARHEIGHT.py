x=int(input("Enter the height of the triangle(number of row): "))
for i in range(1,x+1):
    for j in range(i):
        print("*", end="")
    print()