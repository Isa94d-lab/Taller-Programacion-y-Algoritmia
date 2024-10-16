#Primero definimos a que contiendra la "contraseña" ingresada por el usuario
def a(t:str):
    #Este contador se encargara de contar cuantos caracteres tiene el texto ingresado por el usuario
    c=0
    #l es una lista la cual contiene numeros para poder identificar si 't' tiene algun numero dentro de su texto
    l=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #El for revisara cuales son los caracteres que hay en 't', el contador 'c' los contara, asi sabremos cuantos son
    for w in t: 
        c+=1
    #Tenemos una condicion la cual dice que si 't' tiene + o = caracteres que 8, podremos hacer otra condicion
    if (c>=8): 
        #Esta condicion nos dira si w la variable que reviso 't' tiene algun numero, esto lo hacemos por medio de la lista que ya habiamos creado 'l'
        if w in l:
        #Si se cumple, imprimimos que la contraseña es valida
            print("Contraseña VALIDA")
        #Si no, se le dice que su "contraseña" tiene que tener por lo menos un numero
        else:
            print("A tu contraseña debe tener un numero")
    #Si esta condicion no se cumple, le decimos al usuario que su contraseña no cumple con los requisitos
    else:
        print("Tu contraseña no cumple los requisitos, añadele mas caracteres")
#Iniciamos el programa principal
if (__name__ == '__main__'):
    #Le solicitamos al usuario que ingrese una posible contraseña
    t=(input("Ingresa tu contraseña : "))
    t=a(t)