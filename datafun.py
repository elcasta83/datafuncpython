#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Repositorio de funciones útiles para utilizar con Datos en Python: Listas, Dataframes, Diccionarios, Numpy arrays...
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Función que analiza tweets de twitter de un archivo llamado 'tweets.csv'
def count_entries(df, *args):
	"""Return a dictionary with counts of occurrences as value for each key"""
	cols_count={}
	try:
		for col_name in args:
			col=df[col_name]
			for entry in col:
				if entry in cols_count.keys():
					cols_count[entry]+=1
				else:
					cols_count[entry]=1
		return(cols_count)
	except:
		print("The DataFrame does not have a " +col_name + " column.")	
df=pd.read_csv('tweets.csv')
result1=count_entries(df,'lang')
result2=count_entries(df,'lang','sourc')
print(result1)
print(result2)
