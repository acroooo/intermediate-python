def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            numbers.append(int(line))


def write():
    pass


def run():
    pass


if __name__ == '__main__':
    run()
