import csv

# Step 1: Define student data
students = [
    ["J", "Math", 65],
    ["A", "Science", 75],
    ["C", "English", 45],
    ["K", "Computer", 90],
]

# Step 2: Define header fields
fields = ["Name", "Subject", "Marks"]

# Step 3: Write student data to 'students_marks.csv'
with open("students_marks.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(students)

print("students_marks.csv created successfully!")

# Step 4: Read and filter students with marks >= 60
with open("students_marks.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    filtered = [row for row in reader if int(row[2]) >= 60]

# Step 5: Write filtered data to 'students_plus_60.csv'
with open("students_plus_60.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(filtered)

print("students_plus_60.csv created successfully (marks >= 60).")