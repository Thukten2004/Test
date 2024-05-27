from queue import Queue

patient_list= Queue()
current_list= None
while True:
    print("WELCOME TO CST INFIRMARY AAPPOINTMENT AND REGISTRATION SYSTEM!!")
    print("""Desk Manager-Select the option below:
               1.Register patiant
               2.Remove patiant from the queue
               3.Display queue
               4.Exit""")
    opt=int(input("Select an option from the above(1/2/3/4):"))

    
    if opt==1:
        name=input("Enter the name of the patiant!!:")
        patient_list.put(name)
        current_list=name
        print(f"{name}Registration succesfull THANK YOU!!")


    elif opt==2:
        patient_list.get()
        print(f"{current_list}Removed succesfully from the queue after meeting with the doctor!!")


    elif opt==3:
        for i in patient_list.queue :
            print(i)


    elif opt==4:
        print("Thank you for the Registration!!")
        break 


    else:
        print("Invalid syntax!!")