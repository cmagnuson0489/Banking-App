class bankAccount:

    accountNumber = 0

    customerName = ""

    customerDeposit = 0

    type = ""

    def createAccount(self):

        self.accountNumber = int(input("Please enter your account number:"))

        self.name = input(
            "Please enter the account holder's first and last name:")

        self.type = input(
            "Please enter the account type such as Checking or Savings: ")

        self.customerDeposit = int(input(
            "Please enter the initial amount you would like to deposit:"))

        print("\n Congratulations your account has been created")
