import json
import os
from models import Account


DATA_FILE = "data.json"


def load_accounts():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    accounts = {}
    for cpf, acc_data in data.items():
        account = Account(
            acc_data["name"],
            cpf,
            acc_data["balance"]
        )
        account.transactions = acc_data["transactions"]
        accounts[cpf] = account

    return accounts


def save_accounts(accounts):
    data = {cpf: acc.to_dict() for cpf, acc in accounts.items()}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)