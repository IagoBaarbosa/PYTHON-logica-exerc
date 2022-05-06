# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Ler três notas de um aluno, calcular a média
#  * e informar se ele foi aprovado (Média ? 7),
#  * reprovado (Média < 7) ou aprovado com
#  * louvor (Média = 10)
#  * Autor(a) : Iago Barbosa
#  * Data atual : 28/03/2022
#  */

def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print('A media de suas notas foram: ', media)
    if media > 7:
        print('Voce foi aprovado com media: ', media)
    if media < 7:
        print('Voce foi reprovado com media: ', media)
    if media == 10:
        print('Aprovado com louvor media de: ', media)


nota1 = float(input('Qual foi sua primeira nota: '))
nota2 = float(input('Qual foi sua segunda nota: '))
nota3 = float(input('Qual foi sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

calcularMedia(nota1, nota2, nota3)
