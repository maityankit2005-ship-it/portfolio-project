def append_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")

    with open("employees.txt", "a") as file:
        file.write(emp_id + "," + name + "," + salary + "\n")

    print("Employee Added Successfully!\n")

def display_employees():
    print("\n--- All Employee Records ---")
    try:
        with open("employees.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No employee records found.\n")
            else:
                for line in data:
                    emp_id, name, salary = line.strip().split(",")
                    print(f"ID: {emp_id}, Name: {name}, Salary: {salary}")

    except FileNotFoundError:
        print("employees.txt file not found.\n")

def search_employee():
    search_name = input("Enter employee name to search: ")

    found = False

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, name, salary = line.strip().split(",")
                if name.lower() == search_name.lower():
                    print("\nEmployee Found:")
                    print(f"ID: {emp_id}, Name: {name}, Salary: {salary}\n")
                    found = True
                    break

        if not found:
            print("Employee not found.\n")

    except FileNotFoundError:
        print("employees.txt file does not exist.\n")

while True:
    print(" Employee File Operations")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by Name")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        append_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
