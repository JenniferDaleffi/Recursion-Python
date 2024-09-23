#Calcular a soma de lista de números (com recursão)

def soma_numeros(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_numeros(lista[1:])

#Principal

lista = [1,3,5,7,9]
print(f'Soma: {soma_numeros(lista)}')
