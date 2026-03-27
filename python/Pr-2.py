print("Welcome to pattern generator or number analyzer!")

while True:
    print("Select your choice : ")
    print("1. Generate a pattern")
    print("2. Analyze a range of number")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    match (choice):
        case 1:
            for i in range(5):
                print("*"*i)
        case 2:
            start = int(input("Enter start number: "))
            end = int(input("Entrer end number: "))
            for i in range(start,end+1):
                if i%2==0:
                    print(f"number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
        case 3:
            print("Exiting the program.Thankyou")
            break