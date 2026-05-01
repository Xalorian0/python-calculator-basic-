import time
time.sleep(0.5)
print(r"""   ____                                _____      _            _       _             
  / __ \                              / ____|    | |          | |     | |            
 | |  | |_ __ ___   ___  __ _  __ _  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |  | | '_ ` _ \ / _ \/ _` |/ _` | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| | | | | | |  __/ (_| | (_| | | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \____/|_| |_| |_|\___|\__, |\__,_|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                         __/ |                                                       
                        |___/                                                        """)
menu = (r"""
    ***********Operations***********

    [1] Add            [2] Subtract  [5] Power       [7] History
    [3] Multiply       [4] Divide    [6] Percentage  [8] Exit  


""")
print(menu)
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def divide(a,b):
    if b == 0:
            print("Number is not divisble by 0")
            return None
    else:
        return(a/b)
def multiply(a,b):
    return(a*b)
def Power(a, b):
    return(a ** b)
def perc(a,b):
    return(a * b)/100


operations = { "1" : add ,
  "2" : subtract,
  "3" : multiply,
  "4" : divide,
  "5" : Power,
  "6" : perc

}

markers = { "1" : "+",
 "2" : "-",
 "3" : "*",
 "4" : "/",
 "5" : "^",
 "6" : "%" 
}

History = []
last_result = 0

while True:
    Choice = (input("Plz Enter Your Choice : ")).lower().strip()
    
    if Choice in operations:
        try:
            a =float(input("Enter your first number : "))
            b =float(input("Enter your second number : "))
            result = (operations[Choice](a,b))
            if result is not None:
                print(f"{a} {markers[Choice]} {b} = ",result)
                History.append(f". {a} {markers[Choice]} {b} = {result}")
                last_result = result
                Choice1 = input("Do you want to Continue (Y/N) : ").strip()
                if Choice1 == "Y":
                    print(menu)
                    print("Last Result = ",last_result)
                    x = input("Do you wanna use Last Result (Y/N) : ").strip()
                    if x == "Y":
                        Choice = (input("Enter Your Choice : ")).lower().strip()
                        a = last_result
                        b = float(input("Enter your new number : "))
                        result = (operations[Choice](a,b))
                        print(f"{a} {markers[Choice]} {b} = ",result)
                        History.append(f". {a} {markers[Choice]} {b} = {result}")
                    if x =="N":
                        Choice= (input("Enter Your Choice : ")).lower().strip()
        except ValueError:
            print("Invaild Operation")
    elif Choice == "7":
        if History == []:
            print("No History Yet")
        else:
            for i,item in enumerate(History,start=1):
                print(i,item)
    elif Choice == "8":
        print("You have successfully exited")
        break
    else:
        print("Plz Enter Valid Input")
        continue
    
