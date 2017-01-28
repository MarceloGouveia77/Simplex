# -*- coding: latin-1 -*-
from funcoes import *
from DBconnection import *
from matplotlib import pyplot as plt
from texttable import Texttable
import numpy as np
from parse import *

qtdVariaveis = int(input("Quantidade de variaveis: ")) + 2
qtdRestricoes = int(input("Quantidade de restricoes: "))
qtdColunas = qtdVariaveis + qtdRestricoes
matriz = np.zeros((qtdRestricoes+1,qtdColunas))
cabecalho = [None] * qtdColunas

qtdLinhas = qtdRestricoes+1

# DEFINE O CABEÇALHO
cabecalho[0] = str('Z')
cabecalho[qtdColunas-1] = 'S'
for i in range(1,qtdVariaveis-1):
	cabecalho[i] = 'x%d' %i
j = 1
for i in range(qtdVariaveis-1,qtdColunas-1):
	cabecalho[i] = 'F%d' %j
	j+=1

matriz[0][0] = 1
matriz[0][1] = -600
matriz[0][2] = -800

matriz[1][1] = 1
matriz[1][2] = 1
matriz[1][3] = 1
matriz[1][7] = 100

matriz[2][1] = 3
matriz[2][2] = 2
matriz[2][4] = 1
matriz[2][7] = 235

matriz[3][1] = 8
matriz[3][5] = 1
matriz[3][7] = 480

matriz[4][2] = 10
matriz[4][6] = 1
matriz[4][7] = 800

while(verifica_matrix(matriz)):
	c_entra = coluna_entra(matriz) # PEGA A POSIÇÃO DA COLUNA QUE ENTRA
	nova_linha, linha_pivo = nova_linha_pivo(matriz, qtdLinhas, c_entra) # CALCULA A NOVA LINHA PIVO, E RETORNA A POSIÇÃO DA LINHA

	for i in range(qtdLinhas): # CALCULA AS NOVAS LINHAS
		matriz[i] = calc_nova_linha(matriz, nova_linha, c_entra, i, linha_pivo)

	qtdeCol = ['t'] * qtdColunas # FORMATO PARA IMPRIMIR A TABELA

	imprimir = np.insert(matriz, 0, nova_linha, axis=0) # MATRIZ AUXILIAR PARA IMPRESSÃO
	tabela = Texttable()
	tabela.set_cols_dtype(qtdeCol)
	tabela.add_rows(imprimir)
	tabela.add_rows([cabecalho])
	print("")

	print(tabela.draw())

#print(np.array_str(matriz, precision = 2, suppress_small = True))
