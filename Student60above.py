import csv

f = open("students_marks.csv", 'r')
reader = csv.reader(f)
header = next(reader)
filtered = [row for row in reader if int(row[1]) >= 60]
f.close()

f = open("students_above_60.csv", 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
writer.writerows(filtered)
f.close()

print("Filtered CSV created.")

