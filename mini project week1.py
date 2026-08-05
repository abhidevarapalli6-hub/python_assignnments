PIN = 1234
balance = 10000

def check_balance():
    print("Current Balance = ₹", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount Deposited Successfully")
    print("New Balance = ₹", balance)

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Remaining Balance = ₹", balance)
    else:
        print("Insufficient Balance")

pin = int(input("Enter PIN: "))

if pin == PIN:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")
