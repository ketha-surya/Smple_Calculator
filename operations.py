#operations 

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "error"
    else:
        return a/b
    
def power(a, b):
    return a ** b

def modulo(a,b):
    if b==0:
        return "ZeroDivisionError"
    else:
     return a%b


    

