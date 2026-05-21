import csv

# Initial data
data = [
    ["Name", "Age", "City"],
    ["Kartiken", 21, "Dehradun"],
    ["Rahul", 22, "Delhi"],
    ["Aman", 20, "Mumbai"]
]

# Create CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file generated successfully!")


# rows = []
# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     rows = list(reader)
# rows[1][2] = "Meerut"  

# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

print("CSV file updated successfully!")