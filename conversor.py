# pesos = input("Cuantos pesos Colombianos tienes: ")
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos/valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dólares")

# RETO

# soles = float(input("Ingresa la cantidad de soles que tienes: "))
# valor_dolar_sol= 4.09
# dolar_sol = soles / valor_dolar_sol
# print("Tu dinero en soles equivale a ${} dolares".format(round(dolar_sol,3)))

menu = """
Bienvenido al conversor de monedas 🧸

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
Elige una opcion: """

opcion = int(input(menu))
if opcion == 1:
    pesos = input("Cuantos pesos Colombianos tienes: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    # dolares = str(dolares)
    print("Tienes ${} dólares".format(dolares))
    pass
elif opcion == 2:
    pesos = input("Cuantos pesos Argentinos tienes: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    pass
elif opcion == 3:
    pesos = input("Cuantos pesos Mexicanos tienes: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
    pass    
else:
    print("Escribe una opcion correcta Por favor")