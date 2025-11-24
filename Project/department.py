from datastore import departments

def add_department():
    name = input("Department name: ")
    departments.append(name)
    print("Department added.")

def list_departments():
    if not departments:
        print("No departments yet.")
    else:
        print("-- Departments --")
        for dept in departments:
            print(dept)
