try:
    num1 = float(input("enter your first number : "))
    num2 = float(input("enter your second number : "))
    operation = input("give operation +,-,/,*  : ")
    if operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "/":
        print(num1/num2)
    elif operation == "*":
        print(num1*num2)
    else:
        print("invaild operation")
except:
    print("invaild input")
