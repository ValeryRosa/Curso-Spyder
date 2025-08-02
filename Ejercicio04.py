# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 19:24:06 2025

@author: valer
"""

import pandas as pd
import numpy as np
datos=pd.read_csv('Data.csv', encoding='latin1')
print(datos.info())
print(datos.head())
print(datos.iloc[0:30]) #Muestra valores del 0 al 30
print(datos.iloc[[0,2,3,100,200,239]])
print(datos.iloc[:,0:2]) #Muestra todas la filas :, muestra las dos primeras columnas
print(datos.iloc[[0,23,63,45],[0,6,2]]) #Muestra las filas, de estas columnas
print(datos.iloc[0:10,0:5])