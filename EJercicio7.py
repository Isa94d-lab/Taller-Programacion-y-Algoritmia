#Primero definimos a que contiene 'l1'=Primer lado del triangulo, 'l2'=Segundo lado, 'l3'=tercer lado
def a(l1, l2, l3):
    #Hacemos la condicion de que si (la suma de los 2 primeros lados)->(tiene que ser mayor a la longitud del 3 lado) tambien (la suma del primer lado y el ultimo)->(Tiene que ser mayor a la del 2) y (La suma del segundo y tercer lado)->(Tienen que ser mayores a las del 3 lado)
    #Solo si las 3 condiciones se cumplen PODEMOS formar el triangulo, de lo contrario NO  
    if (l1 + l2 >l3) and (l1+l3>l2) and (l2+l3>l1):
        print("Teniendo en cuenta que se cumplio la desigualdad triangular eso nos da como resultado : SI, SE PUEDE FORMAR UN TRIANGULO")
    else:
        print("Debido a que NO se cumplio la desigualdad triangular, NO SE PUEDE FORMAR EL TRIANGULO")
#Damos inicio al programa principal
if (__name__ == '__main__'):
    #Solicitamos el valor del primer lado
    l1=float(input("Ingresa la longitud del primer lado : ")) 
    #Solicitamos el valor del segundo lado
    l2=float(input("Ingresa la longitud del segundo lado : ")) 
    #Solicitamos el valor del tercer lado
    l3=float(input("Ingresa la longitud del tercer lado : ")) 
    l1=a(l1, l2, l3)