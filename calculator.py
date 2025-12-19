import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(a)


print("=== Advanced Calculator ===")

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == "8":
        print("Calculator closed.")
        break

    if choice not in ["1","2","3","4","5","6","7"]:
        print("Invalid choice")
        continue

    if choice == "7":
        num = float(input("Enter number: "))
        print("Result:", square_root(num))
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print("Result:", power(num1, num2))
    elif choice == "6":
        print("Result:", modulus(num1, num2))
