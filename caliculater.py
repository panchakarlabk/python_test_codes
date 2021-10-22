def caleculate():
    num1 = float(input("Enter a first Number :"))
    num2 = float(input("Enter secound  number  number : "))
    op = input("Enter operator :")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid Operator")

caleculate()