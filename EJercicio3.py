#Primero definimos a que por dentro tendra la nota
def a(n):
    #preguntamos si la nota es mayor o = a 60, si se cumple aprueba
    if (n>=60):
        print("Felicidades aprobaste")
    #Si no, reprueba
    
    else:
        print("Lastimosamente reprobaste")
#Iniciamos el programa principal 
if (__name__ == '__main__'):
    #SOlicitamos n, es la nota ingresada por el usuario 
    n=int(input("Ingresa tu nota : "))
    n=a(n)