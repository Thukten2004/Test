x=int(input("Enter the number for which you want to multiple: "))
y=int(input("Enterthe limit upto which you want the multiplication table generated: "))
for i in range(x,x+1):
    print(i)
    for j in range(y):
        print(f"{i}x{j}={i*j}")
