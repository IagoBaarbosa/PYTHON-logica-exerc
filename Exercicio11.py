# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Construa um programa que exiba a tabuada N.
#  * Autor(a) : Iago Barbosa
#  * Data atual : 29/03/2022
#  */

def calculo():
    n = int(input('Digite o numero da tabuada de sua preferencia: '))
    i = 0
    for i in range(0, 11):
        print(n, ' X ', i, ' = ', i*n)


calculo()
