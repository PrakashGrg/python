import csv

# Define the header and rows
fields = ['Name', 'Age', 'City']
rows = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Specify the filename
filename = "people.csv"

# Write to the CSV file
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header
    csvwriter.writerow(fields)
    
    # Write the data rows
    csvwriter.writerows(rows)