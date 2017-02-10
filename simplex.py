# -*- coding: latin-1 -*-
from funcoes import *
from texttable import Texttable
import numpy as np

func_obj = input("Funcao Objetiva: ")
objetiva, qtdVariaveis = funcao_objetiva(func_obj)

qtdRestricoes = int(input("Quantidade de restricoes: "))
qtdColunas = qtdVariaveis + qtdRestricoes
qtdLinhas = qtdRestricoes + 1

matriz = np.zeros((qtdLinhas, qtdColunas)) # INICIALIZANDO A MATRIZ

for i in range(qtdVariaveis-1): # INSERINDO FUNÇÃO OBJETIVA NA MATRIZ
    matriz[0][i] = objetiva[i]

for i in range(1,qtdRestricoes+1): # INSERINDO AS RESTRIÇÕES NA MATRIZ
    restr = input("Restricao {} = ".format(i))
    restricao, array_pos = calc_restricao(restr)
    matriz = inserir_matriz(matriz, restricao, i, array_pos)
    matriz[i][(qtdVariaveis-2)+i] = 1

# DEFINE O CABEÇALHO
cabecalho = [None] * qtdColunas
cabecalho[0] = str('Z')
cabecalho[qtdColunas - 1] = 'S'
for i in range(1, qtdVariaveis - 1):
    cabecalho[i] = 'x%d' % i
j = 1
for i in range(qtdVariaveis - 1, qtdColunas - 1):
    cabecalho[i] = 'F%d' % j
    j += 1


qtdeCol = ['t'] * qtdColunas  # FORMATO PARA IMPRIMIR A TABELA
imprimir = np.insert(matriz, 0, matriz[0], axis=0)  # MATRIZ AUXILIAR PARA IMPRESSÃO
tabela = Texttable()
tabela.set_cols_dtype(qtdeCol)
tabela.add_rows(imprimir)
tabela.add_rows([cabecalho])
print("")

print(tabela.draw())

while verifica_matriz(matriz):
    c_entra = coluna_entra(matriz)  # PEGA A POSIÇÃO DA COLUNA QUE ENTRA
    print("ENTRA: ", cabecalho[c_entra])
    nova_linha, linha_pivo = nova_linha_pivo(matriz, qtdLinhas,
                                             c_entra)  # CALCULA A NOVA LINHA PIVO, E RETORNA A POSIÇÃO DA LINHA
    print("LINHA PIVO: ", nova_linha)

    for i in range(qtdLinhas):  # CALCULA AS NOVAS LINHAS
        matriz[i] = calc_nova_linha(matriz, nova_linha, c_entra, i, linha_pivo)

    imprimir = np.insert(matriz, 0, nova_linha, axis=0)  # MATRIZ AUXILIAR PARA IMPRESSÃO
    tabela = Texttable()
    tabela.set_cols_dtype(qtdeCol)
    tabela.add_rows(imprimir)
    tabela.add_rows([cabecalho])
    print("")

    print(tabela.draw())

