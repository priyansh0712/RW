print("Welcome to the interactive personal data collector!")

name = input("Enter your name: ")
age = int(input("Enter yout age: "))
height = input("Enter your height: ")
height = float(height)
number = int(input("Enter your favourite number: "))

print("Thank you! Here is the information we collected: ")
print(f"Name : {name} ({type(name)},{id(name)})")
print(f"Name : {age} ({type(age)},{id(age)})")
print(f"Name : {height} ({type(height)},{id(height)})")
print(f"Name : {number} ({type(number)},{id(number)})")

print(f"Your birth year is: {2026-age}")
print("Thankyou!")