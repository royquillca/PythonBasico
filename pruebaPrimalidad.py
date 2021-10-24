"""
Criterio de logica de programacion.
Sabemos que un numero primo es aquel que es divisible entre 1 y entre sí mismo. Ahora bien, el usuario pide un numero input() => numero, se crea un intervalo o rango (1, numero + 1) matematicamente un intervalo cerrado [1; numero], si encontrásemos algun otro divisor en el intervalo  cerrado [1; numero] el código arroja False y se imprime Que no es primo. Por otro lado, si en este mismo intervalo no se cumple la condicion numero % 1 == 0 el contador es True y se imprime Que sí es primo.
"""
def esPrimo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False
def run():
    numero = int(input('Escribe un numero: '))
    if esPrimo(numero): #if esPrimo(numero) == True: => se pude obviar == True
        print("Es primo")
    else:
        print("No es primo")
#
if __name__ == '__main__':
    run()
