#Definiendo la funcion palindromo
def palindromo(palabra):
    palabra = palabra.replace(' ', '') # Remplazar espacios vacios " " por ""
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): # Va hacer que el programa pueda correr al principio
    palabra = input('Ingrese una palabra:')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__  == '__main__': #Entry point = punto de entrada de un programa de Python
    run()



# EJEMPLOS DE PALINDROMOS:

# “Oí lo de mamá: me dolió”
# “Sometamos o matemos”
# “Yo dono rosas, oro no doy”
# “Isaac no ronca así”
# “Lavan esa base naval”
# “No traces en ese cartón”
# “¿Será lodo o dólares?”
# “Logra Casillas allí sacar gol”