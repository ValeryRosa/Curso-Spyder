# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 20:58:53 2025

@author: valer
"""

import pandas as pd
import numpy as np
df=pd.read_csv('canciones.csv', encoding='latin1')
filas=len(df.index)
print("Numero de filas: ",filas)
df.drop(df.index[[filas-1]], inplace=True)
filas=len(df.index)
print("Numero de filas: ",filas)
