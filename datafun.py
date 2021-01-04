#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Repositorio de funciones útiles para utilizar con Datos en Python: Listas, Dataframes, Diccionarios, Numpy arrays...
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#LISTAS
#Función que devuelve valores de una lista (máximo, mínimo, número de elementos)
def value_list (lista):
	maximo=max(lista)
	minimo=min(lista)
	num_elem=len(lista)
	list_value=[maximo, minimo, num_elem]
	return (list_value)
prueba_lista=[1,2,3,4,5,8,9,10,15,68,321,-526,85,69]
valores=value_list(prueba_lista)
print(valores)
print("-----------End Function------")

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
print("-----------End Function------")
#Función que abre un archivo grande de datos
def read_large_file(file_object):
	while True:
		data=file_object.readline()
		if not data:
			break
		yield data

with open ('world_ind_pop_data.csv') as file:
	gen_file=read_large_file(file)
	print(next(gen_file))
	print(next(gen_file))
	print(next(gen_file))
print("-----------End Function------")
#Función que filtra valores por etiqueta en DataFrame
def filter_tag(reader, tag, valuetag, taginterest1, taginterest2):
#Get the first dataFrame
	df_pop=next(reader)
#Check out the specific tag
	df_ceb=df_pop[df_pop[tag]==valuetag]
#Zip DataFrame columns of interest
	interest=zip(df_ceb[taginterest1], df_ceb[taginterest2])
	interest_list=list(interest)
	return interest_list

pd_read=pd.read_csv('world_ind_pop_data.csv', chunksize=1000)
pd_interest=filter_tag(pd_read,'CountryCode','CEB','Total Population','Urban population (% of total)')
print(pd_interest)

print("-----------End Function------")







