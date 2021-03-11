from typing import List
from account import Account
from client import Client
from time import sleep


contas: List[Account] = []


def menu():
    try:
        print('-------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------- ATM ----------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('O QUE DESEJA FAZER: ')
        print()
        print('1 - CRIAR CONTA: ')
        print('2 - EFETUAR DEPÓSITO: ')
        print('3 - EFETUAR SAQUE: ')
        print('4 - EFETUAR TRANSFERÊNCIA: ')
        print('5 - LISTAR CONTAS: ')
        print('5 - SAIR: ')

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def criar_conta():
    pass


def efetuar_deposito():
    pass


def efetuar_saque():
    pass


def efetuar_transferencia():
    pass


def listar_contas():
    pass


def rastrear_conta(numero):
    pass


if __name__ == '__main__':
    menu()
