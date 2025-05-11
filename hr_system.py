import csv
import os

FILENAME = 'Employee.csv'

# Ensure the file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Name', 'Age', 'Department', 'Position', 'Salary'])

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    dept = input("Enter Department: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, age, dept, position, salary])
    print("✅ Employee added successfully!\n")

def view_all_employees():
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    print()

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == emp_id:
                print("🎯 Employee Found:", row)
                found = True
                break
    if not found:
        print("❌ Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    rows = []
    deleted = False
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != emp_id:
                rows.append(row)
            else:
                deleted = True
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    if deleted:
        print("🗑️ Employee deleted successfully!\n")
    else:
        print("❌ Employee ID not found.\n")

def menu():
    while True:
        print("\n HR Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_all_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("👋 Exiting...")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
