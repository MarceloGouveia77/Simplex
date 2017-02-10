def funcao_objetiva(objetiva):
    objetiva = objetiva.split(" ")
    tam = len(objetiva)
    string_aux = [None] * tam

    for i in range(tam):
        string_tmp = objetiva[i]
        if(len(string_tmp) >= 3):
            string_aux[i] = string_tmp

    for i in range(tam):
        if(string_aux[i] != None):
            pos = len(string_aux[i]) -2
            string_aux[i] = int(string_aux[i][:pos]) * (-1)

    string_aux = [x for x in string_aux if x is not None]
    qtd_variaveis = len(string_aux) + 2
    return string_aux, qtd_variaveis

def calc_restricao(restr):
    restr = restr.split(" ")
    tam = len(restr)
    string_aux = [None] * tam

    for i in range(tam):
        string_tmp = restr[i]
        if(i == tam-1):
            string_aux[i] = string_tmp
            break
        if(len(string_tmp) >= 3):
            string_aux[i] = string_tmp

    for i in range(tam):
        if(i == (tam - 1)):
            break
        if(string_aux[i] != None):
            pos = len(string_aux[i]) -2
            string_aux[i] = string_aux[i] = string_aux[i][:pos]

    string_aux = [x for x in string_aux if x is not None]
    print(string_aux)

def coluna_entra(matriz):
    qtdColunas = len(matriz[0])
    menor = 0
    for i in range(qtdColunas):
        if (matriz[0][i] < menor):
            menor = matriz[0][i]
            coluna = i
    return coluna

def nova_linha_pivo(matriz, qtdLinhas, coluna):
    nova_linha = [None] * len(matriz[0])
    qtdColunas = len(matriz[0])
    menor = 999999
    for i in range(1, qtdLinhas):
        if (matriz[i][coluna] != 0):
            pivo_tmp = matriz[i][qtdColunas - 1] / matriz[i][coluna]
        if ((pivo_tmp >= 0) and (pivo_tmp < menor)):
            menor = pivo_tmp
            linha = i
    pivo = matriz[linha][coluna]
    for i in range(qtdColunas):
        nova_linha[i] = matriz[linha][i] / pivo
    return nova_linha, linha

def calc_nova_linha(matriz, linha_pivo, coluna, pos, linha_p):
    qtdColunas = len(matriz[0])
    vetor = [None] * qtdColunas
    pivo = -matriz[pos][coluna]
    if (linha_p == pos):
        return linha_pivo
    for i in range(qtdColunas):
        vetor[i] = (linha_pivo[i] * pivo) + matriz[pos][i]
    return vetor

def verifica_matriz(matriz):
    qtdColunas = len(matriz[0])
    for i in range(qtdColunas):
        if (matriz[0][i] < 0):
            return True
    return False
