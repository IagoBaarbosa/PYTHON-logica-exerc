# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Fazer um algoritmo que calcule e escreva a soma dos
#  * 50 primeiros termos da seguinte serie:
#  * 1000/1 - 997/2 + 994/3 - 991/4 + ...
#  * Autor(a) : Iago Barbosa
#  * Data atual : 29/03/2022
#  */

denominador = 0
numerador = 0
somaTotal = 0

for i in range(denominador, 50):
    numerador = 1000 - (3*(denominador - 1))
    print(numerador)
    print(" ", denominador)
    print("   ")
    if(denominador % 2 == 0):
        print(" + ")
        somaTotal = somaTotal + (numerador/denominador)
    else:
        print(" - ")
        somaTotal = somaTotal - (numerador/denominador)
print('SOMA: ', somaTotal)
