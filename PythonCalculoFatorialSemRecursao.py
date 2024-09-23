# Calculo do Fatorial(sem recursão)

def fatorial(n):
    soma = 1 
    for i in range(1, n+1):
        soma *= i 
        return soma

# Principal
n = int(input('Número: '))
print(f'Fatorial de {n} é {fatorial(n)}')