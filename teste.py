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

    print("\nordenando inversamente a lista3:")
    print(lista3)
    lista3.sort(reverse=True)
    print(lista3)
    





listas()