class Customer:
    def __init__(self, customer_id, customer_name, account_list):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_list = account_list

class Account:
    def __init__(self, account_id, transaction_list, balance):
        self.account_id = account_id
        self.transaction_list = transaction_list
        self.balance = balance


class Transaction:
    def __init__(self, transaction_id, date, amount, type, available_balance, description):
        self.transaction_id = transaction_id
        self.date = date
        self.amount = amount
        self.type = type
        self.available_balance = available_balance
        self.description = description
        