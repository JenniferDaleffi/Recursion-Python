# Calculo fatorial com recursão

def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial(n-1)


# Principal

n = int(input('Número: '))
print(f'Fatorial de {n} é {fatorial(n)}')