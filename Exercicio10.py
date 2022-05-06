# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Anacleto tem 1,50m e cresce 2
#  * centímetros por ano, enquanto Felisberto tem
#  * 1,10 e cresce 3 centímetros por ano. Construa
#  * um programa que calcule e apresente quantos
#  * anos serão necessários para que Felisberto
#  * seja maior que Anacleto
#  *
#  * Autor(a) : Iago Barbosa
#  * Data atual : 29/03/2022
#  */

def calcularAno():
    anacleto = 1.5
    felisberto = 1.1
    i = 0

    while (anacleto > felisberto):
        felisberto = felisberto + 0.03
        anacleto = anacleto + 0.02
        i = i + 1
    return i


total = calcularAno()
print('O total de anos que demoraria seria de: ', total)
