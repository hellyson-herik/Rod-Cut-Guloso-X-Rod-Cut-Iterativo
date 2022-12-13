import random
import time
from rod_cut_iterativo import printa_iterativo
from rod_cut_guloso import rod_cut_guloso
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n = []
tamanho_random = random.randint(10, 21)
vetor = []

for i in range(10):
    vetor_aux = []
    vetor.append(vetor_aux)
    n.append(random.randint(10, 500))

vetor[0].append(1)
for i in range(n[0]):
    vetor[0].append(random.randint(1, n[0]))

vetor[1].append(1)
for i in range(n[1]):
    vetor[1].append(random.randint(1, n[1]))

vetor[2].append(1)
for i in range(n[2]):
    vetor[2].append(random.randint(1, n[2]))

vetor[3].append(1)
for i in range(n[3]):
    vetor[3].append(random.randint(1, n[3]))

vetor[4].append(1)
for i in range(n[4]):
    vetor[4].append(random.randint(1, n[4]))

vetor[5].append(1)
for i in range(n[5]):
    vetor[5].append(random.randint(1, n[5]))

vetor[6].append(1)
for i in range(n[6]):
    vetor[6].append(random.randint(1, n[6]))

vetor[7].append(1)
for i in range(n[7]):
    vetor[7].append(random.randint(1, n[7]))

vetor[8].append(1)
for i in range(n[8]):
    vetor[8].append(random.randint(1, n[8]))

vetor[9].append(1)
for i in range(n[9]):
    vetor[9].append(random.randint(1, n[9]))


def tempo(vetor):
    vetor_rci = []
    vetor_rcg = []
    soma_rci = 0
    soma_rcg = 0
    media_rci = 0
    media_rcg = 0
    for count in range(tamanho_random):
        inicial_rci = time.time()
        printa_iterativo(vetor, len(vetor))
        final_rci = time.time()
        vetor_rci.append(final_rci - inicial_rci)

        inicial_rcg = time.time()
        rod_cut_guloso(vetor, len(vetor))
        final_rcg = time.time()
        vetor_rcg.append(final_rcg - inicial_rcg)

    for count in range(len(vetor_rci)):
        soma_rci += vetor_rci[count]
        soma_rcg += vetor_rcg[count]

        media_rci = soma_rci / tamanho_random
        media_rcg = soma_rcg / tamanho_random

    return [len(vetor), media_rci, media_rcg]


array = []
vetor_lucro_rci = []
vetor_cortes_rci = []
vetor_lucro_rcg = []
vetor_cortes_rcg = []
for count in range(10):
    array.append(tempo(vetor[count]))

    lucro_rci, corte_rci = printa_iterativo(vetor[count], len(vetor[count]))
    vetor_lucro_rci.append(lucro_rci)
    vetor_cortes_rci.append(corte_rci)

    lucro_rcg, corte_rcg = rod_cut_guloso(vetor[count], len(vetor[count]))
    vetor_lucro_rcg.append(lucro_rcg)
    vetor_cortes_rcg.append(corte_rcg)


for i in range(len(vetor_cortes_rci)):
    print(f'Cortes do barra no algoritmo Iterativo {i+1} foi: {vetor_cortes_rci[i]}')
print('-' * 90)
for i in range(len(vetor_cortes_rcg)):
    print(f'Cortes da barra no algoritmo Guloso {i+1} foi:{vetor_cortes_rcg[i]}')

print('*' * 90)
for j in range(len(vetor_lucro_rci)):
    if vetor_lucro_rci[j] < vetor_lucro_rcg[j]:
        print(f'Na barra {j+1}.')
        print(f'Lucro Guloso - R${vetor_lucro_rcg[j]} > Lucro Iterativo - R${vetor_lucro_rci[j]}.')

    if vetor_lucro_rci[j] > vetor_lucro_rcg[j]:
        print(f'Na barra {j+1}.')
        print(f'Lucro Iterativo - R${vetor_lucro_rci[j]} > Lucro Guloso - R${vetor_lucro_rcg[j]}')


df2 = pd.DataFrame(array, columns=['tamanho', 'mediaRCI', 'mediaRCG'])

with plt.style.context('Solarize_Light2'):
    colors = ['b', 'r']
    iterativo = plt.scatter(df2.tamanho, df2.mediaRCI, label='Iterativo', color=colors[0])
    guloso = plt.scatter(df2.tamanho, df2.mediaRCG, label='Guloso', color=colors[1])
    plt.title('Comparação do tempo de execução do Iterativo vs Guloso')
    plt.xlabel('Tamanho de entrada', fontsize=14)
    plt.ylabel('Tempo de execução μs)', fontsize=14)
    plt.legend((iterativo, guloso),
               ('Iterativo', 'Guloso', 'LucroI'),
               scatterpoints=1,
               loc='upper left',
               ncol=3,
               fontsize=8)
plt.show()


barWidth = 0.25
plt.figure(figsize=(10,5))

r1 = np.arange(len(vetor_lucro_rci))
r2 = [x + barWidth for x in r1]

plt.bar(r1, vetor_lucro_rci, color='#6A5ACD', width=barWidth, label='Iterativo')
plt.bar(r2, vetor_lucro_rcg, color='#6495ED', width=barWidth, label='Guloso')

plt.xlabel('Tamanho de entrada (n).')
plt.xticks([r + barWidth for r in range(len(vetor_lucro_rci))], ['Barra 1', 'Barra 2', 'Barra 3', 'Barra 4',
                                                                 'Barra 5', 'Barra 6', 'Barra 7', 'Barra 8',
                                                                 'Barra 9', 'Barra 10'])
plt.ylabel('Lucro ótimo (reais).')
plt.title('Comaparação do lucro ótimo do algoritmo iterativo vs algoritmo guloso.')

plt.legend()
plt.show()

