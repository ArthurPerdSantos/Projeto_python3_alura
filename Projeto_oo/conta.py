

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...{}".format(self))
        # atribui as variáveis recebidas
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = valor < (self.__saldo + self.__limite)
        return valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque feito com sucesso")
        else:
            print("O valor {} ultrapassa o limite da conta".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    @property
    def saldo(self):
        return (self.__saldo)

    @property
    def titular(self):
        return (self.__titular)

    @property
    def limite(self):
        return (self.__limite)

    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigo_bancos():
        return {'BB' : '001', 'Caixa' : '104', 'Bradesco' : '237' }





