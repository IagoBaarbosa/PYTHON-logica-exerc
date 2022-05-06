# /*
#  * Disciplina : [Linguagem e Lógica de Programação]
#  * Professor : Yuri Titi
#  * Descrição : Numa eleição existem três candidatos
#  * identificados pelos números 1, 2 e 3. Faça um
#  * algoritmo que compute o resultado de uma
#  * eleição. Inicialmente o programa deve pedir o
#  * número total de votantes. Em seguida, deve
#  * pedir para cada votante votar (informando o
#  * número do candidato) e ao final mostrar o
#  * número de votos de cada candidato
#  * Autor(a) : Iago Barbosa
#  * Data atual : 28/03/2022
#  */

cd1 = 0
cd2 = 0
cd3 = 0
nulo = 0

numeroVotantes = int(input('Quantas pessoas iram votar? '))
for i in range(0, numeroVotantes):
    print('Digite [1] - para candidato 01')
    print('Digite [2] - para candidato 02')
    print('Digite [3] - para candidato 03')
    voto = int(input(' Eleitor numero:{}º Digite seu voto '.format(i)))

    if (voto == 1):
        cd1 = cd1 + 1
    elif (voto == 2):
        cd2 = cd2 + 1
    elif (voto == 3):
        cd3 = cd3 + 1
    else:
        nulo = nulo + 1

print('O candidato [1] recebeu ', cd1, 'votos')
print('O candidato [2] recebeu ', cd2, 'votos')
print('O candidato [3] recebeu ', cd3, 'votos')
print('Houveram: ', nulo, 'votos nulos ')
