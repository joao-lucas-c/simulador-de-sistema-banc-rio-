from bank import Bank
from storage import load_accounts, save_accounts


def menu():
    print("\n=== BANCO PYTHON ===")
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Transferir")
    print("5 - Histórico")
    print("6 - Sair")


def main():
    bank = Bank()
    bank.accounts = load_accounts()

    while True:
        menu()
        option = input("Escolha uma opção: ")

        try:
            if option == "1":
                name = input("Nome: ")
                cpf = input("CPF (11 dígitos): ")
                bank.create_account(name, cpf)
                print("Conta criada com sucesso!")

            elif option == "2":
                cpf = input("CPF: ")
                amount = float(input("Valor: "))
                account = bank.get_account(cpf)
                account.deposit(amount)
                print("Depósito realizado!")

            elif option == "3":
                cpf = input("CPF: ")
                amount = float(input("Valor: "))
                account = bank.get_account(cpf)
                account.withdraw(amount)
                print("Saque realizado!")

            elif option == "4":
                cpf_from = input("Seu CPF: ")
                cpf_to = input("CPF destino: ")
                amount = float(input("Valor: "))
                acc_from = bank.get_account(cpf_from)
                acc_to = bank.get_account(cpf_to)
                acc_from.transfer(acc_to, amount)
                print("Transferência realizada!")

            elif option == "5":
                cpf = input("CPF: ")
                account = bank.get_account(cpf)
                print(f"\nSaldo: {account.balance}")
                for t in account.transactions:
                    print(t)

            elif option == "6":
                save_accounts(bank.accounts)
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()