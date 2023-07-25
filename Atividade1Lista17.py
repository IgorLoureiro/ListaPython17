"""
1) Escreva um código que apresente a classe Pessoa, com atributos nome,
endereço e telefone e, o método imprimir. O método imprimir deve mostrar na
tela os valores de todos os atributos.
"""


class Pessoa:

    def __init__(self, nome, endereco, telefone):

        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @staticmethod
    def imprimir(x):
        print(x.__nome)
        print(x.__endereco)
        print(x.__telefone)


p1 = Pessoa('Jonas', 'Timbuquistão', 51995777653)

Pessoa.imprimir(p1)
