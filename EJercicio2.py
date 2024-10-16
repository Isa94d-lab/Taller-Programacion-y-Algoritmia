#Primero definimos 'a' que contiene 'e' -> el numero que ingresara el usuario
def a(e:int):
#Ahora creamos una cariable la cual se encargara de almacenar los numeros antedesesores 'e'
    h=[]
#Inicialisamos un contador el cual se encargara de ir sumando las veces que se repita el while
    c=1
        #Hasta que 'c' sea mayor o = a 'e' el programa no se detendra
    while c<=e:
        h+=[c]
        #'c' lo estamos añadiendo a la lista hasta llegar a 'e' y mostrar los numeros anteriores a 'e' 
        c+=1
        #Cada vez que se repite el while 'C' va a ir sumando de uno en uno hasta que sea igual que 'e' 
        h+=[c]
    #Damos el resultado 
    print(f"Los numeros des 1 hasta {e} son -> {h}")

#Iniciamos el programa principal
if (__name__ == '__main__'):
    #Le pedimos al usuario que ingrese un numero entero positivo
    e=int(input("Ingresa un numero entero positivo : "))
    e=a(e)
