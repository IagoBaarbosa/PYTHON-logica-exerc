# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Número primo é aquele que só é divisível
#  * por ele mesmo e pela unidade. Fazer um
#  * algoritmo que determine e escreva os
#  * números primos compreendidos entre um
#  * intervalo fornecido pelo usuário.
#  *
#  * Autor(a) : Iago Barbosa
#  * Data atual : 29/03/2022
#  */

def numeroEprimo(valor):
    for i in range(2, valor):
        if(valor % i == 0):
            return False
        return True


numeroA = int(input('Escreva um valor INICIAL '))
numeroB = int(
    input('Escreva um valor FINAL, obrigatorio ser maior que o INICIAL'))
if(numeroA > numeroB):
    print('ERRO!')
print('No intervalo fornecido pelo USUARIO os numeros primos entre eles sao: ')
for i in range(numeroA, numeroB):
    if(numeroEprimo(i)):
        print('O numero ', i, ' e primo? ', numeroEprimo(i))
