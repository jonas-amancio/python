class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]) -> None:
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def bateria(self) -> int:
        return self.__bateria
    
    @property
    def habilidades(self) -> list:
        return self.__habilidades
    
    def carregar(self) -> None:
        self.__bateria = 100

    def dizer_nome(self) -> str:
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'Meu nome é {self.__nome.title()}'
        return 'Sem bateria, por favor recarregue.'
    
    def aprender_habilidade(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f'Eu aprendi a habilidade: {nova_habilidade.title()}'
        return 'Bateria insuficiente, por favor recarregue.'