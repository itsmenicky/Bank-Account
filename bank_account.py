# Greetings program! code by itsmenicky ;)
import random
import os
import time

class BankAccount:
    def __init__(self, account_holder, balance, password):
        self.__account_holder = account_holder
        self.__balance = balance
        self.__password = password
        self.__cpmf = 0

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        discount = 0.25 * value
        self.__cpmf += discount
        self.__balance -= value + discount

    def transfer(self, value, accountDestino):
        self.__balance -= value
        accountDestino.__balance += value

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_password(self):
        return self.__password
    
    def get_cpmf(self):
        return self.__cpmf

    def show_info(self):
        return f"conta de {self.__account_holder} - saldo de R$ {self.__balance:.2f}"


# -------------------------------- FUNÇÕES -----------------------------------------
def info(accounts):
    os.system('cls')
    print("\ncontas de todos os clientes:")
    for i, account in enumerate(accounts):
        print(f"[{i}] {account.show_info()}")
    time.sleep(2)

def password_authenticator(account_index, verify):
    truePass = accounts[account_index].get_password()
    if verify == truePass:
        return True
    else:
        return False

def withdraw_interaction(accounts):
    valid_client = False
    while not valid_client:
        info(accounts)
        account_index = int(input(f"\n\nO valor será retirado da conta de qual cliente? (0 a {len(accounts) - 1}): "))
        if 0 <= account_index < len(accounts):
            valid_client = True
        else:
            print("Índice de cliente inválido!")
            time.sleep(2)

    verify = input(f"{accounts[account_index].get_account_holder()}, insira sua senha: ")
    if not password_authenticator(account_index, verify):
        passTest = False
        while not passTest:
            passwordError = input("Senha inválida! Insira novamente: ")
            passTest = password_authenticator(account_index, passwordError)

    withdrawel = float(input("Qual o valor do Saque? "))
    accounts[account_index].withdraw(withdrawel)
    print("Saque realizado.")
    time.sleep(2)


def deposit_interaction(accounts):
    valid_client = False
    while not valid_client:
        info(accounts)
        account_index = int(input(f"\n\nO deposito será efetuado na conta de qual cliente? (0 a {len(accounts) - 1}): "))
        if 0 <= account_index < len(accounts):
            valid_client = True
        else:
            print("Índice de cliente inválido")

        verify = input(f"{accounts[account_index].get_account_holder()}, insira sua senha: ")
        if not password_authenticator(account_index, verify):
            passTest = False
            while not passTest:
                passwordError = input("Senha inválida! Insira novamente: ")
                passTest = password_authenticator(account_index, passwordError)

    deposit = float(input("Qual o valor do deposito? "))
    accounts[account_index].deposit(deposit)
    print("Deposito finalizado.")
    time.sleep(2)

def transfer_interaction(accounts):
    valid_origin_client = False
    while not valid_origin_client:
        info(accounts)
        origin_index = int(input(f"\n\nA transferência será efetuada da conta de qual cliente? (0 a {len(accounts) - 1}): "))
        if 0 <= origin_index < len(accounts):
            valid_origin_client = True
        else:
            print("Índice de cliente inválido")

        verify = input(f"{accounts[origin_index].get_account_holder()}, insira sua senha: ")
        if not password_authenticator(origin_index, verify):
            passTest = False
            while not passTest:
                passwordError = input("Senha inválida! Insira novamente: ")
                passTest = password_authenticator(origin_index, passwordError)

    valid_destiny_client = False
    while not valid_destiny_client:
        info(accounts)
        destiny_index = int(input(f"A transferência será efetuada para a conta de qual cliente? (0 a {len(accounts) - 1}): "))
        if 0 <= destiny_index < len(accounts):
            valid_destiny_client = True
        else:
            print("Índice de cliente inválido")

    value = float(input("Qual o valor da transferência? "))
    accounts[origin_index].transfer(value, accounts[destiny_index])
    print("Transferência finalizada.")
    time.sleep(2)
        
# --------------------------- PROGRAMA PRINCIPAL -----------------------------------
accounts = [
    BankAccount("Marcos", 1000.00, "B69c5"),
    BankAccount("Júlia", 250.00, "G6(1t8"),
    BankAccount("João", 2500.00, "]772Bx"),
    BankAccount("Roberto", 3000.00, "8$T99g"),
    BankAccount("Janaína", 4500.00, "1cM628")]

while True:
    os.system('cls')
    print("Escolha uma operação:")
    print("(1) mostrar informações de todas as contas")
    print("(2) sacar")
    print("(3) depositar")
    print("(4) transferir")
    print("(5) sair")
    escolha = int(input("Opção escolhida: "))

    if escolha == 1:
        info(accounts)
    elif escolha == 2:
        withdraw_interaction(accounts)
    elif escolha == 3:
        deposit_interaction(accounts)
    elif escolha == 4:
        transfer_interaction(accounts)
    elif escolha == 5:
        print("Fim do programa!")
        break
    else:
        print("Opção inválida!")

    print()