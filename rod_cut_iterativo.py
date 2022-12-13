def printa_cortes_iterativo(precos, tamanho):
    lucro, ponto_cortes = rod_cut_iterativo(precos, tamanho)
    while tamanho > 0:
        print(f"Corte de tananho: {ponto_cortes[tamanho]}.")
        tamanho = tamanho - ponto_cortes[tamanho]
    print(f'Máximo lucro obtido: {lucro} reais.')


def printa_iterativo(precos, tamanho):
    lucro, ponto_cortes = rod_cut_iterativo(precos, tamanho)
    cortes = []
    while tamanho > 0:
        cortes.append(ponto_cortes[tamanho])
        tamanho = tamanho - ponto_cortes[tamanho]
    return lucro, cortes


def rod_cut_iterativo(p, n):
    lucro = [-1] * (n + 1)
    lucro[0] = 0
    cortes = [-1] * (n + 1)
    for i in range(1, n + 1):
        maior = -1
        for j in range(1, i + 1):
            possivel_maior = p[j-1] + lucro[i - j]
            if maior < possivel_maior:
                maior = possivel_maior
                cortes[i] = j
        lucro[i] = maior
    return lucro[n], cortes

# #
# prices = [1, 3, 11, 15, 20, 10, 4, 2, 1, 5, 4]
# lucro, cortes = printa_iterativo(prices, len(prices))
# print(lucro)
# print(cortes)