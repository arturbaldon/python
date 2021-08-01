#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:21:53 2021

@author: artur

Estudo de caso 2
Um setor público precisa visualizar os resultados das eleições presidenciais
de 2018. É necessário criar um gráfico para demonstrar a quantidade de votos
dos três candidatos mais votados. Tal gráfico deve evidenciar as porcentagens
de cada um dos candidatos nas regiões Sudeste, Nordeste, Sul, Norte e
Centro-Oeste.

Dados retirados do site
https://tinyurl.com/427h3k2h
"""

import numpy as np
import matplotlib.pyplot as plt

regioes = ["SUDOESTE", "NORDESTE", "SUL", "NORTE", "CENTO-OESTE"]

bolsonaro = np.array([53.965, 28.187, 58.446, 50.357, 57.677])
haddad = np.array([20.74, 49.824, 19.213, 30.331, 20.59])
ciro = np.array([11.937, 16.214, 8.786, 7.657, 9.707])

index = np.arange(len(regioes))

plt.bar(index, bolsonaro, label="Bolsonaro", color="red", bottom=ciro+haddad)
plt.bar(index, haddad, label="Haddad", color="blue", bottom=ciro)
plt.bar(index, ciro, label="Ciro", color="yellow")

plt.xticks(index, regioes)
plt.xlabel("Regiões")
plt.legend()
plt.title("Distribuição de presidenciáveis nas regiões brasileiras")
plt.show
