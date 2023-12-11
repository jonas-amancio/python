class Lampada:

    amperagem = '2w'

    def __init__(self, voltagem: str, cor: str) -> None:
        # o __ indica que a variável é private
        self.__voltagem = voltagem
        self.__cor = cor
        self.ligada = False

    @property
    def voltagem(self) -> str:
        return self.__voltagem
    
    @voltagem.setter
    def voltagem(self, new_voltagem) -> None:
        if new_voltagem:
            self.__voltagem = new_voltagem
    
    @voltagem.deleter
    def voltagem(self) -> None:
        self.__voltagem = '0V'
    
    @classmethod
    def get_amperagem(cls) -> str:
        return cls.amperagem
    
    @staticmethod
    def marca() -> str:
        return "Eletrolux"
    
    # @property
    # def cor(self) -> str:
    #     return self.__cor

# lampada = Lampada('2V','Azul')
# print(lampada.ligada)
# print(lampada._Lampada__cor) #funciona, mas não devemos usar
# print(lampada.voltagem)
# lampada.voltagem = '5V'
# print(lampada.voltagem)
# del lampada.voltagem
# print(lampada.voltagem)
# # print(lampada.__cor) #nao funciona
# print(Lampada.get_amperagem())
# print(Lampada.marca())

##############################################
class Pessoa:
    
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.cpf = cpf

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula) -> None:
        super().__init__(nome, cpf)
        self.matricula = matricula

##############################################

class Animal:
    pass

class Terrestre(Animal):
    pass

class Aquatico(Animal):
    pass

class Pinguim(Aquatico):
    pass

class Ornitorrinco(Aquatico, Terrestre):
    pass

print(Ornitorrinco.__mro__)
print(Pinguim.__mro__)

##############################################

