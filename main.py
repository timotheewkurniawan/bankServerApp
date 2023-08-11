from models import *
from bank import customerList
from businessLogic import *
customer_id_count = 0
account_id_count = 0

#creating dummy customers
for i in range(10):
    customerList.append(Customer(customer_id_count,"Dummy Customer "+str(i), [account_id_count]))
    customer_id_count += 1
    account_id_count += 1

login_id = int(input("Please enter your customer ID to login: "))
curr_customer = next(customer for customer in customerList if customer.customer_id == login_id )

selected_acc = int(input("Please input the account id for the account you want to access: "))
curr_acc = next(acc_id for acc_id in curr_customer.account_list if acc_id == selected_acc )


selection = int(input("What would you like to do? (1. Check Balance 2. Withdraw Money 3. Deposit Money 4. Transfer Funds)"))

if selection == 1:
    print("hello")
    # showBalance(curr_customer)
elif selection == 2:
    amount = int(input("How much money do you want to withdraw? "))
    # withdrawMoney(curr_customer,amount)
elif selection == 3:
    amount = int(input("How much money do you want to deposit? "))
    # depositMoney(curr_customer, amount)
else:
    to_account = int(input("Enter the account id that you want to transfer to. "))
    amount = int(input("How much money do you want to transfer?"))
    # transferFunds(curr_customer,)

    