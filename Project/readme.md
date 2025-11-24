# Office Management System

A simple Python-based office management system for beginners. Manages employees, departments, and tasks—with all storage in memory (no databases). This project is built as a student assignment to demonstrate basic Python programming concepts and simple modular coding without external libraries.


## Table of Contents

- [About the Project]
- [Motivation]
- [Features]
- [Technology Stack]
- [Prerequisites]
- [Project Structure]
- [Getting Started]
- [Usage]
- [Sample Session]
- [Code Structure]
- [Known Limitations]
- [Possible Improvements]
- [Author]
- [License]

## About the Project

This Office Management System provides a basic command-line interface to manage Employees, Departments, and Tasks. It imitates typical office software on a much smaller educational scale—so it's great for first-year computer science courses or Python self-study.

All data is stored in Python lists and dictionaries while the program runs. No files are created/loaded; the aim is to focus on logic, modularization, and interactive terminal input/output.

## Motivation

This project was created to:
- Practice splitting programs into multiple files/modules.
- Learn about Python functions, data structures, and user interaction.
- Experience troubleshooting and fixing import, syntax, and runtime errors.
- Submit as a semester or classroom assignment.

## Features

- **Add Employees**: Enter new employee details (name, age, department).
- **List Employees**: Print all employees and their info.
- **Add Departments**: Create new departments for organizing the office.
- **List Departments**: View all existing departments.
- **Add Tasks**: Assign simple tasks to employees.
- **List Tasks**: Print all tasks and who they are assigned to.
- Clean and simple text menu interface driven by numbered choices.
- No advanced features (no file save/load, no GUI, no SQL/database).

## Technology Stack

- **Programming Language**: Python 3 (tested with 3.8+)
- **Libraries**: None (no third-party libraries required)
- **Platform**: Any OS with Python 3 installed

## Prerequisites

- Python 3.8 or newer installed.
- Command-line or terminal access.

## Project Structure

```
office_management/
│
├── main.py         # Responsible for the menu and navigation
├── employee.py     # Employee management logic
├── department.py   # Department management logic
├── task.py         # Task management logic
├── datastore.py    # In-memory lists for employees, departments, tasks
├── README.md       # Project documentation
```

## Getting Started

### 1. Download

1. Download or clone this repository (or just these five `.py` files and this `README.md`).
2. Place all files in a single directory/folder.

### 2. Run

In your terminal, navigate to where the files are and run:

```sh
python main.py
```

The main menu will appear, allowing you to choose actions using numbers.

## Usage

Once the program is running:

- Type the number for your chosen action (like `1` for Add Employee).
- Follow prompts to enter details (name, age, department, etc.).
- Data will remain only until you exit (closing the program loses all info).

## Sample Session

```
-- Office Management System --
1. Add Employee
2. List Employees
3. Add Department
4. List Departments
5. Add Task
6. List Tasks
0. Exit
Enter choice: 1
Employee name: Alice
Employee age: 24
Department: HR
Employee added.
```

## Code Structure

- **main.py**: Entry point; shows menu, gathers user input, calls functions from the other modules.
- **employee.py**: `add_employee` and `list_employees` functions. Accesses employees stored in `datastore.py`.
- **department.py**: Functions for adding/listing departments. Works with the `departments` list in `datastore.py`.
- **task.py**: Functions for adding/listing tasks (keeping things basic and readable).
- **datastore.py**: Simple lists (employees, departments, tasks) for in-memory storage.

## Known Limitations

- **No persistent storage:** All entries are lost upon exiting.
- **No data validation:** Input is accepted as typed (no checks for duplicates or errors).
- **No delete/edit options:** Items can only be added and listed, not modified or removed.
- **No user authentication or security.**
- **No GUI or web interface—command line only.**

## Possible Improvements

- Add file saving/loading so data is not lost.
- Allow deleting or editing employees, departments, or tasks.
- Add input validation (check age as integer, department exists, etc.).
- Add user authentication (login system).
- Convert to a GUI app or web app in the future.

## Author
- Created by AASHUTOSH SHARMA.
- This project was created as a learning example and assignment submission.  
- Feel free to use, learn from, or adapt for your own educational needs.

## License

This project is provided for educational purposes only.

