from CheckingAccount import CheckingAccount

def account_creation():
    name = input("Enter account holder's name: ")
    print("")
    address = input("Enter account holder's address: ")
    account = CheckingAccount(name, address)
    return account

def account_initalization(account):
    print("")
    inital_deposit_request = input("Would you like to make an inital deposit (y/n): ")
    while True:
        if not(inital_deposit_request == 'y' or inital_deposit_request == 'n'):
            print("ERROR: Invald input")
            inital_deposit_request = input("Would you like to make an inital deposit (y/n): ")
        elif inital_deposit_request == 'y':
            account = account_deposit(account)
            return account
        else:
            return account

def account_deposit(account):
    try:
        print("")
        deposit_amount = input('How much would you like to deposit?: ')
        deposit = float(deposit_amount)
        account.deposit(deposit)
        print("")
        print("New balance: ${:,.2f}".format(account.get_balance()))
    except:
        print("ERROR: Invald input")
        account = account_deposit(account)
    return account

def account_withdrawal(account):
    try:
        print("")
        withdrawal_amount = input('How much would you like to withdraw?: ')
        withdrawal = float(withdrawal_amount)
        if (account.get_balance() < withdrawal):
            print('Account contains insufficient funds.')
        else:
            account.withdraw(withdrawal)
            print("")
            print("New balance: ${:,.2f}".format(account.get_balance()))
    except:
        print("ERROR: Invald input")
        account = account_withdrawal(account)
    return account
    
def account_options(account):
    print("")
    print("How can we assist you today?")
    menu_selection = input("Enter (1) to view your account information, enter (2) to make a deposit, enter (3) to make a withdrawl, or enter (4) to exit: ")
    while True:
        if not(menu_selection == '1' or menu_selection == '2' or menu_selection == '3' or menu_selection == '4'):
            print("ERROR: Invald input")
            menu_selection = input("Enter (1) to view your account information, enter (2) to make a deposit, enter (3) to make a withdrawl, or enter (4) to exit: ")
        elif menu_selection == '1':
            print("")
            print("Account Number: {0}".format(account.get_account_number()))
            print("Account Holder Name: {0}".format(account.get_name()))
            print("Account Holder Address: {0}".format(account.get_address()))
            print("Account Balance: ${:,.2f}".format(account.get_balance()))
            print("")
            menu_selection = input("Enter (1) to view your account information, enter (2) to make a deposit, enter (3) to make a withdrawl, or enter (4) to exit: ")
        elif menu_selection == '2':
            account = account_deposit(account)
            print("")
            menu_selection = input("Enter (1) to view your account information, enter (2) to make a deposit, enter (3) to make a withdrawl, or enter (4) to exit: ")
        elif menu_selection == '3':
            account_withdrawal(account)
            print("")
            menu_selection = input("Enter (1) to view your account information, enter (2) to make a deposit, enter (3) to make a withdrawl, or enter (4) to exit: ")
        else:
            exit()
            
    
def main():
    account = account_creation()
    account = account_initalization(account)
    account_options(account)
    
main()