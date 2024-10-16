#Primero definimos a que por dentro tendra las variables de año, mes y dia
def a(año, mes, dia):
    #Dividimos el año en 4, si el resultado es entero, el año sera BISIESTO
    j=año/4
        #Preguntamos se el resultado de la operacion anterior es un entereo, de ser correcta el año es bisiesto
    if (int(j)==j):
        print("El año es BISIESTO")
        l=True
    else: 
        print("El año es NO ES BISIESTO")
        l=False
    #Ponemos en rango cada mes, febrero no esta en esta parte ya que si rango puede variar dependiendo del año (si es bisiesto o no) 
    ene=(range(1, 31))
    feb=(range(1, 29 if l else 28))
    mar=(range(1, 31))
    abr=(range(1, 30))
    may=(range(1, 31))
    jun=(range(1, 30))
    jul=(range(1, 31))
    ago=(range(1, 31))
    sep=(range(1, 30))
    oct=(range(1, 31))
    nov=(range(1, 30))
    dic=(range(1, 31))
    #Por medio del march queremos saber que mes ingreso el usuario
    match mes:
        #Mes 1 es enero, 2 es febrero, 3 es marzo, etc. 
        case 1:
            print("Ingresaste el mes de enero")
            #Preguntamos si el dia ingresado por el usuario esta dentro del rango del mes
            if dia in ene:
                print("Ingresaste una fecha CORRECTA")
            else:
            #Si no esta, se da este mensaje
                print("La marcacion del dia fue incorrecta")
        case 2:
            print("Ingresaste el mes de febrero")
            #Preguntamos si el dia ingresado por el usuario esta dentro del rango del mes

            if dia in feb:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 3:
            print("Ingresaste el mes de marzo")
            if dia in mar:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 4:
            print("Ingresaste el mes de abril")
            if dia in abr:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 5:
            print("Ingresaste el mes de abril")
            if dia in may:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 6:
            print("Ingresaste el mes de junio")
            if dia in jun:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 7:
            print("Ingresaste el mes de julio")
            if dia in jul:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 8:
            print("Ingresaste el mes de agosto")
            if dia in ago:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 9:
            print("Ingresaste el mes de septiembre")
            if dia in sep:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 10:
            print("Ingresaste el mes de septiembre")
            if dia in oct:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 11:
            print("Ingresaste el mes de noviembre")
            if dia in nov:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case 12:
            print("Ingresaste el mes de diciembre")
            if dia in dic:
                print(f"Ingresaste una fecha CORRECTA -> {dia} / {mes} / {año}")
            else:
                print("La marcacion del dia fue incorrecta")
        case _:
            print("Marcaste un mes incorrecto por consiguiente tu dia tambien es erroneo")
#Iniciamos el programa principal
if (__name__ == '__main__'):
    #Solicitamos al usuario un año, un mes de ese año y un dia de ese mes
    año=int(input("Ingresa un año : "))
    mes=int(input("Ingresa un mes por su numero : "))
    dia=int(input("Ingresa un dia segun del mes ingresado anteriormente : "))
    año=a(año, mes, dia)




        
