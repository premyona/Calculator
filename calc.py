def add(x, y):
 return x + y

def subtract(x, y):
 return x - y

def multiply(x, y): 
 return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error"

VALID_OPS = {"+", "-", "*", "/", "."}

while True:
    print("\nEnter operation:+, -, *, / or .")
    op = input("Operation:")
    
    if op not in VALID_OPS:
     print("Invalid operator. Please enter one of +, -, *, / or . to exit.")
     continue
    
    if op == '.':
     break
    a = float(input("Enter number: "))
    b = float(input("Enter number: "))

    if op == '+':
     print("Result:", add(a, b))
    elif op == '-': 
     print("Result:", subtract(a, b))
    elif op == '*': 
     print("Result:", multiply(a, b))
    elif op == '/': 
     print("Result:", divide(a, b))
    else: 
     print("Invalid. Try again.")