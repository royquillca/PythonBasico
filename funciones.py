# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Esty aprendiendo a usar funciones: ")

# imprimir_mensaje() #Invocando una función
# imprimir_mensaje() #Invocando la funcion por segunda vez
# imprimir_mensaje() # Invocando la funcion por tercera vez

## SIN USAR FUNCIONES

# opcion = int(input("Elige una opcion (1, 2, 3):"))

# if opcion == 1:
#     print("Hola")
#     print("Como estas")
#     print("Elegiste la opción 2")
#     print("Adiós")
# elif opcion == 2:
#     print("Hola")
#     print("Como estas")
#     print("Elegiste la opción 2")
#     print("Adiós")
# elif opcion == 3:
#     print("Hola")
#     print("Como estas")
#     print("Elegiste la opción")
#     print("Adiós")
# else:
#     print("Escribe la opcion correcta")


## OPCION CORREGIDA USANDO FUNCIONES

opcion = int(input("Elige una opcion (1, 2, 3):"))
def conversacion(mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Adiós")
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")    
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("Elige una opcion correcta")

