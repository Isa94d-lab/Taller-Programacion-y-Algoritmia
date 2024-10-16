#Definimos a que contendra 'n' el numero ingresado por el usuario
def a(n:int):
    #Un acumulador el cual cada vez que se cumpla la condicion ira sumando el numero ingresado por el usuario
    c=0
    #Este contador ira sumando las veces que se cumpla el sistema, esto sera de utilidad para sacar el promedio
    h=0
    #Confirmamos que el primer numero sea positivo
    if (n>0):
        #Iniciamos un while en el que cuando sea un numero negativo, el while se detendra
        while n>0:
            c+=n
            h+=1
            n=int(input("Vuelve a ingresar un numero : "))
        #Realizamos el promedio de los numeros ingresados
        w=c/h
        print(f"El promedio de los numeros ingresados es de : {w}")
        return n
    #Si la primera condicion no se cumple no hay resultado del promedio
    else:
        print("Ingresaste un numero negativo")
if (__name__ == '__main__'):
    n=int(input("Ingresa un numero : "))
    n=a(n)

        

