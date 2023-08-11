class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}. Current balance: ${self.balance:.2f}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


def main():
    accounts = {}

    while True:
        print("\n===== Simple Banking Application =====")
        print("1. Create an account")
        print("2. Request account information")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                print("Account already exists. Please choose another account number.")
            else:
                accounts[account_number] = BankAccount(account_number)
                print("Account created successfully.")

        elif choice == "2":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                print(f"Account Number: {account.account_number}")
                print(f"Current Balance: ${account.get_balance():.2f}")
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            else:
                print("Account not found. Please check your account number.")

        elif choice == "3":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                amount = float(input("Enter the amount to deposit: $"))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found. Please check your account number.")

        elif choice == "4":
            account_number = input("Enter your account number: ")
            if account_number in accounts:
                amount = float(input("Enter the amount to withdraw: $"))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found. Please check your account number.")

        elif choice == "5":
            print("Thank you for using the Simple Banking Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")


if __name__ == "__main__":
    main()
