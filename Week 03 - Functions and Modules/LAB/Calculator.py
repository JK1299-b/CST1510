def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return n1 / n2 if n2 != 0 else "Error: Division by zero"

n1 = float(input("Enter first number: "))
keep_going = True

while keep_going:
    operator = input("Enter an operator (+ - * /): ").strip()
    n2 = float(input("Enter second number: "))
    
    if operator == "+": result = add(n1, n2)
    elif operator == "-": result = subtract(n1, n2)
    elif operator == "*": result = multiply(n1, n2)
    elif operator == "/": result = divide(n1, n2)
    else: result = "Invalid Operator"
        
    print(f"{n1} {operator} {n2} = {result}")
    
    if isinstance(result, str):
        n1 = float(input("\nEnter a new first number: "))
        continue

    choice = input("Type 'y' to continue with the result, or 'n' to start over: ").lower().strip()
    if choice == "y":
        n1 = result
    else:
        n1 = float(input("\nEnter a new first number: "))
