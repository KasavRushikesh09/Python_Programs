'''Pandas (Intermediate)
 A DataFrame contains account_id, transaction_date, amount, and transaction_type.'''
from datetime import date

from faker import Faker
import pandas as pd

def banking_transaction():
    fk = Faker()

    account_id_list = list(i for i in range(101,161))
    min_trans_date = date(2025,1,1)
    max_trans_date = date(2026,1,1)

    min_amount = 500
    max_amount = 20000

    transaction_type_list = ['Credit','Debit','UPI','ATM']

    account_id = []
    transaction_date = []
    amount = []
    transaction_type = []

    data ={
        'account_id' : account_id,
        'transaction_date' :transaction_date,
        'amount':amount,
        'transaction_type':transaction_type
    }

    for _ in range(332):
        account_id.append(fk.random_element(account_id_list))
        transaction_date.append(fk.date_between_dates(date_start = min_trans_date,date_end = max_trans_date))
        amount.append(fk.random_int(min = min_amount,max =max_amount))
        transaction_type.append(fk.random_element(transaction_type_list))
    return pd.DataFrame(data)

if __name__ == '__main__':
    print(banking_transaction())





