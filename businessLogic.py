from models import Account, Transaction

# returns a boolean value whether it is possible to withdraw the money or not
def withdrawMoney(account,amount):
    if account.balance < amount:
        return False
    else:
        account.balance -= amount
        return True


def showBalance(account):
    return account.balance


def depositMoney(account,amount):
    account.balance += amount


# returns boolean value whether the transaction could proceed or not
def transferFunds(from_account, to_account, amount):
    if from_account.balance < amount:
        return False
    else:
        from_account.balance -= amount
        to_account.balance += amount
        return True