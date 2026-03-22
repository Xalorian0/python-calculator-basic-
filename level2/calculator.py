while True:
    try:
        num1 = float(input("enter your first number : "))
        num2 = float(input("enter your second number : "))
        operation = input("give operation +,-,/,*, : ")
        if operation == "+":
            print(f"{num1} + {num2} = {num1+num2}")
        elif operation == "-":
            print(f"{num1} - {num2} = {num1-num2}")
        elif operation == "/":
            if num2 == 0:
                print("number cannot be divisible by 0")
            else:
                print(f"{num1} * {num2} = {num1/num2}")
        elif operation == "*":
            print(f"{num1} * {num2} = {num1*num2}")
        else :
            print("Invaild operation")
        choice = input("Should we countinue ? type (yes/no) : ")
        if choice == "no":
            break
    except ValueError:
        print("invaild input")
