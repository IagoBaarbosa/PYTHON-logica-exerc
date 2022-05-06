# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Faça um algoritmo que lê uma temperatura
#  * em Fahrenheit e calcula a temperatura
#  * correspondente em Celsius. Ao final o
#  * programa deve exibir as duas temperaturas.
#  * - Usar a fórmula: C = (5 * (F-32) / 9)
#  *
#  * Autor(a) : Iago Barbosa
#  * Data atual : 28/03/2022
#  */

temp1 = float(input('Digite uma temperatura em Fahrenheit: '))
print('A temperatura convertida para Celsius e de: ', (5 * (temp1 - 32)/9))
resposta = str(
    input('Quer converter de Celsius para Fahrenheit? SIM ou NAO \n'))
resposta = resposta.upper()
if (resposta == 'SIM'):
    temp2 = float(input('Digite uma temperatura em Celsius: '))
    print('A temperatura convertida de Celsius para Fahrenheit e de:',
          (9 * temp2 + 160) / 5)
else:
    print('OK! muito obrigado')
    exit()
