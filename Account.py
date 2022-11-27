class Account:
    def __init__(self,amount):
        self.__balance = amount

    def setBalance(self,amount = 0):
        if amount > 0:
            self.__balance = amount 

    def getBalance (self):
        return self.__balance

    def deposit(self,amount):
        if amount >0:
            self.__balance +=amount
            return True
        else:
            return False

    def withdraw (self,amount):
        if amount > self.__balance:
            return False
        else:
            self.__balance -=amount
            return True