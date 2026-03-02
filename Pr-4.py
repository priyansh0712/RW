print("Welcome to data analyzer")
print("Main menu")
while True:
    print("1. Input data")
    print("2. Display summary")
    print("3. calculate factorial")
    print("4. Filter data ")
    print("5. sort data")
    print("6. Display Dataset Statistics")
    print("7. Exit")
    choice = int(input("Enter Your choice : "))
    match(choice):
        case 1:
            data = input("Enter data for 1D Array (saparate by space)").split()
            print("Data has been store successfully!")
        case 2:
            print("Data summary:")
            print(f"Total Element : {len(data)}")
            print(f"Max value : {max(data)}")
            print(f"Min value : {min(data)}")
            print(f"Sum of all value : {sum(data)}")
            print(f"Avg of all value : {sum(data)/len(data)}")
        case 3:
            no = int(input("Enter number : "))
            def fact(no):
                if no==0:
                    return 1
                else:
                    return no*fact(no-1)
            print(f"Fact of {no} is {fact(no)}")
        case 4:
            val = input("Enter a threshold value to filter out data above this value : ")
            final = list(filter(lambda x: x >= val,data))
            print("Filterd data : ",final)
        case 5:
            print("Choose sorting option:")
            while True:
                print("1. Ascending")
                print("2. Descending")
                schoice = int(input("Enter your choice: "))
                match schoice:
                    case 1:
                        print("Sorted data in Ascending")
                        print(data.sort())
                    case 2:
                        print("Sorted data in Descending")
                        print(data.sort(reverse=True))
        case 6:
            print(f"Max value : {max(data)}")
            print(f"Min value : {min(data)}")
            print(f"Sum of all value : {sum(data)}")
            print(f"Avg of all value : {sum(data)/len(data)}")
        case 7:
            print("Thank you for using data Analyzer.Good bye!")
            break