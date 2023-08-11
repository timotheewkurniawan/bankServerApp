# returns a boolean value whether it is possible to withdraw the money or not
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


# returns boolean value whether the transaction could proceed or not
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