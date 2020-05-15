from random import randint

class CheckingAccount:
    def __init__(self, user_name, user_address):
        self.name = user_name
        self.address = user_address
        self.account_number = '{:09}'.format(randint(1, 10**9))
        self.__balance = 0.00
        
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, credit):
        self.__balance = self.__balance + credit
        
    def withdraw(self, debit):
        self.__balance = self.__balance - debit