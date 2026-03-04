def show_balance(balance):
    print("Current Balance:", balance)

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Updated Balance:", balance)
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Updated Balance:", balance)
    return balance

def menu():
    print("\n---- BANK MENU ----")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def main():
    balance = 1000.0

    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            print("Thank you")
            break
        else:
            print("Invalid choice")

main()