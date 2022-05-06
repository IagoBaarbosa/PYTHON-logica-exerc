# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Tem-se um conjunto de dados contendo a
#  * altura e o sexo (masculino, feminino) de 50
#  * pessoas. Fazer um algoritmo que calcule e
#  * escreva:
#  * o - a maior e a menor altura do grupo;
#  * o - a média de altura das mulheres;
#  * o - o número de homens;
#  *
#  * Autor(a) : Iago Barbosa
#  * Data atual : 29/03/2022
#  */


def sexoAltura():

    for i in range(0, 4):
        j = int(input('Escolha o sexo da pessoa [1] Mulher OU [2] Homem'))
        vetS.append(j)
        k = int(input('Digite uma altura: '))
        vetA.append(k)


def menorAltura():
    menor = vetA[1]
    for i in range(0, 4):
        if(vetA[i] < menor):
            menor = vetA[i]
    print('A menor altura e de: ', menor)


def maiorAltura():
    maior = 0
    for i in range(0, 4):
        if(vetA[i] > maior):
            maior = vetA[i]
    print('A maior altura e de: ', maior)


def mediaAlturaMulheres():
    qtMulheres = 0
    for i in range(0, 4):
        if(vetS[i] == 1):
            qtMulheres = qtMulheres + 1
            alturaTotal = vetA[i]
    print('A media das altura das mulher e de: ', alturaTotal/qtMulheres)


def numeroDeHomens():
    nh = 0
    for i in range(0, 4):
        if(vetS[i] == 2):
            nh = nh + 1
    print('O numero de homens e de: ', nh)


vetS = []
vetA = []
menor = 0
maior = 0
alturaTotal = 0
qtMulheres = 0
nh = 0
i = 0

sexoAltura()
menorAltura()
maiorAltura()
mediaAlturaMulheres()
numeroDeHomens()
