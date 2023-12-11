#Usar help() para saber como funciona um método.
#Usar dir() para saber quais métodos podem ser usados com uma veriável específica.

from collections import Counter, defaultdict
from functools import reduce
import math
import statistics

def tipos_de_print():
    print("Qual seu nome?")
    nome = input()
    # print("Seu nome é:", nome,"!")
    # print("Seu nome é {0}!".format(nome))
    print(f"Seu nome é {nome}!")

    idade = input("Qual a sua idade?\n")
    # print("O %s tem %s anos." % (nome,idade))
    # print("O {0} tem {1} anos.".format(nome,idade))
    print(f"O {nome} tem {idade} anos.")
    print(f"O {nome} nasceu em {2023 - int(idade)}")


def tipos_de_dados():
    valor1, valor2 = 3, 5.2
    print(valor1)
    print(valor2)
    print(type(valor1))
    print(type(valor2))

def tipo_booleano():
    ativo = False
    logado = False
    print("not ativo: ", not ativo)
    print("is bool: ", type(ativo) is bool)
    print("ativo or logado: ", ativo or logado)
    print("not ativo and not logado: ", not ativo and not logado)

def tipo_string():
    nome = "jonas AMANCIO"
    numero = "123456"
    space = " "
    print(numero.isnumeric())
    print(nome.isspace())
    print(space.isspace())
    print(nome.lower())
    print(nome.upper())
    print(nome.title()) #Coloca a primeira letra de cada palavra em maiúsculo e o restante em minúsculo
    print(nome.title().istitle())
    print(nome[0:5])
    print(nome.split()[1]) #lista
    print(nome[2])
    print(nome[::-1]) #inverter string
    print(nome.replace('a','4')) #é case sensitive
    print(nome, end='') #para não pular linha no final do print
    print(nome.title() + " Silva santos")
    print(nome * 3) #é possível múltiplicar strings de forma concatenada
    print("\U0001F60D") #é possível imprimir emojis no console

def loop():
    nome = "Jonas Amancio"
    lista = [1, 2, 3, 4, 5]
    numeros = range(1,10) #o valor final não é incluso

    for index, letra in enumerate(nome):
        print(f"{index}:{letra}")
    
    for tupla in enumerate(nome):
        print(f"{tupla}")
        print(f"{tupla[0]}:{tupla[1]}")

    for value in range(2,15,2): #mudando o index de 2 em 2
        print(value)

    for value in range(10,0,-1): #loop invertido
        print(value)
        if value == 6:
            break

def listas():
    lista1 = [1,"a",(3,4), True,["subarray",2,(1,2), False]]
    lista2 = list("jonas")
    lista3 = list(range(11))

    print("for na lista:")
    for index,item in enumerate(lista1):
        print(f"{index} : {item} : {type(item)}")
    print("\ncount:")
    #count verifica quantas vezes determinado elemento aparece na lista, mas não checa sublistas.
    #ele não diferencia 1 de true
    print(lista1.count(1))

    print("\nappend, extend e insert:")
    lista1.append([6.7, 7.8, 9.1]) #só adiciona um item por vez, ou seja, o array vai inteiro
    lista1.extend([9, 8, 7]) #adiciona todos os itens do array um a um
    lista1.insert(2,"index") #insere um valor em uma posição específica sem substituir o valor que já havia lá, "empurrando" para a direita.
    print(lista1)

    print("\n7.8 in lista1:")
    print(7.8 in lista1) #não encontra item em sublista

    print("\nn in lista2:")
    print(lista2)
    print("n" in lista2)

    print("\invertendo a lista3:")
    print(lista3)
    lista3.sort(reverse=True) #ordena na lista atual. Para gerar uma nova lista ordenada use sorted(lista3) ou sorted(lista3, reverse=True) para ordernar inversamente
    print(lista3)
    lista3.reverse()
    print(lista3)
    print(lista3[::-1])

    print("\ncopiando uma lista:")
    lista4 = lista1.copy()
    lista5 = lista1 #nessa situação ele usa ponteiro, alterar a lista1 também alterará a lista5 e vice versa
    print(lista4)
    print(lista5)

    print("\nfunções de lista:")
    lista5.pop() #remove o último elemento e RETORNA o último elemento.
    lista1.pop(2) #é possível remover o elemento de um index específico.
    lista1.remove([6.7, 7.8, 9.1]) #procura e remove um elemento específico.
    print(lista5)
    print(lista1)
    print(lista4)
    lista4.clear()
    print(lista4)

    lista6 = ['jonas','amancio','silva','santos']
    nome_inteiro = ' '.join(lista6)
    print(nome_inteiro)

    print(lista1.index((3,4))) #mostra em qual posição está o primeiro item encontrado
    print(lista1.index(True,3,6)) #é possível definir uma posição a partir da qual ele vai começar a busca
    

    print("\ndados da lista1")
    print(len(lista3))
    print(len(lista3[3:]))
    print(max(lista3))
    print(min(lista3))
    print(sum(lista3))
    print(tuple(lista3))

    #desempacotamento de lista
    lista7 = [1,2,3]
    num1, num2, num3 = lista7 #a quantidade de variáveis deve ser exatamente igual a quantidade de itens na lsita
    print(num1,num2,num3)


