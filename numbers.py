for x in range(1,10):    
    if x==7:
        print(f"breaking at point {x}")
        break
    if x==3:
        print(f"Skipping {x} in inner loop")
        continue
    for y in range(1,4):
        if x==3:
            continue
    print(x)
    


    
    
    