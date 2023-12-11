"""
Assertions (Checagens/Questionamentos) retorna None para verdadeiro e AssertionError para falso.

Se o programa for executado com o parâmetro -O nenhum assert será executado.
"""

def valida_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos.'
    return a + b

# print(valida_positivos(2,4))
# print(valida_positivos(-2,4))

def comida_lista(comida):
    assert comida in [
        'pizza',
        'sorvete'
    ], 'Comida não está na lista'
    return True

# print(comida_lista('pizza'))
# print(comida_lista('lasanha'))

"""
Doctests são feitos nas docstrings das funções e executados com:
python -m docteste -v nome_do_modulo.py
"""

def soma(a, b):
    """
    Soma os números a e b
    >>> soma(1,2)
    3

    >>> soma(5,5)
    10

    >>> soma(True, None)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'
    """
    return a + b