def tuplas(): # não possui a função copy() pois existe shallow copy. tupla1 = tupla2 não usa ponteiro
    tupla1 = (1,2,3)
    tupla2 = 1,2,3
    tupla3 = tuple(range(1,6))
    print(tupla3)
    print(type(tupla1))
    

def dicionario():
    dic1 = {'br':'Brasil','eua':'estados unidos da america'.title()}
    dic2 = dict(ru='russia'.title(),py='Paraguay')
    print(type(dic1))
    print(type(dic2))
    print(dic1['eua'])
    print(dic2.get('ru'))
    print(dic1.get('py', 'não encontrado'.title()))
    dic1['cd'] = 'canada'.title() #adiciona novo dado, ou atualiza caso a chave já existe
    dic1.update({'cu':'Cuba'}) #adiciona novo dado, ou atualiza caso a chave já existe
    print(dic1.pop('br')) #remove o item da chave passada e retorna o value da chave removida
    del dic1['eua'] #não gera erro caso a chave não exista
    print(dic1)

    dic3 = {}.fromkeys(['nome','email','usuario','senha'],'desconhecido')
    print(dic3)
    print(dic3.keys())
    print(dic3.values())
    
def conjuntos():
    set1 = set({1,2,3,4,5,1,2,3,4})
    set2 = set({5,6,7,8,9})
    set1.add(77)
    set1.remove(4) #remove todas as ocorrências do valor passado. Gera erro caso o valor não exista.
    set1.discard(2) #não gera erro caso o valor não exista.
    print(set1)
    print(set1.union(set2))
    print(set1 | set2)
    print(set1.intersection(set2))
    print(set1 & set2)
    print(set1.difference(set2))
    print(set2.difference(set1))

def modulo_collections():
    lista1 = [1,1,1,1,1,2,2,2,2,2,2,3,3]
    contador = Counter(lista1)
    print(contador) #calcula a quantidade de ocorrências de cada item da lista. Funciona com string, tupla, dicionario, lista, sets...
    print(contador.most_common(2)) #mostra os 2 itens que mais apareceram e quantas vezes apareceram

    dicionario1 = defaultdict(lambda: 'desconhecido') #cria um dicionario que atribui um valor padrão à chaves inexistentes.
    dicionario1['chave1'] = 'dado da chave 1'
    print(dicionario1['chave1'])
    print(dicionario1['chave2'])
    

def docstring_func(arg1,arg2):
    """
    Função que mostra como documentar uma função.
    :param arg1: Argumento 1 de exemplo
    :param arg2: Argumento 2 de exemplo
    :return: Retorna a documentação da função.
    """
    return help(docstring_func)

def o_que_e_args(*args):
    """
    Explicação o parâmetro *args.
    Pode ter qualquer nome, contanto que tenha o asterísco.
    É uma tupla que contém os valores de todos os parâmetros extras que foram passados para a função.
    Caso eu envie uma collection e deseje desempacota-los, devo envia-los com asterísco.
    A ordem obrigatória é: (parametros_obrigatorios, *args, parametros_opcionais, **kwargs).
    """
    return help(o_que_e_args)

