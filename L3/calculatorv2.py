def welcomeMessage():
    print(""" 
    Welcome dear user, to use the calculator we need some numbers. 
    1. Addition
    2. Multipy
    3. Substract
    4. Division
    """)

def displayResult(op):
    print("Result : ", op)

operantions  ={
    1: lambda a,b : a+b,
    2: lambda a,b : a*b,
    3: lambda a,b : a-b,
    4: lambda a,b : a/b,
}

def mainLoop():
    while True:
        oparant =int(input('Choose an operation: '))
        if oparant > len(operantions):
            print('Invalid operant. ')
            continue


        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter the secon number: '))
        result =  operantions[oparant](num1,num2)
        displayResult(result)

# Workflow
#1. Greeding tthe user
welcomeMessage()

#2. Starting the main loop
mainLoop()













