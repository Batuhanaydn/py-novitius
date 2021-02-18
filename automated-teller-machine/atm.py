import random
import time

class Account:
    def __init__(self, id, checkingBalance = 0, savingsBalance = 0, annualInterestRateSavings = 3.4):
        self.id = id
        self.checkingBalance = checkingBalance
        self.savingsBalance = savingsBalance
        self.annualInterestRateSavings = annualInterestRateSavings
 
    def getId(self):
        return self.id
 
    def checkingAccountBalance(self):
        return self.checkingBalance
 
    def withdrawCheckingAccount(self, amount):
        self.checkingBalance -= amount
 
    def depositCheckingAccount(self, amount):
        self.checkingBalance += amount
 
    def transferCheckingAccount(self, amount):
        self.checkingBalance += amount
        self.savingsBalance -= amount
        
    def savingsAccountBalance(self):
        return self.savingsBalance
 
    def withdrawSavingsAccount(self, amount):
        self.savingsBalance -= amount
 
    def depositSavingsAccount(self, amount):
        self.savingsBalance += amount
 
    def transferSavingsAccount(self, amount):
        self.savingsBalance += amount
        self.checkingBalance -= amount
 
    def savingsAccountMonthlyInterest(self):
        return self.savingsBalance * self.savingsAccountMonthlyInterest()
    
    def savingsAccountAnnualInterestRate(self):
        return self.annualInterestRateSavings
 
    def savingsAccountMonthlyInterestRate(self):
        return self.annualInterestRateSavings / 12



