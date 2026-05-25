def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

print("Simple Calculator")
num1 = float(input("Enter first number: "))
print("Result:", add(num1, num2))

choice = '4'
while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError as e:
        print(e)

result = divide(num1, num2)
if choice == '4':
    print(result)