from texttable import Texttable
import numpy as np

def inserir_matriz(matriz, restricao, pos_linha, lista_pos):
    qtdColunas = len(matriz[0])
    lista_aux = [0] * qtdColunas
    tam = len(restricao)

    for i in range(len(lista_pos)): # 
        pos = lista_pos[i]
        lista_aux[pos] = restricao[i] 
    lista_aux[qtdColunas-1] = restricao[tam-1]

    for i in range(qtdColunas):
        matriz[pos_linha][i] = float(lista_aux[i])
                
    return matriz

def funcao_objetiva(objetiva):
    objetiva = objetiva.split(" ")
    tam = len(objetiva)
    lista_aux = [None] * tam

    for i in range(len(objetiva)): # DETECTA SINAL NEGATIVO E APLICA À VARIAVEL
        if(objetiva[i] == '-'):
            tmp = objetiva[i+1]
            objetiva[i+1] = '-' + tmp

    for i in range(tam):
        string_tmp = objetiva[i]
        if(len(string_tmp) >= 3):
            lista_aux[i] = string_tmp

    for i in range(tam):
        if(lista_aux[i] != None):
            pos = len(lista_aux[i]) -2
            lista_aux[i] = float(lista_aux[i][:pos]) * (-1)

    lista_aux = [x for x in lista_aux if x is not None]
    qtd_variaveis = len(lista_aux) + 2
    lista_aux = [1] + lista_aux
    return lista_aux, qtd_variaveis

def calc_pos(string):
    tam = len(string)
    pos = int(string[tam-1:])
    return pos

def calc_restricao(restr):
    restr = restr.split(" ")
    tam = len(restr)
    lista_aux = [None] * tam
    lista_pos = [None] * tam

    for i in range(len(restr)): # DETECTA SINAL NEGATIVO E APLICA À VARIAVEL
        if(restr[i] == '-'):
            tmp = restr[i+1]
            restr[i+1] = '-' + tmp

    for i in range(tam): 
        string_tmp = restr[i]
        if(i == tam-1):
            lista_aux[i] = string_tmp
            break
        if(len(string_tmp) >= 3):
            lista_pos[i] = calc_pos(string_tmp) # CALCULA EM QUAL POS VAI CADA VARIÁVEL 
            lista_aux[i] = string_tmp

    for i in range(tam): # FILTRA APENAS OS NÚMEROS DA RESTRICAO
        if(i == (tam - 1)):
            break
        if(lista_aux[i] != None):
            pos = len(lista_aux[i]) -2
            lista_aux[i] = lista_aux[i][:pos]

    lista_aux = [x for x in lista_aux if x is not None]
    lista_pos = [x for x in lista_pos if x is not None]
    return lista_aux, lista_pos

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
        if(matriz[i][coluna] > 0):
            pivo_tmp = float(matriz[i][qtdColunas - 1] / matriz[i][coluna])
        else:
            continue
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
    qtdeCol = ['t'] * qtdColunas # FORMATO DA TABELA 'TEXTO'
    imprimir = np.insert(matriz, 0, linha, axis=0)  # LISTA AUXILIAR PARA IMPRESSÃO
    tabela = Texttable()
    tabela.set_cols_dtype(qtdeCol)
    tabela.add_rows(imprimir)
    tabela.add_rows([cabecalho])
    print("")
    print(tabela.draw())
    return None
