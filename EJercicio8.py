#Primero definimos a que contendra 'n', el numero ingresado por el usuario
def a(n:int):
    #Usamos el for para que una variable en este caso 'j' almacene el rando de (1, 11), (Ponemos 11 ya que si solol ponemos 10 el range contara hasta el 9)
    for j in range(1,11):
    #Multiplicamos el numero ingresado por cada uno de los numeros del rango gracias a 'j'
        w=(n*j)
    #Damos la respuesta
        print(f"el resultado de {n}*{j} es de {w}")
#Iniciamos el programa principal
if (__name__ == '__main__'):
    #Le solicitamos al usuario el numero que usaremos
    n=int(input("Ingresa un numero para saber su tabla de multiplicar : "))
    n=a(n)