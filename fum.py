import random
x=random.randint(1,100)
print(x)
for i in range(len(x)):
    if (x%2)==0:
        print("they are even number")
    else:
        print("They are odd number")
print(i)