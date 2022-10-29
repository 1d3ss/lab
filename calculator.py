x = "y"

while x == "y":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = input("Enter a symbol(+, -, *, /): ")

    if c == "+":
        print("Result: ", a + b)
    elif c == "-":
        print("Result: ", a - b)
    elif c == "*":
        if b == 0:
            print("Action is impossible!")
        elif a == 0:
            print("Action is impossible!")
        else:
            print("Result: ", a * b)
    elif c == "/":
        if b == 0:
            print("Action is impossible!")
        elif a == 0:
            print("Action is impossible!")
        else:
            print("Result: ", a / b)
    else:
        print("Wrong operation selected!")
    x = input("Type 'y' to continue or another key to exit: ")
