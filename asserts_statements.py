def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número que además se encuentre dentro de los números enteros positivos"
    result = divisors(int(num))
    if result is not None:
        print("Los divisores de {} son: {}".format(num, result))
    print("finalizo el programa")


if __name__ == '__main__':
    run()
