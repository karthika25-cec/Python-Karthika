class BankAccount:
    def __init__(self,acc_no,name,acc_type,balance=0.0):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
        self.acc_type=acc_type
    def deposit (self,amount):
            if amount>0:
                self.balance +=amount
                print(f"Rs.{amount} Deposited successfully")
            else:
                print("Enter valid amount")
    def withdraw (self,amount):
             if amount <=0:
                 print("withdraw amount must be positive")
             elif amount>self.balance:
                 print("insufficient balance")
             else:
                 self.balance=amount
                 print(f"Rs,{amount}withdraw successfully")
    def display(self):
            print("-----Account Detals----")
            print(f"Account Number:{self.acc_no}")
            print(f"Name:{self.name}")
            print(f"Account Type:{self.acc_type}")
            print(f"Balance:Rs{self.balance}")
            
acc_no=input("Enter accout number:")
name=input("Enter account holder name:")
acc_type=input("Enter type of account(savings/current):")
balance=float(input("Enter initial balance:"))
account=BankAccount(acc_no,name,acc_type,balance)
account.display()
deposit_amount=float(input("\n Enter amount to deposit:"))
account.deposit(deposit_amount)
account.display()
withdraw_amount=float(input("\n Enter amount to withdraw:"))
account.withdraw(withdraw_amount)
account.display()


        
        
        
