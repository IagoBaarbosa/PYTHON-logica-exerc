# /*  Disciplina   : [Linguagem e Lógica de Programação]
#  Professor   : Yuri Titi
#  Descrição   :   Determinar se um número é par ou ímpar e
#                  positivo ou negativo

#  Autor(a)    : Iago Barbosa
#  Data atual  : 28/03/2022 */


numero = int(input('Digite um numero qualquer: '))
if numero % 2 == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))
if numero >= 0:
    print('O numero é POSITIVO')
else:
    print('O numero é NEGATIVO')
