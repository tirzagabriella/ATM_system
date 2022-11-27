from Account import Account
from Customer import Customer
from Bank import Bank

nameList = []
bca = Bank("BCA")

def main():
    x = 1
    while x == 1:
        print("Choose Role:")
        print("1. Customer")
        print("2. Administrator")
        y = eval(input("Answer 1 or 2 : "))
        if y == 1:
            print("You are a Customer")
            CustomerInput()
        elif y == 2:
            print("You are an Admin")
            AdminInput()
        else:
            print("Error plis retry")

def AdminInput():
    adm = 1
    while adm == 1:
        print ("Options:")
        print ("1. Add Customer")
        print ("2. Delete Customer")
        print ("3. Edit Customer")
        print ("4. Search Customer")
        admin = eval(input("Choose your option 1 or 2 or 3 or 4:"))
        if admin == 1:
            print ("Adding Customer Input:")
            fn = input("Please input your first name:")
            ln = input("Please input your last name:")
            bca.addCustomer(fn,ln)
            print ("Your name for your account is:",fn,ln)
            nameList.append(fn + " " + ln)
            adm = adm + 1
        elif admin == 2:
            print ("Choose customer to delete:")

            if len(nameList) == 0:
                print ("Customer still empty, please add customer first")
                return 

            y = 0
            for x in nameList:
                y = y + 1
                print (y,".",x)
            delete = eval(input("Enter a number:"))
            deleteindex = delete - 1 
            bca.deleteCustomer(deleteindex)
            print ("Succesusfully deleted", nameList[deleteindex])
            nameList.pop(deleteindex)
            adm = adm + 1
        elif admin == 3:
            print ("Choose customer to edit:")

            if len(nameList) == 0:
                print ("Customer still empty, please add customer first")
                return 

            y = 0
            for x in nameList:
                y = y + 1
                print (y,".",x)
            edit = eval(input("Enter a number:"))
            editindex = edit - 1
            newfn = input ("Enter new first name:")
            newln = input ("Enter new last name:")
            bca.editCustomer(editindex, newfn, newln)
            nameList[editindex] = newfn + " " + newln
            bca.editCustomer (editindex, newfn, newln)
            adm = adm + 1
        elif admin == 4:
            print ("Choose a number to search name:")

            if len(nameList) == 0:
                print ("Customer still empty, please add customer first")
                return 

            search = eval(input("Enter Number:"))
            searchindex = search - 1
            print(bca.searchCustomer(searchindex,bca))
        else:
            print ("Error Please Retry")


def CustomerInput ():
    if len(bca.getCustomers()) == 0:
        print ("Please register your customer first")
        return
        
    cus = 1
    while cus == 1:
        print ("Options:")
        print ("1. Balance")
        print ("2. Withdraw")
        print ("3. Deposit")
        cusin = eval(input("Choose your option 1 or 2 or 3:"))
        if cusin ==1:
            balance = eval(input ("Input card number:"))
            balanceindex = balance - 1
            resultBalance= bca.getCustomer(balanceindex).getAccount().getBalance()
            if resultBalance:
                print("Your balance in your bank account:",bca.getCustomer(balanceindex).getAccount().getBalance())
        elif cusin ==2:
            balance2 = eval(input("Input card number:"))
            balance2index = balance2 - 1
            withdraw = eval(input("Input withdraw amount:"))
            resultWithdraw = bca.getCustomer(balance2index).getAccount().withdraw(withdraw)
            if resultWithdraw:
                print("Withdraw Successful")
        elif cusin ==3:
            balance3= eval(input("Input card number:"))
            balance3index = balance3 - 1
            depo = eval(input("Input deposit amount:"))
            result = bca.getCustomer(balance3index).getAccount().deposit(depo)
            if result:
                print ("Deposit successful")

        else:
            print("Error Please Retry")


if __name__ == "__main__":
    main()