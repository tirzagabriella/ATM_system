from Customer import Customer

class Bank:
    def __init__(self,bName):
        self.__bName = bName
        self.__customer = []
        self.__numofCustomer = 0

    def addCustomer(self,f,l):
        self.__customer.append(Customer(f,l))
        self.__numofCustomer += 1

    def getCustomer(self,index):
        return self.__customer[index]

    def getnumofCustomer(self):
        return self.__numofCustomer

    def getCustomers(self):
        return self.__customer

    def editCustomer(self, index, f, l):
        self.__customer[index].setfirstName(f)
        self.__customer[index].setlastName(l)
        return self.__customer[index]

    def deleteCustomer(self, index):
        if index > len(self.__customer):
            return "ERROR"
        else:
            self.__customer.pop(index)

    def searchCustomer(self,index,bName):
        return bName.getCustomer(index).getfirstName(), bName.getCustomer(index).getlastName()
    