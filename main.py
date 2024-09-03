import matplotlib.pyplot  as plt
import seaborn as sns
import numpy as np

#Configurar el generador de numeros aleatorios
rng = np.random.RandomState(0)

#Generar un rango de valores en el eje x
x = np.linspace(0,10,500)
#print(x)

#Generar datos aleatorios y calcular la suma acumulativa
y = np.cumsum(rng.randn(500,6),axis=0) #Sirve para hacer la suma acumulada de los datos

#Graficar los datos
plt.plot(x,y)
plt.legend('ABCDEF' , ncol = 2, loc = 'upper left')
plt.show()

#Aplicar estilo de seaborn
sns.set()
plt.plot(x,y)
plt.legend('ABCDEF' , ncol = 2, loc = 'upper left')
plt.show()


#Creacion de un grafico de dispersion
y_val = x ** 2 #Eleva al cuadrado cada valor del array x
plt.scatter(x,y_val,marker='o',color = 'g')
plt.title('Grafico de dispersion')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

print("Soy el perfil secundario de git y este es mi aporte al repositorio principal en la misma maquina.")
