from datastore import employees

def add_employee():
    name = input("Employee name: ")
    age = input("Employee age: ")
    dept = input("Department: ")
    emp = {
        "name": name,
        "age": age,
        "department": dept
    }
    employees.append(emp)
    print("Employee added.")

def list_employees():
    if len(employees) == 0:
        print("No employees found.")
    else:
        print("-- Employees --")
        for idx, emp in enumerate(employees, 1):
            print(f"{idx}. Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}")
