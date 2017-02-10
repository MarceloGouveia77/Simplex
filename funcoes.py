from texttable import Texttable
import numpy as np

def inserir_matriz(matriz, restricao, pos_linha, array_pos):
    qtdColunas = len(matriz[0])
    vet_aux = [0] * qtdColunas
    tam = len(restricao)

    for i in range(len(array_pos)): # 
        pos = array_pos[i]
        vet_aux[pos] = restricao[i] 
    vet_aux[qtdColunas-1] = restricao[tam-1]

    for i in range(qtdColunas):
        matriz[pos_linha][i] = float(vet_aux[i])
                
    return matriz

def funcao_objetiva(objetiva):
    objetiva = objetiva.split(" ")
    tam = len(objetiva)
    array_aux = [None] * tam

    for i in range(tam):
        string_tmp = objetiva[i]
        if(len(string_tmp) >= 3):
            array_aux[i] = string_tmp

    for i in range(tam):
        if(array_aux[i] != None):
            pos = len(array_aux[i]) -2
            array_aux[i] = int(array_aux[i][:pos]) * (-1)

    array_aux = [x for x in array_aux if x is not None]
    qtd_variaveis = len(array_aux) + 2
    array_aux = [1] + array_aux
    return array_aux, qtd_variaveis

def calc_pos(string):
    tam = len(string)
    pos = int(string[tam-1:])
    return pos

def calc_restricao(restr):
    restr = restr.split(" ")
    tam = len(restr)
    array_aux = [None] * tam
    array_pos = [None] * tam

    for i in range(tam):
        string_tmp = restr[i]
        if(i == tam-1):
            array_aux[i] = string_tmp
            break
        if(len(string_tmp) >= 3):
            array_pos[i] = calc_pos(string_tmp)
            array_aux[i] = string_tmp

    for i in range(tam):
        if(i == (tam - 1)):
            break
        if(array_aux[i] != None):
            pos = len(array_aux[i]) -2
            array_aux[i] = array_aux[i][:pos]

    array_aux = [x for x in array_aux if x is not None]
    array_pos = [x for x in array_pos if x is not None]
    #array_aux = [0] + array_aux
    return array_aux, array_pos

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

def imprime_matriz(matriz, cabecalho, qtdColunas):
    linha = [0] * qtdColunas
    qtdeCol = ['t'] * qtdColunas 
    imprimir = np.insert(matriz, 0, linha, axis=0)  # MATRIZ AUXILIAR PARA IMPRESSÃO
    tabela = Texttable()
    tabela.set_cols_dtype(qtdeCol)
    tabela.add_rows(imprimir)
    tabela.add_rows([cabecalho])
    print("")
    print(tabela.draw())
    return None
