# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 17:19:01 2025

@author: valer
"""

import pandas as pd
import numpy as np

datos={
  "Nombre":["Pedro","Ana","Luis","N/A","Juan"],
  "Calificacion":[8,9,7,6,10],
  "Deportes":["Futbol","Baloncesto","Tenis","Natación","Ciclismo"],
  "Materia":["Matematicas","Historia","Ciencias","Lengua","Inglés"],
  "Edad":[15,16,15,17,16]
}
df=pd.DataFrame(datos)
print(df)
print('\n'*5)

datos2={
  "Nombre":["Pedro","Ana","Luis","N/A","Juan"],
  "Calificacion":["8","9","7",np.nan,"10"],
  "Deportes":["Futbol","Baloncesto","Tenis","Natación","Ciclismo"],
  "Materia":["Matematicas","Historia","Ciencias","Lengua","Inglés"],
  "Edad":[15,16,15,17,16]
}
df2=pd.DataFrame(datos2)
print(df2)
print(df2.info())#Informacion general del dataframe
print('\n'*5)
print(df.describe()) 
#PARA DATOS NUMÉRICOS: count:valores, mean:promedio general, std:desviacion estandar, min:valor minimo, 25%:primer cuartil, 50%:media, 75%:tercer cuartil, max:valor máximo
#PARA DATOS NO NUMERICOS: Top:numero de veces que se repite
print('\n'*5)

nuevo=pd.DataFrame(df2)
print(nuevo)
nuevo=nuevo.replace(np.nan,"0") #Reemplazar NaN por 0
print(nuevo)
columna=df2[df["Nombre"]!="N/A"]
print(columna)
print('\n'*5)

nuevo["Calificacion"]=nuevo["Calificacion"].astype(int) #Convertir valores String a int
print(nuevo.describe())