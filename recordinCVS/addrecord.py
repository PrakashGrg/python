import cvs

class Student:

    def __init__(self, roll, name, grade, age):
        self.roll = roll
        self.name = name
        self.grade = grade
        self.age = age


    def to_dict(self):
        return {'Roll': self.roll, 'Name': self.name, 'Grade': self.grade, 'Age': self.age}
def add_student_record(student):
    fieldnames = ['Roll', 'Name', 'Grade', 'Age']
    with open('students.csv', 'a', newline='') as csvfile:
        writer = cvs.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(student.to_dict())

if __name__ == "__main__":
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    age = input("Enter Age: ")

    student = Student(roll, name, grade, age)
    add_student_record(student)
    print("Student record added successfully.")
    