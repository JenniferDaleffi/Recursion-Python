# Recursion Python

PARA ESTUDOS: Python, Recursão Aprender a formular programas de forma recursiva.

Na aula dada pelo professor Fernando Almeida, aprendi sobre Recursão(Recursion)

* Recursão é um método de resolução de problemas que envolve quebrar um problema em subproblemas menores e menores até chegar a um problema pequeno o suficiente para que ele possa ser resolvido trivialmente. Normalmente recursão envolve uma função que chama a si mesma. Embora possa não parecer muito, a recursão nos permite escrever soluções elegantes para problemas que, de outra forma, podem ser muito difíceis de programar.(https://panda.ime.usp.br/pensepy/static/pensepy/12-Recursao/recursionsimple-ptbr.html)

# Objetivos

❥ Os objetivos deste capítulo são os seguintes:

❥ Entender que alguns problemas muito complexos podem ter uma solução recursiva simples.
Aprender a formular programas de forma recursiva.

❥ Entender e aplicar as três leis da recursão.

❥ Entender a recursão como uma forma de iteração.

❥ Implementar a formulação recursiva de um problema.

❥ Entender como a recursão é implementada por um sistema computacional.


# Como funciona?

Lista = [1,3,5,7,9]
soma (lista)

'''Return (1) + soma ([3,5,7,9])
Return (3) + soma ([5,7,9])
Return (5) + soma ([7,9])
Return (7) + soma ([9])
Para no 9 que vira o número da lsita que precisa obrigatoriamente voltar a primeira posição
somando assim valores quando retorna 9+7+ 16 + 5 = 21 + 3 = 24 + 1 + 25 retorna 25'''

