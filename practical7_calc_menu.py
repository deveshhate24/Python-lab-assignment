def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero not allowed"
    return a % b

def menu():
    print("\n---- CALCULATOR MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 6:
            print("Exiting...")
            break

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        elif choice == 5:
            n1 = int(input("Enter first integer: "))
            n2 = int(input("Enter second integer: "))
            print("Result:", modulus(n1, n2))
        else:
            print("Invalid choice")

main()