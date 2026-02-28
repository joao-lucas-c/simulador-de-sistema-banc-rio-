from datetime import datetime


class Transaction:
    def __init__(self, type_, amount, description=""):
        self.type = type_
        self.amount = amount
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "description": self.description,
            "date": self.date
        }


class Account:
    def __init__(self, name, cpf, balance=0.0):
        self.name = name
        self.cpf = cpf
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Valor de depósito inválido.")
        self.balance += amount
        self.transactions.append(Transaction("Depósito", amount).to_dict())

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Valor de saque inválido.")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente.")
        self.balance -= amount
        self.transactions.append(Transaction("Saque", amount).to_dict())

    def transfer(self, target_account, amount):
        if amount <= 0:
            raise ValueError("Valor de transferência inválido.")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente.")
        self.balance -= amount
        target_account.balance += amount

        self.transactions.append(
            Transaction("Transferência Enviada", amount, f"Para {target_account.cpf}").to_dict()
        )
        target_account.transactions.append(
            Transaction("Transferência Recebida", amount, f"De {self.cpf}").to_dict()
        )

    def to_dict(self):
        return {
            "name": self.name,
            "cpf": self.cpf,
            "balance": self.balance,
            "transactions": self.transactions
        }