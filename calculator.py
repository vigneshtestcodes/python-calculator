def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Can't divide by zero."
    return a / b

print("Simple Calculator")
print("Operations: +  -  *  /")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Answer:", add(num1, num2))
elif operator == "-":
    print("Answer:", subtract(num1, num2))
elif operator == "*":
    print("Answer:", multiply(num1, num2))
elif operator == "/":
    print("Answer:", divide(num1, num2))
else:
    print("Invalid operator!")