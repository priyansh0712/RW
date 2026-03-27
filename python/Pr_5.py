class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id=None, salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Programming Language:", self.programming_language)


def main():
    person_obj = None
    employee_obj = None
    manager_obj = None
    developer_obj = None

    print("issubclass(Manager, Employee):", issubclass(Manager, Employee))
    print("issubclass(Developer, Employee):", issubclass(Developer, Employee))

    while True:
        print("\n--- Employee Management System ---")
        print("1. Create Person")
        print("2. Create Employee")
        print("3. Create Manager")
        print("4. Create Developer")
        print("5. Show Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                person_obj = Person(name, age)
                print("Person created.")

            case "2":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                employee_obj = Employee(name, age, emp_id, salary)
                print("Employee created.")

            case "3":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                dept = input("Enter Department: ")
                manager_obj = Manager(name, age, emp_id, salary, dept)
                print("Manager created.")

            case "4":
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                lang = input("Enter Programming Language: ")
                developer_obj = Developer(name, age, emp_id, salary, lang)
                print("Developer created.")

            case "5":
                print("\n1. Person")
                print("2. Employee")
                print("3. Manager")
                print("4. Developer")
                sub_choice = input("Enter your choice: ")

                match sub_choice:
                    case "1":
                        person_obj.display() if person_obj else print("Person not created.")
                    case "2":
                        employee_obj.display() if employee_obj else print("Employee not created.")
                    case "3":
                        manager_obj.display() if manager_obj else print("Manager not created.")
                    case "4":
                        developer_obj.display() if developer_obj else print("Developer not created.")
                    case _:
                        print("Invalid choice.")

            case "6":
                print("Exiting program.")
                break

            case _:
                print("Invalid choice. Try again.")
main()