# -*- coding: utf-8 -*-
"""Pregunta 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ucGWiEpebgCDNSvEybTK9XMDIqmVJri
"""

import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Trabajo/reto_precios.csv')
pd.set_option('display.max_columns', None)

df.head()

distinct_count = df['age_in_years'].nunique()
distinct_count

df.info()

df.describe()

msno.bar(df)

# Crear una subselección del DataFrame solo con las columnas relevantes
subset_df = df[['price_square_meter','days_on_site','bathrooms','parking_lots','num_bedrooms']]

# Calcular la matriz de correlación
correlation_matrix = subset_df.corr(method='pearson')

# Crear un mapa de calor de la matriz de correlación
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlación por metro cuadrado Pearson')
plt.show()

# Crear una subselección del DataFrame solo con las columnas relevantes
subset_df = df[['price_square_meter','days_on_site','bathrooms','parking_lots','num_bedrooms']]

# Calcular la matriz de correlación
correlation_matrix = subset_df.corr(method='spearman')

# Crear un mapa de calor de la matriz de correlación
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlación por metro cuadrado Spearman')
plt.show()

# Crear una subselección del DataFrame solo con las columnas relevantes
subset_df = df[['price_square_meter','days_on_site','bathrooms','parking_lots','num_bedrooms']]

# Calcular la matriz de correlación
correlation_matrix = subset_df.corr(method='kendall')

# Crear un mapa de calor de la matriz de correlación
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlación por metro cuadrado Spearman')
plt.show()



# Select the columns of interest
columns_of_interest = ['price_square_meter', 'num_bedrooms']
selected_data = df[columns_of_interest]

# Plotting the data
x = selected_data['num_bedrooms']
y = selected_data['price_square_meter']

plt.scatter(x, y)
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price per Square Meter')
plt.title('Relationship between Price per Square Meter and Number of Bedrooms')
plt.show()