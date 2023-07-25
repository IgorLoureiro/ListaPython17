class Equipamento:

    def __init__(self, data, preco):
        self.__data = data
        self.__preco = preco

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, x):
        self.__preco = x

    def exibe_equipamento(self):
        print(self.__data)
        print(self.__preco)


class Computador(Equipamento):

    def __init__(self, data, preco, processador, placa):
        super().__init__(data, preco)
        self.__processador = processador
        self.__placa = placa

    @property
    def processador(self):
        return self.__processador

    @processador.setter
    def processador(self, x):
        self.__processador = x

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, x):
        self.__placa = x

    def exibe_computador(self):
        self.exibe_equipamento()
        print(self.__processador)
        print(self.__placa)