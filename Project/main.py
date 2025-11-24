from employee import * 
from department import * 
from task import *
from datastore import *
import random
import statistics

print(" ")
print("--- WELCOME TO THE OFFICE ---")
print("")
print("1. Office Management System 🏢")
print("2. Monthly Expense Calculator 💸")
print("3. Lucky Draw Winner 🪙")

opt=int(input("ENTER THE CHOICE:   "))

if opt == 1:
    while True:
        print("--- Office Management System ---")
        print("")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Add Department")
        print("4. List Departments")
        print("5. Add Task")
        print("6. List Tasks")
        print("0. Exit")
        opt1 = input("Enter choice: ")
        print("")

        if opt1 == "1":
            add_employee()
        elif opt1 == "2":
            list_employees()
        elif opt1 == "3":
            add_department()
        elif opt1 == "4":
            list_departments()
        elif opt1 == "5":
            add_task()
        elif opt1 == "6":
            list_tasks()
        elif opt1 == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

elif opt == 2:
    print("--- Monthly Expense Calculator ---")
    print("")
    print("Choose the Department :  ")
    print("1. Technical")
    print("2. Finance")
    print("3. Cleaning")
    print("4. Exit")
    opt2=int(input("Enter Choice :"))
    
    def option(l):
        while True:
            print("")
            print("--- Choose the Operation ---")
            print("1. Average Salary")
            print("2. Total Salary")
            print("3. Minimum Salary")
            print("4. Maximum Salary")
            print("5. Exit")
            sal=int(input("Choose : "))
            print("")

            if sal == 1:
                print(" Average Salary is : ",statistics.mean(l))
            elif sal == 2:
                print("Total Salary is : ",sum(l))
            elif sal == 3:
                print("Minimum Salary is :",min(l))
            elif sal == 4:
                print("Maximum Salary is : ",max(l))
            elif sal == 5:
                print("GoodBye !")
                break
            

    if opt2 == 1:
        tech=[]
        for i in employees:
            if i["department"] == "Technical":
                tech.append(i["salary"])
        option(tech)
    
    elif opt2 == 2:
        fin=[]
        for i in employees:
            if i["department"] == "Finance":
                fin.append(i["salary"])
                option(fin)

    elif opt2 == 3:
        clean=[]
        for i in employees:
            if i["department"] == "Cleaning":
                clean.append(i["salary"])
                option(clean)
    
    elif opt2 == 4:
        print("GoodBye!")

    else:
        print("Invalid input. Try again.")

elif opt == 3:
    print("--- Lucky Draw Winner ---")
    print("")
    name = []
    for i in employees:
        name.append(i["name"])
    print("\n🎉✨ And the moment we've all been waiting for... ✨🎉")
    print("💫✨ Congratulations to the lucky star of the day:  "," >>-- " ,random.choice(name).upper())


    


else:
    print("-- Please, Enter a Valid Option --")





    
        









