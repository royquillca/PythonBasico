def run():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    # }
    # print(mi_diccionario)
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }
    # print(poblacion_paises['Argentina'])
    for pais in poblacion_paises.keys():
        print(pais)
    for poblacion in poblacion_paises.values():
        print(poblacion)
    for country, population in poblacion_paises.items():
        print(country + ' tiene ' + str(population) + ' habitantes.')


    # CODIGO 

    caballeros_dorados = {
        'aries': 'mu',
        'tauro': 'aldebaran',
        'cancer': 'deadmask',
        'geminis': 'saga',
        'leo': 'aioria',
        'virgo': 'shaka',
        'libra': 'dohko',
        'sagitario': 'aioros',
        'escorpion': 'milo',
        'capricornio': 'shura',
        'acuario': 'camus',
        'piscis': 'afrodita',
    }
    # for signo_zodiacal in caballeros_dorados.keys():
    #     print(signo_zodiacal)
    # for nombre_caballero in caballeros_dorados.values():
    #     print(nombre_caballero)
    # for signo_zodiacal, nombre_caballero in caballeros_dorados.items():
    #     print(str(signo_zodiacal).capitalize() + ': ' + str(nombre_caballero).capitalize())
    seguir = 's'
    while seguir.lower() == 's':
        llave = input('Escribe tu signo zodical: ').lower()
        print (f'El caballero que representa tu signo es: {str(caballeros_dorados[llave]).capitalize()}')
        seguir = input('Desea continuar S/N:')


if __name__ == '__main__':
    run()
