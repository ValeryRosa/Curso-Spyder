# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 19:50:58 2025

@author: valer
"""
import pandas as pd

datos=pd.read_csv('movies3.csv', encoding='latin1')
df=pd.DataFrame(datos)
print(df)
print("Máxima duración de peliculas: ")
print(df['duration'].max())
minutos=df['duration'].max()
print("Las horas de la peli son: ", minutos//60)
print("La película más larga es: ")
idx=df['duration'].idxmax()
print(df.loc[idx,'movie_title'])
print("Comparación de likes entre géneros")
df1=df.groupby('genres')['movie_facebook_likes'].sum().reset_index()
print(df1)
print("El genero más gustado en Facebook: ")
likes=df.groupby('genres')['movie_facebook_likes'].sum().reset_index()
print(likes.loc[likes['movie_facebook_likes'].idxmax(),'genres'])
print("con: ", likes['movie_facebook_likes'].max()," likes")
print("¿Cuál es el promedio de presupuesto por director?")
df2=df.groupby('director_name')['budget'].mean().reset_index()
print(df2)
print("¿Cuál es el género que gasta más dinero?")
dinero=df.groupby('genres')['budget'].mean().reset_index()
print(dinero)
print("¿Cuál es actor que trae más ganancia?")
actor=df.groupby('actor_1_name')['gross'].max().reset_index()
print(actor)
