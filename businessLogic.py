def withdrawMoney(account,amount):
    balance = showBalance(account)
    print(f'Your current balance is {balance}.')
    if account.balance < amount:
        print('Not enough balance!')
        return False
    else:
        account.balance -= amount
        print(f'Amount withdrawn, your current balance is {balance - amount}.')
        return True


def showBalance(account):
    return account.balance


def depositMoney(account,amount):
    account.balance += amount
    print("Deposit successfully, total amount in account is",str(account.balance))


def transferFunds(from_account, to_account, amount):
    from_balance = showBalance(from_account)
    print(f'Your current balance is {from_account.balance}.')
    if from_account.balance < amount:
        print('Not enough balance!')
        return False
    else:
        from_account.balance -= amount
        print(f'Funds transfered, your current balance is {from_balance - amount}')
        to_account.balance += amount
        return True
    
def showRecentTransactions(account):
    count = 0
    for i in range(len(account.transaction_list) - 1, -1, -1):
        if count == 10:
            break
        print(account.transaction_list[i].__dict__)
        count += 1
