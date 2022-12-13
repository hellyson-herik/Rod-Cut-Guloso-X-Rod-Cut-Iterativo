def printa_cortes_guloso(precos, tamanho):
    lucro, ponto_cortes = rod_cut_guloso(precos, tamanho)
    ponto_cortes.reverse()
    while tamanho > 0:
        corte = ponto_cortes.pop()
        print(f"Corte de tananho: {corte}.")
        tamanho = tamanho - corte
    print(f'Máximo lucro obtido: {lucro} reais.')


def rod_cut_guloso(p, n):
    lucro_total = 0
    cortes_totais = []
    lucro = []
    corte = []
    densidade = list()
    for count in range(n):
        densidade.append(p[count]/(count+1))
    maior = max(densidade)
    for count in range(n):
        if p[count]/(count+1) == maior:
            lucro.append(p[count])
            corte.append(count+1)
    tamanho_restante = n - corte[-1]
    if tamanho_restante > 0:
        lucro_restante, corte_restante = rod_cut_guloso(p, tamanho_restante)
        lucro.append(lucro_restante)
        corte.append(corte_restante)
    for count in range(len(lucro)):
        lucro_total += lucro[count]
        cortes_totais = lista_simples(corte)
    return lucro_total, cortes_totais


def lista_simples(lista):
    if isinstance(lista, list):
        return [sub_elem for elem in lista for sub_elem in lista_simples(elem)]
    else:
        return [lista]

# #
# prices = [1, 3, 11, 15, 20, 10, 4, 2, 1, 5, 4]
# lucro, cortes = rod_cut_guloso(prices, len(prices))
# print(lucro)
# print(cortes)