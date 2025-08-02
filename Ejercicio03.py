# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 18:41:25 2025

@author: valer
"""
import pandas as pd
import numpy as np
datos=pd.read_csv('Data.csv', encoding='latin1')
print(datos.info())
print('\n'*5)
print(datos.head()) #muestra los 5 primeros datos
print('\n'*5)
nuevo= pd.DataFrame(datos)
nuevo=nuevo.replace(np.nan,"0")
print(nuevo.info())
print(nuevo.describe())
print(nuevo.describe())
nuevo=nuevo.replace("N/A","0")
nuevo=nuevo.replace("NR","0")
nuevo['WRank']= nuevo['WRank'].astype(int)
nuevo['Wsets']= nuevo['Wsets'].astype(int)
print(nuevo)
print('\n'*5)
print(nuevo.describe())
