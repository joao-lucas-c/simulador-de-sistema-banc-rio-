from models import Account


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, cpf):
        if cpf in self.accounts:
            raise ValueError("Conta já existe.")
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido.")
        self.accounts[cpf] = Account(name, cpf)

    def get_account(self, cpf):
        if cpf not in self.accounts:
            raise ValueError("Conta não encontrada.")
        return self.accounts[cpf]