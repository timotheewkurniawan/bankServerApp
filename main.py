from models import *
from bank import *
from businessLogic import *

from datetime import date


#to ensure customer_id, account_id, and transaction_id is unique across the application
customer_id_count = 0
account_id_count = 0
transaction_id_count = 0

#creating dummy customers
for i in range(10):
    new_acc = Account(account_id_count,[],1000)
    customerList.append(Customer(customer_id_count,"Dummy Customer "+ str(customer_id_count), [new_acc]))
    accountList.append(new_acc)
    customer_id_count += 1
    account_id_count += 1



#app logic starts
login_id = int(input("Please enter your customer ID to login: "))
curr_customer = next(customer for customer in customerList if customer.customer_id == login_id )

selected_acc = int(input("Please input the account id for the account you want to access: "))
curr_acc = next(acc for acc in curr_customer.account_list if acc.account_id == selected_acc )

while True:
    print("\n")
    selection = int(input("---BANK APP---\n1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4. Transfer Funds\n5. Show Recent Transactions\n6. Logout\n7. Close App\nWhat would you like to do?\n"))

    if selection == 1:
        print("Your balance is", str(showBalance(curr_acc)),"HKD.")

    elif selection == 2:
        amount = int(input("How much money do you want to withdraw? "))
        withdrawMoney(curr_acc,amount)


    elif selection == 3:
        amount = int(input("How much money do you want to deposit? "))
        depositMoney(curr_acc, amount)

    elif selection == 4:
        to_account_id = int(input("Enter the account id that you want to transfer to. "))
        amount = int(input("How much money do you want to transfer?"))
        to_account = next(acc for acc in accountList if acc.account_id == to_account_id )
        status = transferFunds(curr_acc,to_account, amount)

        if status == True:
            description = input("Enter a description for your transaction. (Optional) ")
            new_transaction = Transaction(transaction_id_count, date.today(), amount, "CR", showBalance(curr_acc), description)
            (curr_acc.transaction_list).append(new_transaction)
            transactionList.append(new_transaction)
            print(curr_acc.transaction_list)
            print(transactionList)
            transaction_id_count += 1

    elif selection == 5:
        print("---RECENT TRANSACTIONS---")
        showRecentTransactions(curr_acc)

    elif selection == 6:
        print("Logged out successfully")
        login_id = int(input("Please enter your customer ID to login: "))
        curr_customer = next(customer for customer in customerList if customer.customer_id == login_id )

        selected_acc = int(input("Please input the account id for the account you want to access: "))
        curr_acc = next(acc for acc in curr_customer.account_list if acc.account_id == selected_acc )

    elif selection == 7:
        print("Exited app.")
        break

    