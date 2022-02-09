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
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    result = divisors(int(num))
    if result is not None:
        print("Los divisores de {} son: {}".format(num, result))
    print("finalizo el programa")


if __name__ == '__main__':
    run()
