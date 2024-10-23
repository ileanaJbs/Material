import pandas as pd

# Crear un Dataframe de ejemplo
data = {
    "Edad" : [23, 25, 26, 24, 30, 24, 22, 28, 27, 24],
    "Salario" : [48000, 52000, 58000, 49000, 60000, 48000, 50000, 62000, 59000, 54000]
}
df = pd.DataFrame(data)
print("Describe: ", "\n" , df.describe())
print() 

#Medidas de tendencia central
#Calcular media
media_edad = df['Edad'].mean()
media_salario = df['Salario'].mean()

#Calcular mediana
mediana_edad = df['Edad'].median()
mediana_salario = df['Salario'].median()

#Calcular moda
moda_edad = df['Edad'].mode()[0]
moda_salario = df['Salario'].mode()[0]

# Medidas de dispersion
# Calcular el rango
rango_edad = df['Edad'].max() - df['Edad'].min()
rango_salario = df['Salario'].max() - df['Edad'].min()

# Calcular la varianza
varianza_edad = df['Edad'].var()
varianza_salario = df['Salario'].var()

# Calcular la desviacion estandar
desviacion_edad = df['Edad'].std()
desviacion_salario = df['Salario'].std()

# Medidas de posicion
#Calcular percentiles

percentil_25_edad = df['Edad'].quantile(0.25)
percentil_50_edad = df['Edad'].quantile(0.50)
percentil_75_edad = df['Edad'].quantile(0.75)

percentil_25_salario = df['Salario'].quantile(0.25)
percentil_50_salario = df['Salario'].quantile(0.50)
percentil_75_salario = df['Salario'].quantile(0.75)

# Los cuartiles son simplemente los percentiles 25, 50 y 75
cuartil_1_edad = percentil_25_edad
cuartil_2_edad = percentil_50_edad
cuartil_3_edad = percentil_75_edad

cuartil_1_salario = percentil_25_salario
cuartil_2_salario = percentil_50_salario
cuartil_3_salario = percentil_75_salario

# Calcular los deciles
deciles_edad = df['Edad'].quantile([i/10 for i in range(1,10)])
deciles_salario = df['Salario'].quantile([i/10 for i in range(1,10)])

# Mostrar Resultados
print("Medidas de Tendencia Central")
print("Media - Edad:", media_edad, ", Salario:", media_salario)
print("Mediana - Edad:", mediana_edad, ", Salario:", mediana_salario)
print("Moda - Edad:", moda_edad, ", Salario:", moda_salario)
print()

print("Medidas de Dispersión")
print("Rango - Edad:", rango_edad, ", Salario:", rango_salario)
print("Varianza - Edad:", varianza_edad, ", Salario:", varianza_salario)
print("Desviación Estándar - Edad:", desviacion_edad, ", Salario:", desviacion_salario)
print ()

print("Medidas de Posición")
print("Percentiles - Edad: 25%,", percentil_25_edad, "50%", percentil_50_edad, "75%", percentil_75_edad)
print("Percentiles - Salario: 25%,", percentil_25_salario, "50%", percentil_50_salario, "75%")
print()

print("Cuartiles - Edad: Q1", cuartil_1_edad, "Q2", cuartil_2_edad, "Q3", cuartil_3_edad)
print("Cuartiles - Salario: Q1", cuartil_1_salario, "Q2", cuartil_2_salario, "Q3", cuartil_3_salario)
print()

print("Deciles - Edad:" ,  deciles_edad)
print("Deciles - Salario:" , deciles_salario)