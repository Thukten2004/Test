while True:
    print("My Calculator")
    print('''-----------------------------------------------------------------
            1.add
            2. substract
            3. multiply
            4. divide''')
    a=int(input("What you want to do:"))
    x= int(input("Enter any number:"))
    y= int(input("enter another number:"))


    if a == 1:
        b=x+y
        print(f"{x}+{y}={b}")
    elif a == 2:
        c=x-y
        print(f"{x}-{y}={c}")
    elif a == 3:
        d=x*y
        print(f"{x}x{y}={d}")
    elif a == 4:
        e=x/y
        print(f"{x}/{y}={e}")
    else:
        print("error!")