def o_que_e_kwargs(**kwargs):
    """
    Explicação o parâmetro **kwargs.
    Pode ter qualquer nome, contanto que tenha o asterísco.
    Contém todos os parâmetros extras nomeados, em formato de dicionário.
    Os dados são acessados com kwargs.items().
    Caso eu envie um dicionário e deseje desempacota-los, devo envia-los com dois asteríscos.
    A ordem obrigatória é: (parametros_obrigatorios, *args, parametros_opcionais, **kwargs).
    """
    return help(o_que_e_args)

def list_comprehension():

    def ao_quadrado(valor):
        return valor*valor

    numeros = [1,2,3,4,5]
    lc = [ao_quadrado(numero) for numero in numeros]
    pares = [numero for numero in numeros if not numero % 2]
    impares = [numero for numero in numeros if numero % 2]
    res = [numero * 2 if numero % 2 else numero / 2 for numero in numeros]
    print(lc)
    print(pares)
    print(impares)
    print(res)

def lambda_function(x):
    """
    Expressões lambda são funções sem nome.
    """
    calc = lambda x: 3 * x + 1
    calc2 = lambda nome,sobrenome: nome.title() + ' ' + sobrenome.title()
    print(calc(x))
    print(calc2('jonas','amancio'))

    def funcao_quadratica(a,b,c):
        return lambda x: a * x ** 2 + b * x + c
    teste = funcao_quadratica(2,3,-5)
    print(teste(0))
    print(teste(1))
    print(teste(2))

def maps():
    """
    Map é uma função que recebe 2 parâmetros, uma função e um iterável.
    Retorna um Map Object que pode ser acessado transformando em uma coleção.
    Ao utilizar os dados do Map Object, ele é zerado.
    """
    def area(r):
        return math.pi * (r ** 2)
    raios = [2,5,7.1,0.3,10,44]
    areas = map(area,raios)
    print(list(areas))
    print(list(areas)) #vai imprimir vazio pois já foi utilizado
    print(list(map(lambda r: math.pi * (r ** 2),raios)))
    pass

def filters():
    """
    Filters é uma função que recebe 2 parâmetros, uma função que retorna um booleano e um iterável.
    Retorna um Filter Object que pode ser acessado transformando em uma coleção.
    Ao utilizar os dados do Filter Object, ele é zerado.
    """
    dados = [1.2,2.7,0.8,4.1,4.3,-0.1]
    media = statistics.mean(dados)
    print(media)
    res = filter(lambda x: x > media, dados)
    print(list(res))
    nomes = ['vanessa','ana','maria']
    lista = list(map(lambda nome: f'Sua instrutora é {nome.title()}', filter(lambda nome: len(nome) >= 5, nomes)))
    print(lista)

def reduce_from_functools():
    """
    Passo 1: res1 = f(a1, a2)
    Passo 2: res2 = f(res1, a3)
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)
    """
    dados = [2,3,4,5,7,11,13,17,19,23,29]
    multi = lambda x, y: x * y
    res = reduce(multi,dados)
    print(res)

def any_and_all():
    print(all([0,1,2,3])) #verifica se todos os elementos de um iteravel são True
    print(any([0,1,2,3])) #verifica se algum dos elementos de um iteravel são True

def debug_pdb():
    """
    Importar pdb e utilizar pdb.set_trace() para colocar um breakpointem python inferior a 3.7.
    Em python 3.7 ou superior é possível utilizar a função breakpoint() sem a necessidade de import.
    Os comandos são:
    l: mostrar onde estamos no código
    n: passar para próxima linha de código
    p: imprimir variável
    c: continuar execução e finalizar pdb
    """

    nome = 'jonas'
    sobrenome = 'amancio'
    # import pdb; pdb.set_trace()
    breakpoint()
    nome_completo = nome.title() + ' ' + sobrenome.title()
    print(nome_completo)

