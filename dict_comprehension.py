import math


def run():
    #my_dict = {}
    # for i in range(1, 101):
    #    my_dict[i] = i**3

    # con dict comprehension
    #my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    # Reto
    # crear, con un dict comprehension, un diccionario cuyas llaves sean los 1000 primeros numeros naturales
    #  con sus raices cuadradas como valores
    my_dict = {i: math.sqrt(i) for i in range(1, 1001)}
    print(my_dict)


if __name__ == '__main__':
    run()
