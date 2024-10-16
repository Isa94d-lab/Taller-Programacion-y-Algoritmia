#Definimos a que contendra n=nombre del trabajador, z=en que año entro el trabajador a la empresa, p=apellidos y e= la edad
def a(n:str, z:int, p:str, e:int):
    #Decimos el nombre del trabajador
    print(f"Nombre del trabajador : {n}")
    #Sus apellidos
    print(f"Apellidos del trabajador : {p}")
    #Su edad
    print(f"Edad : {e}")
    #le restamos el año actual con el que ingreso el usuario
    w=2024-z
    #Damos la respuesta
    print(f"El trabajador lleva trabajando {w} años, teniendo en cuenta que estamos en el año 2024")
#Damos inicio al programa principal
if (__name__ == '__main__'):
    #Solicitamos el nombre del trabajador
    n=str(input("Ingresa tu nombre : "))
    #Sus apellidos
    p=str(input("Ingresa tus apellidos : "))
    #Su edad
    e=int(input("Ingresa tu edad : "))
    #Y en que año inicio a trabajar en la empresa
    z=int(input("En que año empezaste a trabajar con nosotros? : "))
    n=a(n, z, p, e)