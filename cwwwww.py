from queue import Queue

def main():
    patient_queue = Queue()

    while True:
        print("\n1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = input("Enter the patient's name: ")
            patient_queue.put(patient_name)
            print(f"Patient {patient_name} registered successfully!")

        elif choice == '2':
            if not patient_queue.empty():
                print(f"Patient {patient_queue.get()} has met the doctor and has been removed from the queue.")
            else:
                print("No patients in the queue.")

        elif choice == '3':
            print("Current Patient Queue:")
            temp_queue = Queue()
            while not patient_queue.empty():
                patient_name = patient_queue.get()
                print(patient_name)
                temp_queue.put(patient_name)
            patient_queue = temp_queue

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()