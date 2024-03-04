def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonacci(n-2)+fibonacci(n-1))

n=int(input("Ingrese el valor de n: "))
print("El resultado de la secuencia: ")
for n in range(0,n):
    print (fibonacci(n))

#Clase para una calculadora simple
    class Calculadora:
        def __init__(self):
            self.resultado = 0
        
        #Metodo para sumar dos
        def sumar(self,a,b):
            self.resultado = a + b
            return  self.resultado
        #Metodo para restar
        def restar(self,a,b):
            self.resultado = a - b
        #Metodo para multiplicar
        def multiplicar(self,a,b):
            self.resultado=a*b

#Objeto de la clase
calc = Calculadora()
#Uso del metodo sumar
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
resultado=calc.sumar(a,b)
print("La suma de ",a,"+",b,"=",resultado)             




