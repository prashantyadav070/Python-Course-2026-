## File Handling in python 


"""
==========================================
PYTHON FILE HANDLING - BASIC TO INTERMEDIATE
Single File Revision Code
Author: Prashant (Revision Purpose)
==========================================
"""

import os
import json
import csv
from datetime import datetime

print("===== PYTHON FILE HANDLING REVISION =====\n")

# ==========================================================
# 1️⃣ BASIC FILE CREATION & WRITING (Mode: 'w')
# Real World: Creating a simple notes file
# ==========================================================

print("1️⃣ Writing to file using 'w' mode")

with open("notes.txt", "w") as file:
    file.write("Welcome to File Handling Revision\n")
    file.write("This file is created using write mode.\n")
    file.write("Write mode overwrites existing content.\n")

print("notes.txt created successfully.\n")


# ==========================================================
# 2️⃣ APPENDING DATA (Mode: 'a')
# Real World: Adding new log entries
# ==========================================================

print("2️⃣ Appending new data using 'a' mode")

with open("notes.txt", "a") as file:
    file.write("This line is appended.\n")

print("Data appended successfully.\n")


# ==========================================================
# 3️⃣ READING FILE (Mode: 'r')
# read(), readline(), readlines()
# ==========================================================

print("3️⃣ Reading file content")

with open("notes.txt", "r") as file:
    print("Using read():")
    print(file.read())

with open("notes.txt", "r") as file:
    print("Using readline():")
    print(file.readline())

with open("notes.txt", "r") as file:
    print("Using readlines():")
    print(file.readlines())

print()


# ==========================================================
# 4️⃣ EXCLUSIVE FILE CREATION (Mode: 'x')
# Error if file already exists
# ==========================================================

print("4️⃣ Exclusive file creation using 'x'")

try:
    with open("unique.txt", "x") as file:
        file.write("This file is created only if it doesn't exist.\n")
    print("unique.txt created successfully.\n")
except FileExistsError:
    print("unique.txt already exists.\n")


# ==========================================================
# 5️⃣ READ + WRITE MODE ('r+')
# Modify existing file
# ==========================================================

print("5️⃣ Using 'r+' mode")

with open("notes.txt", "r+") as file:
    content = file.read()
    file.write("\nAdded using r+ mode.\n")

print("r+ operation completed.\n")


# ==========================================================
# 6️⃣ CHECK IF FILE EXISTS
# ==========================================================

print("6️⃣ Checking file existence")

if os.path.exists("notes.txt"):
    print("notes.txt exists.\n")
else:
    print("notes.txt does not exist.\n")


# ==========================================================
# 7️⃣ DELETE FILE
# ==========================================================

print("7️⃣ Deleting a temporary file")

if os.path.exists("unique.txt"):
    os.remove("unique.txt")
    print("unique.txt deleted.\n")


# ==========================================================
# 8️⃣ REAL WORLD PROJECT: EXPENSE LOGGER
# ==========================================================

print("8️⃣ Real World Example: Expense Logger")

expense_file = "expenses.txt"

def add_expense(amount, category):
    with open(expense_file, "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date} | {category} | ₹{amount}\n")

def view_expenses():
    if os.path.exists(expense_file):
        with open(expense_file, "r") as file:
            print("\nExpense History:")
            print(file.read())
    else:
        print("No expenses found.\n")

add_expense(200, "Food")
add_expense(500, "Travel")
view_expenses()


# ==========================================================
# 9️⃣ CSV FILE HANDLING
# Real World: Student Marks Storage
# ==========================================================

print("9️⃣ Working with CSV file")

csv_file = "students.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Prashant", 85])
    writer.writerow(["Rahul", 90])

print("CSV file created.\n")

with open(csv_file, "r") as file:
    reader = csv.reader(file)
    print("Reading CSV:")
    for row in reader:
        print(row)

print()


# ==========================================================
# 🔟 JSON FILE HANDLING
# Real World: User Data Storage
# ==========================================================

print("🔟 Working with JSON file")

user_data = {
    "name": "Prashant",
    "age": 21,
    "skills": ["Python", "DSA", "Backend"]
}

# Writing JSON
with open("user.json", "w") as file:
    json.dump(user_data, file, indent=4)

print("JSON file created.\n")

# Reading JSON
with open("user.json", "r") as file:
    data = json.load(file)
    print("Reading JSON Data:")
    print(data)

print("\n===== FILE HANDLING REVISION COMPLETED =====")
