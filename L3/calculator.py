def welcomeMessage():
    print(""" 
    Welcome dear user, to use the calculator we need some numbers. 
    1. Addition
    2. Multipy
    3. Substract
    4. Division
    """)

def add(a, b):
    displayResult((a+b))

def div(a, b):
    displayResult((a/b))

def sub(a, b):
    displayResult((a-b))

def mul(a, b):
    displayResult((a*b))

def displayResult(op):
    print("Result : ", op)

def mainLoop():
    while True:
        oparant = str(input('Choose an operation: '))
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter the secon number: '))

        if oparant =='1': 
            add(num1, num2)    
        if oparant =='2': 
            mul(num1, num2)    
        if oparant =='3': 
            sub((num1-num2))
        if oparant =='4': 
            div(num1, num2)


# Workflow
#1. Greeding tthe user
welcomeMessage()

#2. Starting the main loop
mainLoop()













