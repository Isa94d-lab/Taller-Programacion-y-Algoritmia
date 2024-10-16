#Primero definimos a que por dentro tendra la edad
def a(e:int):
#preguntamos si e es mayor o = que 18
    if (e>=18): 
    #Si se cumple, es mayor de edad
        print("Eres mayor de edad")
    #Si no, por descarte es menor de edad
    else:
        print("Eres menor de edad")
#Iniciamos el programa principal 
if (__name__ == '__main__'):
    #Solicitamos e, la edad 
    e=int(input("Ingresa tu edad : "))
    e= a(e)
