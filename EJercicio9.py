#Primero definimos a que contendra los datos que nos dara el usuario como el consumo de kw, tar=Lo que paga por kw y est=estrato
def a(consumo, tar, est):
    #Multiplicamos el consumo*tarifa ya que eso nos dara la base de la factura
    c=consumo*tar
    #Preguntamos si es estrato 1 ya q los estratos<=3 suelen tener un subsidio del gobierno en sus facturas
    if (est==1):
        print("Al pertenecer al estrato social 1 se te dara un subsidio del 60% para tu factura electrica")
        #Sacamos en este caso el 60% de la base de la factura
        h=c*0.6
        #Luego se la restamos y ese va a ser el total a pagar por esa factura
        t=c-h
        print(f"Tu total a pagar de esta factura es de : {t}")
        #Se repite el mismo proceso
    elif (est==2):
        print("Al pertenecer al estrato social 2 se te dara un subsidio del 50% para tu factura electrica")
        #En este caso en lugar de ser del 60% ahora es del 50% ya que estamos en estrato 2
        h=c*0.5
        t=c-h
        print(f"Tu total a pagar de esta factura es de : {t}")
        #Se vuelve a repetir el proceso
    elif (est==3):
        #Lo unico diferente es que ahora es de 15% el subsidio
        print("Al pertenecer al estrato social 3 se te dara un subsidio del 15% para tu factura electrica")
        h=c*0.15
        t=c-h
        print(f"Tu total a pagar de esta factura es de : {t}")
    else:
        #Si no cumple ninguna de estas condiciones significa que es mayor a 3 por lo que, no clasifica para el subsidio
        print(f"Tu estrato, no califica. Total a pagar de esta factura es de : {c}")
#Damos inicio al programa principal
if (__name__ == '__main__'):
    #Le solicitamos al usuario su consimo de kw en el mes
    consumo=float(input("Ingresa tu consumo de kw de este mes : "))
    #Solicitammos la tarifa de kw
    tar=float(input("Ingresa el valor de la tarifa por kw : "))
    #Por ultimo pedimos el estrato para saber si se le aplicara un subsidio o no
    est=int(input("Ingresa el numero de tu estrato : "))
    consumo=a(consumo, tar, est)
    