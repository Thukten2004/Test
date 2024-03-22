x=int(input("Enter the number for which you want to multiple: "))
y=int(input("Enterthe limit upto which you want the multiplication table generated: "))
for i in range(x,x+1):
    for j in range(1,y+1):
        print(f"{i}x{j}={i*j}")
