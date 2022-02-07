def run():
    #squares = [i for i in range(1, 101) if i % 4 == 0]
    #squares = []
    # for i in range(1, 101):
    #    if i % 3 != 0:
    #        squares.append(i ** 2)
    #squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(type(squares))
    # print(squares)

    # Reto del video
    # crear, con un list comprehension, una lista de todos los múltiplos de 4 que a la vez sean también múltiplos
    # de 6 y 9, hasta 5 dígitos
    list_c = [i for i in range(1, 100000) if i % 36 == 0]
    print(list_c)


if __name__ == '__main__':
    run()
