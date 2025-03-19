def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
      return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide (n1, n2):
    return  n1 / n2

operations={
    "+": add,
    "-": subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_accumulate=True
    first_number = float(input("What is your first number?"))
    while should_accumulate:
            for symbol in operations:
                print(symbol)
            operator = input(f"Pick an operation:")
            second_number = float(input("What is your second number?"))
            answer= operations[operator](first_number, second_number)
            print(answer)

            choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

            if choice == "y":
               first_number = answer

            else:
                    should_accumulate = False
                    print("\n" * 5)

calculator()