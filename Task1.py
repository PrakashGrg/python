import csv

fields = ['Name', 'Age', 'Marks']
rows = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print(f"\nStudent {i+1}:")
    name = input("Enter name: ",)
    age = int(input("Enter age: ",))
    marks = float(input("Enter marks: ",))
    rows.append([name, age, marks])

filename = "students_input.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print("\nCSV file 'students_input.csv' created successfully.")
