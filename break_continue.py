def run():
#
#
    # CASO CONITNUE : IMPRIME LOS NUMEROS PARES COMPRENDIDOS EN EL INTERVALO/ RANGO DE [0; 999]

    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # CASO BREAK : Imprime los numeros hasta que i sea igual a 5678 en el intervalo [0; 9 999]

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    #CASO PARA STR / CADEAS DE TEXTO

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    #RETO APLICADO A WHILE

    # contador = 0
    # par_2 = contador % 2
    # print(contador)
    # while par_2 == 0:
    #     contador += 1
    #     par_2 = contador % 2
    #     print(par_2)
    #     if par_2 != 0:
    #         break

    # CICLO IF ELSE
    # edad = int(input('¿Cuantos años tienes?'))
    # if  edad < 18:
    #     print('Es usted menor de edad')
    # else:
    #     print('Es usted mayor de edad')
    # print('¡Hasta la próxima!') # Esta fuera del ciclo if ... else
    
    #CON DOS CILO IF (IF ... IF) 
    
    edad = int(input('¿Cuantos años tienes? '))
    if edad < 18:
        print("Es usted menor de edad")
    if edad > 18:
        print("Es usted mayor de edad")
    print("¡Hasta la próxima!")
    
    """
    Es mejor no hacerlo así por dos motivos:

    - Al poner dos bloques if estamos obligando a Python a evaluar siempre las dos condiciones, mientras que en un bloque if ... else ... sólo se evalúa una condición. En un programa sencillo la diferencia no es apreciable, pero en programas que ejecutan muchas comparaciones, el impacto puede ser apreciable.
    - Utilizando else nos ahorramos escribir una condición (además, escribiendo la condición nos podemos equivocar, pero escribiendo else no).
    - Utilizando if ... else nos aseguramos de que se ejecuta uno de los dos bloques de instrucciones. Utilizando dos if cabría la posibilidad de que no se cumpliera ninguna de las dos condiciones y no se ejecutara ninguno de los dos bloques de instrucciones.
    
    """

    # edad = int(input("¿Cuántos años tiene? "))
    # if edad < 120:
    #     pass
    # else:
    #     print("¡No me lo creo!")
    # print(f"Usted dice que tiene {edad} años.")
    
    # edad = int(input("¿Cuántos años tiene? "))
    # if edad >= 120:
    #     print("¡No me lo creo!")
    # print(f"Usted dice que tiene {edad} años.")


if __name__  == '__main__':
    run()