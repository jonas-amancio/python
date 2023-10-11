class Lampada:

    def __init__(self, voltagem: str, cor: str) -> None:
        # o __ indica que a variável é private
        self.__voltagem = voltagem
        self.__cor = cor
        self.ligada = False

    @property
    def voltagem(self) -> str:
        return self.__voltagem
    
    # @property
    # def cor(self) -> str:
    #     return self.__cor

lampada = Lampada('2V','Azul')
print(lampada.ligada)
print(lampada._Lampada__cor) #funciona, mas não devemos usar
# print(lampada.__cor) #nao funciona