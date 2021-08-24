
def calc(x,y,o):
    if o == "+":
        print(x+y)
        return x + y
    elif o == "-":
        print(x-y)
        return x-y
    
    elif o == "*":
        print(x*y)
        return x*y
    
    elif o == "/":
        print(x/y)
        return x/y
    else:
        return("I didnt catch that, please enter the right value")
x = int(input("Enter a number "))
o = input("Enter an operator, + , -, *, / ")
y = int(input("Enter a number "))
calc(x,y,o)
