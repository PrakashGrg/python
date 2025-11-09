import csv

fields = ['Name', 'Marks']
rows = [
    ['Jester', 50],
    ['MAlla', 50],
    ['Jaddu', 70],
    ['Chet', 60]
]

filename = "students_marks.csv"

f = open(filename, 'w', newline='')
csvwriter = csv.writer(f)
csvwriter.writerow(fields)
csvwriter.writerows(rows)
f.close()

print("CSV file created successfully.")
