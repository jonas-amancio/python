def comer(comida, saudavel):
    if saudavel:
        return f'{comida} é saudável.'
    return f'{comida} não é saudável.'

def dormir(horas):
    if horas >= 8:
        return 'Dormiu por tempo suficiente.'
    return 'Dormiu pouco.'
