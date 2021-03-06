from aux import date_to_str
from aux import str_to_date
from datetime import date


class Client:

    contador: int = 100

    def __init__(self, nome: str, sobrenome: str, email: str, cpf: str, data_nascimento: str):
        self.__codigo: int = Client.contador
        self.__nome: str = nome
        self.__sobrenome: str = sobrenome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_to_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Client.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def sobrenome(self) -> str:
        return self.__sobrenome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento_p(self) -> str:
        return date_to_str(self.__data_nascimento)

    @property
    def data_cadastro_p(self) -> str:
        return date_to_str(self.__data_cadastro)

    def __str__(self):
        return f'\nCódigo: {self.codigo}\nNome: {self.nome}\nSobrenome: {self.sobrenome}' \
               f'\nData de nascimento: {self.data_nascimento_p}\nData de cadastro: {self.data_cadastro_p}'
