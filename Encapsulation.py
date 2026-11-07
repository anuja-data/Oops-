class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def display(self):
        print("Total Balance:", self.__balance)

# Creating object
b = BankAccount(5000)

b.deposit(2000)
b.display()

