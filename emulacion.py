import random #Numero aleatorios
import math #Biblioteca para funciones matematicas
#Funcion Activacion ("Funcion sigmoideal")
def sigmoideal(x):
    return 1/(1+pow(2.71828,-x))

#Clase para el modelo de red neuronal
class RedNeuronal:
    def __init__(self,nodos_entrada,nodos_ocultos,nodos_salida):
        self.nodos_entrada=nodos_entrada
        self.nodos_ocultos=nodos_ocultos
        self.nodos_salida=nodos_salida

        #Pesos aleatorios para las conexiones entre las capas (capa entrada - capa oculta)
        self.pesos_entrada_ocultos=[[random.uniform(-1,1) for _ in range(self.nodos_ocultos)] for _ in range(self.nodos_entrada)]
        #Pesos aleatorios para las conexiones entre las capas (capa oculta - capa salida)
        self.pesos_ocultos_salida=[[random.uniform(-1,1)for _ in range(self.nodos_salida)]for _ in range(self.nodos_ocultos)]
    
    #Funcion de Propagacion - (Propagacion hacia adelante)
    def propagacion(self, entradas):
        #Capa Oculta
        entradas_ocultas=[0]*self.nodos_ocultos
        for i in range(self.nodos_ocultos):
            for j in range(self.nodos_entrada):
                entradas_ocultas[i]+=entradas[j]*self.pesos_entrada_ocultos[j][i]
            entradas_ocultas[i]=sigmoideal(entradas_ocultas[i])
        
        #Capa Salida
        salidas_finales=[0]*self.nodos_salida
        for i in range(self.nodos_salida):
            for j in range(self.nodos_ocultos):
                salidas_finales[i]+=entradas_ocultas[j]*self.pesos_ocultos_salida[j][i]
            salidas_finales[i]=sigmoideal(salidas_finales[i])
        
        return salidas_finales


#Ejemplo de prueba del modelo
nodos_entrada=3
nodos_ocultos=4
nodos_salida=2

#Crearnos la instancia de la clase redNeuronal
red_neuronal=RedNeuronal(nodos_entrada,nodos_ocultos,nodos_salida)

#Entradas de Prueba
entradas=[0.5,0.3,0.8]

#Salida del modelo (prediccion)
salida=red_neuronal.propagacion(entradas)

#mostrar el resultado final de la prediccion
print("Salida de la red neuronal: ",salida)