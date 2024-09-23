#Função para somar todos os números de uma lista

def soma_numeros(lista):
    soma = 0 
    for i in lista:
        soma+=i
    return soma

#Principal

lista = [1,3,5,7,9]
print(f'Soma: {soma_numeros(lista)}')