from datetime import datetime
import time
import math
import random
import uuid
import os
import string


def display_current_datetime():
    now = datetime.now()
    print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_date_difference():
    try:
        date1 = input("Enter the first date (YYYY-MM-DD): ").strip()
        date2 = input("Enter the second date (YYYY-MM-DD): ").strip()

        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")

        diff = abs((d2 - d1).days)
        print("Difference in days:", diff)
    except ValueError:
        print("Invalid date format.")


def format_custom_date():
    try:
        date_str = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ").strip()
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        print("\nChoose format:")
        print("1. DD-MM-YYYY")
        print("2. Month DD, YYYY")
        print("3. HH:MM:SS AM/PM")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Formatted Date:", dt.strftime("%d-%m-%Y"))
        elif choice == "2":
            print("Formatted Date:", dt.strftime("%B %d, %Y"))
        elif choice == "3":
            print("Formatted Time:", dt.strftime("%I:%M:%S %p"))
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid date-time format.")


def stopwatch():
    input("\nPress Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    end = time.time()

    elapsed = end - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")


def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: ").strip())
        while seconds > 0:
            print(f"Time left: {seconds} seconds", end="\r")
            time.sleep(1)
            seconds -= 1
        print("\nTime's up!")
    except ValueError:
        print("Please enter a valid integer.")


def datetime_menu():
    while True:
        print("\n" + "=" * 35)
        print("Datetime and Time Operations")
        print("=" * 35)
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            calculate_date_difference()
        elif choice == "3":
            format_custom_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


def calculate_factorial():
    try:
        n = int(input("Enter a number: ").strip())
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial:", math.factorial(n))
    except ValueError:
        print("Invalid input.")


def solve_compound_interest():
    try:
        principal = float(input("Enter principal amount: ").strip())
        rate = float(input("Enter rate of interest (in %): ").strip())
        time_period = float(input("Enter time (in years): ").strip())

        amount = principal * ((1 + rate / 100) ** time_period)
        print(f"Compound Interest Amount: {amount:.2f}")
    except ValueError:
        print("Invalid input.")


def trigonometric_calculations():
    try:
        degree = float(input("Enter angle in degrees: ").strip())
        rad = math.radians(degree)

        print(f"sin({degree}) = {math.sin(rad):.4f}")
        print(f"cos({degree}) = {math.cos(rad):.4f}")
        print(f"tan({degree}) = {math.tan(rad):.4f}")
    except ValueError:
        print("Invalid input.")


def logarithm_calculation():
    try:
        num = float(input("Enter a positive number: ").strip())
        if num <= 0:
            print("Logarithm only works for positive numbers.")
            return
        print(f"Natural log of {num}: {math.log(num):.4f}")
        print(f"Base-10 log of {num}: {math.log10(num):.4f}")
    except ValueError:
        print("Invalid input.")


def area_of_shapes():
    print("\nChoose shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            radius = float(input("Enter radius: ").strip())
            area = math.pi * radius * radius
            print(f"Area of Circle: {area:.2f}")
        elif choice == "2":
            length = float(input("Enter length: ").strip())
            width = float(input("Enter width: ").strip())
            area = length * width
            print(f"Area of Rectangle: {area:.2f}")
        elif choice == "3":
            base = float(input("Enter base: ").strip())
            height = float(input("Enter height: ").strip())
            area = 0.5 * base * height
            print(f"Area of Triangle: {area:.2f}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")


def unit_conversion():
    print("\nChoose conversion:")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")

    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            km = float(input("Enter kilometers: ").strip())
            print(f"Miles: {km * 0.621371:.2f}")
        elif choice == "2":
            c = float(input("Enter temperature in Celsius: ").strip())
            print(f"Fahrenheit: {(c * 9/5) + 32:.2f}")
        elif choice == "3":
            kg = float(input("Enter weight in kilograms: ").strip())
            print(f"Pounds: {kg * 2.20462:.2f}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")


def math_menu():
    while True:
        print("\n" + "=" * 35)
        print("Mathematical Operations")
        print("=" * 35)
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Logarithm Calculations")
        print("5. Area of Geometric Shapes")
        print("6. Unit Conversion")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculate_factorial()
        elif choice == "2":
            solve_compound_interest()
        elif choice == "3":
            trigonometric_calculations()
        elif choice == "4":
            logarithm_calculation()
        elif choice == "5":
            area_of_shapes()
        elif choice == "6":
            unit_conversion()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")


def generate_random_number():
    try:
        start = int(input("Enter starting number: ").strip())
        end = int(input("Enter ending number: ").strip())
        print("Random Number:", random.randint(start, end))
    except ValueError:
        print("Invalid input.")


def generate_random_list():
    try:
        size = int(input("Enter size of list: ").strip())
        start = int(input("Enter minimum value: ").strip())
        end = int(input("Enter maximum value: ").strip())

        random_list = [random.randint(start, end) for _ in range(size)]
        print("Random List:", random_list)
    except ValueError:
        print("Invalid input.")


def create_random_password():
    try:
        length = int(input("Enter password length: ").strip())
        if length <= 0:
            print("Length must be greater than 0.")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input.")


def generate_random_otp():
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)


def random_sampling():
    data = input("Enter items separated by commas: ").strip().split(",")
    data = [item.strip() for item in data if item.strip()]

    if not data:
        print("Dataset is empty.")
        return

    try:
        sample_size = int(input("Enter sample size: ").strip())
        if sample_size > len(data):
            print("Sample size cannot be greater than dataset size.")
            return

        sample = random.sample(data, sample_size)
        print("Random Sample:", sample)
    except ValueError:
        print("Invalid input.")


def random_menu():
    while True:
        print("\n" + "=" * 35)
        print("Random Data Generation")
        print("=" * 35)
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling from Dataset")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            create_random_password()
        elif choice == "4":
            generate_random_otp()
        elif choice == "5":
            random_sampling()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


def generate_uuid():
    unique_id = uuid.uuid4()
    print("Generated UUID:", unique_id)


def uuid_menu():
    while True:
        print("\n" + "=" * 35)
        print("Generate Unique Identifiers (UUID)")
        print("=" * 35)
        print("1. Generate UUID")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_uuid()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")


def create_file():
    filename = input("Enter file name: ").strip()
    try:
        with open(filename, "w") as file:
            pass
        print("File created successfully!")
    except Exception as e:
        print("Error:", e)


def write_file():
    filename = input("Enter file name: ").strip()
    data = input("Enter data to write: ")

    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Data written successfully!")
    except Exception as e:
        print("Error:", e)


def read_file():
    filename = input("Enter file name: ").strip()

    try:
        with open(filename, "r") as file:
            content = file.read()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)


def append_file():
    filename = input("Enter file name: ").strip()
    data = input("Enter data to append: ")

    try:
        with open(filename, "a") as file:
            file.write(data + "\n")
        print("Data appended successfully!")
    except Exception as e:
        print("Error:", e)


def update_file_content():
    filename = input("Enter file name: ").strip()

    if not os.path.exists(filename):
        print("File not found.")
        return

    old_text = input("Enter text to replace: ")
    new_text = input("Enter new text: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        content = content.replace(old_text, new_text)

        with open(filename, "w") as file:
            file.write(content)

        print("File updated successfully!")
    except Exception as e:
        print("Error:", e)


def file_menu():
    while True:
        print("\n" + "=" * 35)
        print("File Operations")
        print("=" * 35)
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Update File Content")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            update_file_content()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


def explore_module_attributes():
    print("\nExplore Module Attributes")
    module_name = input("Enter module name to explore: ").strip()

    try:
        module = __import__(module_name)
        print(f"\nAvailable attributes in {module_name}:")
        print(dir(module))
    except ModuleNotFoundError:
        print("Module not found.")
    except Exception as e:
        print("Error:", e)


def main_menu():
    while True:
        print("\n" + "=" * 35)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 35)
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module_attributes()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
