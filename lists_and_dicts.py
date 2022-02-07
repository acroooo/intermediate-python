def run():
    my_list = [1, 'Hi', True, 4.5]
    my_dict = {
        "first_name": "Hernan",
        "last_name": "Chamorro",
    }

    super_list = [
        { "first_name": "Hernan", "last_name": "Chamorro",},
        { "first_name": "Gustavo", "last_name": "Ramon",},
        { "first_name": "Bruno", "last_name": "Facundo",},
        { "first_name": "Geronimo", "last_name": "Atahualpa",},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "integer_nums": [-2, -1, 0, 1, 2, 3, 4, 5,],
        "floating_nums": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for dict in super_list:
        print(dict['first_name'], "-", dict['last_name'])

if __name__ == '__main__':
    run()