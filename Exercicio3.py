# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Fazer um algoritmo que:
#  * o Leia um número indeterminado de linhas
#  * contendo cada uma a idade de um indivíduo.
#  * o A última linha que não entrará nos cálculos,
#  * contém o valor da idade igual a zero.
#  * o Calcule e escreva a idade média deste grupo
#  * de indivíduos.
#  * o Escreva também a maior idade e a menor
#  * Autor(a) : Iago Barbosa
#  * Data atual : 28/03/2022
#  */

from statistics import mean


def fazTudo():
    idade = []
    for i in range(0, 5):
        j = int(input('Digite uma idade: '))
        idade.append(j)
    print('A maior idade foi: ', max(idade))
    print('A media das idades e: ', mean(idade))
    print('A menor idade e: ', min(idade))


fazTudo()
