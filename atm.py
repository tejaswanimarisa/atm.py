# Simple ATM Program

balance = 1000  # Initial balance

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful!")
        print("New balance is:", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance is:", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice! Please try again.")