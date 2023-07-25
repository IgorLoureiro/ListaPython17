"""
Escreva um código que apresente a classe Quadrado, com atributos
lado, área e perímetro e, os métodos calcularArea, calcularPerimetro e imprimir.
Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos
cálculos e colocar os valores nos atributos area e perimetro. O método imprimir
deve mostrar na tela os valores de todos os atributos. Salienta-se que a área de
um quadrado é obtida pela fórmula (lado * lado) e o perímetro por (4 * lado).
"""

class Quadrado:

    def __init__(self, lado):

        self.__lado = lado


    @classmethod
    def calcular_area(cls, x):

        return x.__lado * x.__lado

    @classmethod
    def calcular_perimetro(cls, x):

        return x.__lado * 4

    @classmethod
    def imprimir(cls, x):

        print(f"Lado: {x.__lado}")
        print(f"Area: {Quadrado.calcular_area(x)}")
        print(f"Perimetro: {Quadrado.calcular_perimetro(x)}")

quadrado = Quadrado(4)

Quadrado.imprimir(quadrado)