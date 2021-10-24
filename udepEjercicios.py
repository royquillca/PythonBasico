def run():
    A = int(input('Ingrese el numero A: '))
    B = int(input('Ingrese el numero B: '))
    
    intervalo = list(range(A,B+1))
    print(intervalo)
    suma = 0
    for num in intervalo:
        if num % 3 == 0:
            print(num)
            num += 1
            sum = sum + num
        else:
            continue


if __name__ == '__main__':
    run()