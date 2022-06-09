import random
# Generate 5 random numbers between 1 and 10
randomlist = random.sample(range(1, 10), 6)
accountNumber = ''.join(str(randomlist).split(','))


class bankAccount:

    customerName = ""

    customerDeposit = 0

    type = ""

    def createAccount(self):

        self.name = input(
            "Please enter the account holder's first and last name:")

        self.type = input(
            "Please enter the account you would like to access such as Checking, Savings, Money Market: ")

        self.customerDeposit = int(input(
            "Please enter the amount you would like to deposit in your account:"))

        print("\n Congratulations! Your account has been created")

    def displayAccount(self):

        print("Account Holder's Name: ", self.name)

        print("Type of Account:", self.type)

        print("Balance:", self.deposit)


def modifyAccount(self):

    self.name = input("Modify the Account Holder's name: ")

    self.type = input(
        "Modify the type of Account(checking, savings, money market): ")
