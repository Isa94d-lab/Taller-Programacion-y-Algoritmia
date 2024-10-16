#Definimos 'p'(el pais que ingresara el usuario) por medio de 'a'
def a(p:str):
#Hacemos una lista por cada continente con sus respectivos paises
    NorthAmerica=['Canada', 'Estados Unidos', 'Mexico']
    SurAmerica = [ 'Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Surinam', 'Uruguay', 'Venezuela']
    Asia=['Japon','China', 'Mongolia', 'Corea del Norte', 'Corea del Sur', 'Filipinas', 'Vietnam', 'Laos', 'Camboya', 'Myanmar', 'Tailandia', 'Malasia', 'Brunei', 'Singapur', 'Indonesia', 'Timor Oriental', 'Nepal', 'Bhutan', 'Bangladesh', 'India', 'Pakistan' ]
    Africa=['Egipto', 'Marruecos', 'Sudafrica','Argelia','Etiopia','Angola','Kenia','Sudan','Tanzania','Ghana','Tunez', 'Costa de Marfil', 'Uganda', 'Camerun', 'Zambia', 'Senegal', 'Libia', 'Namibia','Malaui', 'Mali', 'Botsuana', 'Mozambique', 'BurkinaFaso', 'Gabon', 'Zimbabue', 'Republica del Congo', 'Guinea', 'Mauricio', 'Guinea Ecuatorial', 'Chad', 'Benin', 'Namibia', 'Ruanda', 'Malaui', 'Níger', 'Somalia', 'Mauritania', 'Togo', 'Sierra Leona', 'Suazilandia','Eritrea', 'Burundi', 'Lesoto', 'Liberia', 'Gambia', 'Republica Centroafricana', 'Yibuti', 'Cabo Verde', 'Guinea-Bisau', 'Seychelles', 'Comoras', 'Santo Tome y Principe' ]
    Europa=['Bélgica', 'Bulgaria', 'Chequia', 'Dinamarca', 'Alemania', 'Estonia', 'Irlanda', 'Grecia', 'España', 'Francia', 'Croacia', 'Italia', 'Chipre', 'Letonia', 'Lituania', 'Luxemburgo', 'Hungria', 'Malta', 'Paises Bajos', 'Austria', 'Polonia', 'Portugal', 'Rumania', 'Eslovenia', 'Eslovaquia', 'Finlandia', 'Suecia']
    Oceania=['Australia','islas de Nueva Guinea', 'Nueva Zelanda', 'archipiélagos coralinos', 'Volcanicos de Melanesia', 'Micronesia', 'Polinesia']
    #Preguntamos continente por continente si el pais ingresado esta en alguno
    if (p in NorthAmerica): 
        print("El pais ingresado pertenece al continente de Norte America")
    elif (p in SurAmerica):
        print("El pais ingresado pertenece al continente de Sur America")
    elif (p in Asia):
        print("El pais ingresado pertenece al continente Asiatico")
    elif (p in Africa):
        print("El pais ingresado pertenece al continente Africano")
    elif (p in Europa):
        print("El pais ingresado pertenece al continente Europeo")
    elif (p in Oceania):
        print("El pais ingresado pertenece al continente de Oceania")
    else:
        print("Hiciste una marcacion erronea")
#Iniciamos el programa principal 
if (__name__ == '__main__'):
    #Le pedimos al usuario que ingrese el nombre de un pais
    p=str(input("Ingresa el nombre de un pais, que su primer letra sea mayuscula y el resto en minuscula y sin tildes : "))
    p=a(p)