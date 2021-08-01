#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:07:17 2021

@author: artur

Estudo de caso 1
Precisamos apresentar um gráfico de barras para demonstrar o ganho de medalhas
de cinco países, os dados serão criados manualmente neste estudo, visto que o
intuito é demonstrar o uso de um gráfico de barras segmentadas.
"""

# inportação de pacotes
import numpy as np
import matplotlib.pyplot as plt

# relação de países da amostra
paises = ["EUA", "China", "Brasil", "Argentina", "Alemanha"]

# dados referente a cada país e suas respectivas medalhas 
ouro = np.array([46, 27, 26, 19, 17])
prata = np.array([37, 23, 18, 18, 10])
bronze = np.array([38, 17, 26, 19, 15])

# criação de um vetor de indices para o eixo x do gráfico
ind = np.arange(len(paises))

# barra de medalhas de ouro
plt.bar(ind, ouro, label="Ouro", color="#c9b037", bottom=prata+bronze)

# barra de medalhas de prata
plt.bar(ind, prata, label="Prata", color="#b4b4b4", bottom=bronze)

# barra de medalhas de bronze
plt.bar(ind, bronze, label="Bronze", color="#ad8a56")

# associação dos nomes dos países para cada indice do eixo X
plt.xticks(ind, paises)

# rótulos dos eixos X e Y
plt.xlabel("Países")
plt.ylabel("Medalhas")

# legenda padrão para as três medalhas
plt.legend()

# título do gráfico
plt.title("Medalhas - Olimpíadas 2018")

# exibe o gráfico
plt.show
