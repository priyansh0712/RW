data = []

def show_values(*values):
    """Display multiple values - demonstrates *args."""
    print("Values:", " ".join(str(v) for v in values))


def show_summary(**info):
    """Print dataset information - demonstrates **kwargs."""
    print("\nDataset Summary:")
    for key, value in info.items():
        print(f"- {key}: {value}")


def input_data():
    """User-defined function to input data."""
    global data  
    
    user_input = input("\Enter data for a 1D array (separated by spaces):\n")
    data = [float(x) for x in user_input.split()]  
    
    print("\nData has been stored successfully!")
    show_values(*data)  


def display_data_summary():
    """User-defined function demonstrating built-in functions."""
    if not data:
        print("No data available. Please input data first.")
        return
    
    #
    total = len(data)
    minimum = min(data)
    maximum = max(data)
    total_sum = sum(data)
    average = total_sum / total
    
    print("\nData Summary:")
    print(f"- Total elements: {total}")
    print(f"- Minimum value: {minimum}")
    print(f"- Maximum value: {maximum}")
    print(f"- Sum of all values: {total_sum}")
    print(f"- Average value: {round(average, 2)}")


def factorial(n):
    """Recursive function - function calling itself."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  


def calculate_factorial():
    """Calculate factorial using recursion."""
    number = int(input("\nEnter a number to calculate its factorial: "))
    result = factorial(number)
    print(f"Factorial of {number} is: {result}")


def filter_data():
    """Filter data using lambda function."""
    if not data:
        print("No data available. Please input data first.")
        return
    
    threshold = float(input("\nEnter a threshold value to filter data >= this value: "))
    
    filtered = list(filter(lambda x: x >= threshold, data))
    
    print(f"\nFiltered Data (values >= {threshold}):")
    print(", ".join(str(x) for x in filtered))


def sort_data():
    """Sort data in ascending or descending order."""
    if not data:
        print("No data available. Please input data first.")
        return
    
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")
    
    sorted_data = data.copy()
    if choice == "1":
        sorted_data.sort() 
        print("\nSorted Data in Ascending Order:")
    else:
        sorted_data.sort(reverse=True)  
        print("\nSorted Data in Descending Order:")
    
    print(", ".join(str(x) for x in sorted_data))


def calculate_stats(numbers):
    """Function that returns multiple values."""
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, round(average, 2)  


def display_statistics():
    """Display statistics using function that returns multiple values."""
    if not data:
        print("No data available. Please input data first.")
        return
    
    min_val, max_val, sum_val, avg_val = calculate_stats(data)
    
    print("\nDataset Statistics:")
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")
    print(f"- Sum of all values: {sum_val}")
    print(f"- Average value: {avg_val}")
    
    show_summary(min=min_val, max=max_val, sum=sum_val, average=avg_val)


def print_menu():
    """Display the main menu."""
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


def main():
    """Main program loop."""
    while True:
        print_menu()
        choice = input("\nPlease enter your choice: ")
        
        if choice == "1":
            input_data()
        elif choice == "2":
            display_data_summary()
        elif choice == "3":
            calculate_factorial()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            sort_data()
        elif choice == "6":
            display_statistics()
        elif choice == "7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 7.")
main()