def main():
    
    # Creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)
        print(account)
    while True:
        
        # Reading id from user
        print("Welcome to International Bank.")
        id = int(input("\nEnter 4-digit account pin: "))
 
        # Loop till id is valid
        while id < 1000 or id > 9999:
           id = int(input("\nInvalid Id.. Re-enter: "))
 
        # Iterating over interface
        while True:
            
            # Printing menu
            print("\nHow can we help you today?")
            print("""\n1 - View Checking Balance \t\t2 - Withdraw Checking \n3 - Deposit Checking \t\t\t4 - Transfer Checking
                    \n5 - View Savings Balance \t\t6 - Withdraw Savings \n7 - Deposit Savings \t\t\t8 - Transfer Savings
                    \n9 - Exit """)
 
            # Reading selection
            selection = int(input("\nEnter your numerical selection: "))
            
            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    account = acc
                    break
 
            # View Checking Balance
            if selection == 1:
                
                # Printing balance
                print(f"\nChecking account balance: ${format(account.checkingAccountBalance(), '.2f')} ")
                
                time.sleep(2)
                    
 
            # Checking Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw from checking: "))
                ver_checking_withdraw = input(f"Is ${format(amt, '.2f')} the correct amount to withdraw, Yes or No ? ")
                ver_checking_withdraw = ver_checking_withdraw.upper()
                
                if ver_checking_withdraw == "YES":
                    print("\nVerified checking account withdraw.")
                    time.sleep(2)
                else:
                    break
 
                if amt < account.checkingAccountBalance():
                    # Calling withdraw method
                    account.withdrawCheckingAccount(amt)
                    # Printing updated balance
                    print(f"Updated checking account balance: ${format(account.checkingAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(f"\nYour checking account balance is less than withdrawl amount: ${format(account.checkingAccountBalance(), '.2f')} ")
                    time.sleep(2)
 
            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit in checking: "))
                ver_checking_deposit = input(f"Is ${format(amt, '.2f')} the correct amount to deposit, Yes or No ? ")
                ver_checking_deposit = ver_checking_deposit.upper()
                
                if ver_checking_deposit == "YES":
                    # Calling deposit method
                    print("\nVerified checking account deposit.")
                    time.sleep(2)
                    account.depositCheckingAccount(amt)
                    # Printing updated balance
                    print(f"\nUpdated checking account balance: ${format(account.checkingAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    break
 
            #Transfer Savings Account to Checking Account
            elif selection == 4:
                amt = float(input("\nEnter amount to transfer from savings account to checking: "))
                ver_checking_transfer = input(f"Is ${format(amt, '.2f')} the correct amount to transfer, Yes or No ? ")
                ver_checking_transfer = ver_checking_transfer.upper()
                if ver_checking_transfer == "YES":
                    print("Verified savings account transfer to checking account.")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break
 
                if amt < account.savingsAccountBalance():
                    # Calling transfer method
                    account.transferCheckingAccount(amt)
                    # Printing updated balance
                    print(f"Updated checking account balance: ${format(account.checkingAccountBalance(), '.2f')} ")
                    print(f"Updated savings account balance: ${format(account.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(f"\nYour savings account balance is less than transfer amount: ${format(account.checkingAccountBalance(), '.2f')} ")
                    time.sleep(2)
                
            # View Checking Balance
            elif selection == 5:
                # Printing balance
                print(f"Savings account balance: ${format(account.savingsAccountBalance(), '.2f')} ")
                time.sleep(2)
 
            # Savings Withdraw
            elif selection == 6:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw from savings: "))
                ver_savings_withdraw = input(f"Is ${format(amt, '.2f')} the correct amount to withdraw, Yes or No ? ")
                ver_savings_withdraw = ver_savings_withdraw.upper()
                if ver_savings_withdraw == "YES":
                    print("\nVerified savings account withdraw.")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break
 
                if amt < account.savingsAccountBalance():
                    # Calling withdraw method
                    account.withdrawSavingsAccount(amt)
                    # Printing updated balance
                    print(f"Updated checking account balance: ${format(account.checkingAccountBalance(), '.2f')} ")
                    print(f"Updated savings account balance: ${format(account.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(f"\nYour savings account balance is less than withdrawl amount: ${format(account.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
 
            # Savings Account Deposit
            elif selection == 7:
                # Reading amount
                amt = float(input("\nEnter amount to deposit in savings: "))
                ver_savings_deposit = input(f"Is ${format(amt, '.2f')} the correct amount to withdraw, Yes or No ? ")
                ver_savings_deposit = ver_savings_deposit.upper()
                
                if ver_checking_deposit == "YES":
                    print("\nVerified savings account deposit.")
                    time.sleep(2)
                    # Calling deposit method
                    account.depositSavingsAccount(amt)
                    # Printing updated balance
                    print(f"Updated savings account balance: ${format(account.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    time.sleep(2)
                    break
 
            #Transfer Checking Account to Savings Account
            elif selection == 8:
                amt = float(input("\nEnter amount to transfer from checking account to savings account: "))
                ver_savings_transfer = input(f"Is ${format(amt, '.2f')} the correct amount to transfer, Yes or No ? ")
                ver_savings_transfer = ver_savings_transfer.upper()
                if ver_savings_transfer == "YES":
                    print("Verified checking account transfer to savings account.")
                    time.sleep(2)
                else:
                    break
 
                if amt < account.checkingAccountBalance():
                    # Calling withdraw method
                    account.transferSavingsAccount(amt)
                    # Printing updated balance
                    print(f"Updated checking account balance: ${format(account.checkingAccountBalance(), '.2f')} ")
                    print(f"Updated savings account balance: ${format(account.savingsAccountBalance(), '.2f')} ")
                    time.sleep(2)
                else:
                    print(f"\nYour checking account balance is less than transfer amount: ${format(account.checkingAccountBalance(), '.2f')} ")
                    time.sleep(2)
                     
            elif selection == 9:
                print("\nTransaction is now complete.")
                print("Transaction number: ", random.randint(10000, 1000000))
                print("Current Interest Rate: ", account.annualInterestRateSavings)
                print("Monthly Interest Rate: ", account.annualInterestRateSavings / 12)
                print("Thanks for choosing us as your bank")
                exit()
            elif selection == 10:
                print(account.gizli_isim)


            # Any other choice
            else:
                print("\nThat's an invalid choice.")
                break
 
# Main function
main()