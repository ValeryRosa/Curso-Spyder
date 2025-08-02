# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 20:45:20 2025

@author: valer
"""

import pandas as pd
import numpy as np
datos=pd.read_csv('datosyt.csv', encoding='latin1')
print(datos.dtypes)
print(datos.sort_values(by='xs',ascending=True))
df1=pd.DataFrame(np.sort(datos.values, axis=0),index=datos.index,columns=datos.columns)
print(df1)