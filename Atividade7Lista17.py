"""
Escreva um código que apresente a classe Moto, com atributos marca,
modelo, cor e marcha e, o método imprimir. O método imprimir deve mostrar na
tela os valores de todos os atributos. O atributo marcha indica em que a marcha

a Moto se encontra no momento, sendo representado de forma inteira, onde O -
neutro, 1 — primeira, 2 — segunda, etc.

adicione um método construtor que permita a
definição de todos os atributos no momento da instanciação do objeto.

adicione os métodos marchaAcima e marchaAbaixo que deverão efetuar a troca de marchas, onde o método
marchaAcima deverá subir uma marcha, ou seja, se a moto estiver em primeira
marcha, deverá ser trocada para segunda marcha e assim por diante. O método
marchaAbaixo deverá realizar o oposto, ou seja, descer a marcha.

adicione os atributos menorMarcha e maiorMarcha, onde o atributo menorMarcha indica qual será a menor marcha possível
para a moto e o atributo maiorMarcha indica qual será a maior marcha possível. Desta
forma os métodos marchaAcima e marchaAbaixo devem ser reescritos de forma
a não permitirem a troca de marchas para valores abaixo da menorMarcha e
acima da maiorMarcha. O método imprimir deve ser modificado de forma a
mostrar na tela os valores de todos os atributos.

adicione o atributo ligada que terá a função de indicar se a moto está ligada ou não. Este atributo deverá
ser do tipo boleano. O método imprimir deve ser modificado de forma a mostrar na tela os valores de
todos os atributos.
"""


class Moto:

    def __init__(self, marca, modelo, cor, menormarcha=0, maiormarcha=6, motor=False):

        self.__marcha = 0
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__menormarcha = menormarcha
        self.__maiormarcha = maiormarcha
        self.__motor = motor

    @classmethod
    def imprimir(cls, x):

        print(x.__marca)
        print(x.__modelo)
        print(x.__cor)
        print(x.__marcha)
        print(x.__menormarcha)
        print(x.__maiormarcha)
        print(x.__motor)

    @classmethod
    def marchaAcima(cls, x):
        if x.__marcha + 1 <= x.__maiormarcha:
            x.__marcha += 1

    @classmethod
    def marchaAbaixo(cls, x):
        if x.__marcha - 1 >= x.__menormarcha:
            x.__marcha -= 1

    @classmethod
    def estadomotor(cls, x):
        if x.__motor:
            print("O motor está desligado")
        else:
            print("O motor está ligado")

    @classmethod
    def alterarmotor(cls, x):
        if x.__motor:
            x.__motor = False
        else:
            x.__motor = True


p1 = Moto('Honda', 'XZ18', 'Vermelho')

Moto.marchaAbaixo(p1)

Moto.imprimir(p1)
