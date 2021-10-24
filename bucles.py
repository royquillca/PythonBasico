#Definir la funcion entrada:
#numero = input('Ingresa el numero:')

def run():
    LIMITE = 1000 #constante por estar escrito en MAYUSCULA
    contador = 1
    potencia_2 = 2**contador
    #Definir el ciclo
    while potencia_2 < LIMITE:
        print('2 elevado a ' +str(contador) + ' es igual a: ' +  str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
#
#


#
#
if __name__ == '__main__':
    run()