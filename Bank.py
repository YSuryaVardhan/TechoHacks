class ATMSimulator:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount or insufficient funds")

def atm_simulator():
    atm = ATMSimulator()
    while True:
        print("ATM Simulator")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thanks you for your transaction...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    atm_simulator()