def function_generator(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# gen = function_generator(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

""" Decorator """

def seja_educado(funcao):
    def sendo():
        print("foi um prazer conhecer você!")
        funcao()
        print("Tenha um ótimo dia!")
    return sendo

def saudacao():
    print("Seja bem-vindo ao ITEC!")

def demissao():
    print("Não volte mais aqui.")

contratacao_educada = seja_educado(saudacao)
demissao_educada = seja_educado(demissao)
# contratacao_educada()
# demissao_educada()

""" Decorator With Syntax Sugar """

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("É um prazer conhecer você!")
        funcao()
        print("Espero que possamos nos dar bem!")
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print("Meu nome é Jonas!")

# apresentando()


""" Decorators With Different Signatures - Decorator Pattern """

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, meu nome é {nome}'

@gritar
def reclamar(nome, atitude):
    return f'{nome} você tem sido muito {atitude}!'

# print(saudacao('Jonas'))
# print(reclamar('Jonas','Arrogante'))


""" Decorators With Arguments """

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args,**kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor} no lugar de {args[0]}'
            return funcao(*args,**kwargs)
        return outra
    return interna

@verifica_primeiro_argumento(10)
def soma_dez(num1,num2):
    return num1 + num2

def multiplica_dez(num1,num2):
    return num1 * num2

def divide_dez(num1,num2):
    return num1 / num2

# print(soma_dez(10,5))
# print(soma_dez(5,10))

# verifica = verifica_primeiro_argumento(10)

# multiplica = verifica(multiplica_dez)
# divide = verifica(divide_dez)

# print(multiplica(10,5))
# print(multiplica(7,10))

# print(divide(10,2))
# print(divide(2,10))

""" Decorators With Wraps """

from functools import wraps

""" Wraps irá preservar os metadados da função. sem ele, o __name__ e __docs__
retornarão as informações do decorator e não da função chamada"""
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Função logar"""
        print(f'você chamou: {funcao.__name__}')
        print(f'documentação: {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b

# print(soma(10,30))
# print(soma.__name__)
# print(soma.__doc__)


""" ZIP function """
a = (1,2,3)
b = (4,5,6)
# print(dict(zip(a,b)))
# print(tuple(zip(a,b)))




import datetime
def data_hora():
    print(datetime.datetime.now())
    print(datetime.datetime.now().replace(hour=16, minute=0, second=0, microsecond=0))
    print(datetime.datetime(2019, 1, 3, 14))
    nascimento = '02/08/1996'
    split = nascimento.split('/')
    data = datetime.datetime(int(split[2]), int(split[1]), int(split[0]))
    print(data, type(data))
    print(data.year)
    print(data.month)
    print(data.day)
    print(data.hour)
    print(data.minute)
    print(data.microsecond)

    #delta = diferença entre datas
    inicio = datetime.datetime.now()
    fim = datetime.datetime(2024, 8, 2)
    tempo = inicio - fim
    tempo_invertido = fim - inicio
    print(tempo)
    print(tempo_invertido)

    #adicionando dias
    compra = datetime.datetime.now()
    boleto = datetime.datetime.now() + datetime.timedelta(days=3)
    teste = datetime.datetime.now() - datetime.timedelta(days=5)
    print(compra)
    print(boleto)
    print(teste)
    print()

    compra_hora = datetime.datetime.now()
    boleto_hora = datetime.datetime.now() + datetime.timedelta(hours=3)
    teste_hora = datetime.datetime.now() - datetime.timedelta(hours=5)
    print(compra_hora)
    print(boleto_hora)
    print(teste_hora)
    print()

    teste = datetime.time()
    print(teste)
    print(type(teste))
    print(repr(teste))
    combinacao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=2)), datetime.time())
    print(combinacao)
    print(datetime.time(hour=17, minute=30))
    print()

    #segunda-feira = 0 e assim por diante até o 6 = domingo
    print(datetime.datetime.now().weekday())
    print()

    #formatando com strtime()
    teste = datetime.datetime.today().strftime('%d/%m/%Y')
    teste2 = datetime.datetime.time(datetime.datetime.now()).strftime('%H:%M:%S')
    print(teste)
    print(teste2)
    
    #formatando inversamente
    teste3 = datetime.datetime.strptime('02/08/1996', '%d/%m/%Y')
    print(teste3)
    print()
    

data_hora()