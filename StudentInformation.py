students_list = []
students_dict = {}

def add_student():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    print(f"Student {name} added successfully!")
    print(students_dict)

def search_student(): 
    name = input("Enter the name of the student you want to search for: ")
    if name in students_dict:
        print(f"Student found! Name: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter the name of the student you want to remove: ")
    if name in students_dict:
        del students_dict[name]
        students_list.remove(name)
        print(f"Student {name} removed successfully!")
    else:
        print("Student not found.")

while True:
    print("\n1. Add student\n2. Search student\n3. Remove student\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")