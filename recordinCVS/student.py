
import csv

# Step 1: Define the Student class
class Student:
    def __init__(self, roll, name, grade):
        self.roll = roll
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {'Roll': self.roll, 'Name': self.name, 'Grade': self.grade}

# Step 2: Write student records to CSV using DictWriter
def write_students(filename, students):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Roll', 'Name', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student.to_dict())

# Step 3: Update a student's value using their roll number (key)
def update_student(filename, roll_to_update, new_grade):
    updated_students = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Roll'] == roll_to_update:
                row['Grade'] = new_grade
            updated_students.append(row)

    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Roll', 'Name', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_students)

# Example usage
students = [
    Student('101', 'Alice', 'A'),
    Student('102', 'Bob', 'B'),
    Student('103', 'Charlie', 'C')
]

filename = 'students.csv'
write_students(filename, students)
update_student(filename, '102', 'A+')  # Update Bob's grade