def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Ingresa un número positivo")
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as err:
        print(err)


def run():
    try:
        num = int(input("Ingresa un número: "))
        result = divisors(num)
        if result is not None:
            print("Los divisores de {} son: {}".format(num, result))
    except ValueError as ve:
        print("Se debe ingresar un número")
    finally:
        print("----------- Fin del programa -----------")


if __name__ == '__main__':
    run()
