def calculator():
    while True:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /) or 'q' to quit: ")

        if op == 'q':
            print("Exiting the calculator.")
            break
        elif op == '+':
            print(f"Result: {x + y}")
        elif op == '-':
            print(f"Result: {x - y}")
        elif op == '*':
            print(f"Result: {x * y}")
        elif op == '/':
            print(f"Result: {x / y}" if y != 0 else "Cannot divide by zero")
        else:
            print("Invalid operation")

calculator()
