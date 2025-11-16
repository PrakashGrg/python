import csv

fields = ['Name', 'Age', 'Marks']
rows = [
    ['Jester', 25, 70],
    ['MAlla', 35, 80],
    ['Jaddu', 28, 90],
    ['Chet', 20, 100]
]
for row in rows:
    name, age, marks = row
    print(f"{name} ({age} yrs): ", end="")
    if marks > 90:
        print("Distinction")
    elif marks > 80:
        print("First Division")
    elif marks > 70:
        print("Pass with Merit")
    elif marks < 100:
        print("Topper")
    else:
        print("Fail")

filename = "tech.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
