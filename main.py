import operator 

def main():
    #print out the intro to the program
    print_intro()
    #print the menu presented to the user
    print_operations()
    print(calculate())
    user_choice = ask()
    more_calculation(user_choice)
    

# -------------------------------------------------------

def print_intro():
    # This helper function will print out the intro to the program.
    print("Welcome to Karel's Calculator!")
    print("------------------------------")
    print(f"Help Karel with arithmetic!")

def print_operations():
    # This helper function will print the menu presented to the user.
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print()

def calculate():
    #This helper function will calculate according to the user's options
    operations = { 
        "1": operator.add,
        "2": operator.sub,
        "3": operator.mul,
        "4": operator.floordiv
    }
    operator_symbols = {
        operator.add: "+",
        operator.sub: "-",
        operator.mul: "*",
        operator.floordiv: "//",
    }
    user_operation = input("Which operation do you want to help Karel with?: ")
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
    operation = operations[user_operation]
    result = operation(first_number, second_number)
    return(f"{first_number} {operator_symbols[operation]} {second_number} results in {result}.")

def ask():
    print()
    user_choice = input("Do you want to perform another operation? (y/n): ")
    return user_choice

def more_calculation(user_choice):
    while user_choice == "y":
        print_operations()
        more_result = calculate()
        print(more_result)
        user_choice = ask()
             
    
if __name__ == "__main__":
    main()