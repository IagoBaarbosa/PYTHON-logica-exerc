# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Fazer um algoritmo para calcular e escrever a
#  * soma dos cubos dos números pares
#  * compreendidos entre B e A (B > A). B e A são
#  * lidos pelo teclado.
#  * Autor(a) : Iago Barbosa
#  * Data atual : 28/03/2022
#  */

def somaCuboPares(val_a, val_b):
    valorTotal = 0
    for i in range(val_a, val_b):
        if(i % 2 == 0):
            valorTotal = valorTotal + (i ** 3)
            print(i)
    return valorTotal


a = int(input('Digite um valor: '))
b = int(input('Digete outro valor, Obrigatorio ser maior que o anterior: '))
if (a >= b):
    print('ERRO!')


total = somaCuboPares(a, b)
print('A soma dos cubos dos numeros pares sao: ', total)
