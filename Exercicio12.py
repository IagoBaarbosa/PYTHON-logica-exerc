# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Fazer um algoritmo para calcular e
#  * escrever a seguinte soma:
#  * 37x38/1 + 36x37/2 + 35x36/2 + ... + 1x2/37
#  *
#  * Autor(a) : Iago Barbosa
#  * Data atual : 29/03/2022
#  */

denominador = 1
numeradorA = 0
numeradorB = 0
somaTotal = 0

for i in range(denominador, 38):
    denominador = denominador + 1
    numeradorA = 37 - (denominador - 1)
    numeradorB = numeradorA + 1

    somaTotal = somaTotal + ((numeradorA * numeradorB)/denominador)
    print(' ( ', numeradorA, ' x ', numeradorB, ' )/ ', denominador)
print('A soma e de: ', somaTotal)
