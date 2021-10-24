import random


def run():
    numero_aleatorio = random.randint(1,100) # Pide un numero aleatorio al PC entre el 1 y 100
    numero_elegido = int(input('Elige un numero del 1 al 100: '))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mayor')
        else:
            print('Busca un numero mas pequeño')
        numero_elegido = int(input('Elige de nuevo el numero: '))
        
    else:
        print('Ganaste!')




if __name__ == '__main__':
    run()
