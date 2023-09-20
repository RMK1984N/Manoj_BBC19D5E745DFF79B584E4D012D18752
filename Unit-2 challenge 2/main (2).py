class Bank_Account:
    def __init__(self): #initialize the const
        self.balance=5000
        print("Account holder name: Manoj kumar")
        print("ifc code:4262892736728")
        print("Hello!!! Welcome to the ATM Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrow:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
r=Bank_Account()
r.deposit()
r.withdraw()
r.display()