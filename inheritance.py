class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying {self.course}.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting in the {self.department} department.")

# Example usage:
student1 = Student(name="Thukten Yezer", age=19, cid_number="10909000065", student_id="02230089", course="1 EE", year=2, gpa=3.3)
teacher1 = Teacher(name="Miss Tandin", age=24, cid_number="121123122", subject="CSF 101", salary=53000, department="IT", designation="Lecturer")

print(f"Student: {student1.name}, Age: {student1.age}, CID: {student1.cid_number}, Student ID: {student1.student_id}, Course: {student1.course}, Year: {student1.year}, GPA: {student1.gpa}")
student1.walk()
student1.study()
student1.attend_class()
student1.write_exam()
student1.eat()
student1.sleep()

print(f"\nTeacher: {teacher1.name}, Age: {teacher1.age}, CID: {teacher1.cid_number}, Subject: {teacher1.subject}, Salary: {teacher1.salary}, Department: {teacher1.department}, Designation: {teacher1.designation}")
teacher1.walk()
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()
teacher1.eat()
teacher1.sleep()