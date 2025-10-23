#try:
#    numerator = float(input("Enter the numerator: "))
#    denominator = float(input("Enter the denominator: "))
#    if denominator == 0:
#        print("Error: Denominator cannot be zero.")
#    else:
#        percentage = (numerator / denominator) * 100
#        print(f"The percentage is: {percentage:.2f}%")
#except ValueError:
#    print("Invalid input. Please enter numbers.")


def print_options():
    print("Select an option:")
    print("1. Say Hello")
    print("2. Calculate Square of a Number")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice.isdigit() and 1 <= int(choice) <= 3:
        return int(choice)
    else:
        print("Invalid choice. Please try again.")
        return None
    
def Say_hello():
       print("Hello, User!")   

def calculate_square():
        num = input("Enter a number to calculate its square: ")
        if num.replace('.','',1).isdigit():
            number = float(num)
            square = number ** 2
            print(f"The square of {number} is {square}.")
        else:
            print("Invalid input. Please enter a numeric value.")    

options = print_options()
while(options):
    options = print_options()
    match(options):
        case 1:
            Say_hello()
            
            
        case 2:
            calculate_square()
            
        case 3:
            print("bye")
            break



