documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def show_people():
    """Выводим имя человека, которому принадлежит номер документа"""
    number_doc = input('Введите номер документа: ')
    for elements in documents:
        if number_doc == elements['number']:
            print(elements['name'])
            return


def show_shelf():
    """Выводим номер полки, на которой лежит номер документа"""
    number_doc = input('Введите номер документа: ')
    for directory in directories.items():
        for values in directory[1]:
            if number_doc == values:
                print(f'Документ находится на полке {directory[0]}')
                return
    print('Такого документа нет')


def show_list():
    """Выводим список всех документов"""
    print('Информация обо всех документах:')
    for document in documents:
        print('{}, "{}", "{}"'.format(document['type'], document['number'], document['name']))


def show_add():
    number_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    person = input('Введите имя владельца: ')
    number_shelf = input('Введите номер полки (от 1 до 3), на которой будет храниться документ: ')
    if number_shelf not in directories:
        print('Такой полки не существует')
    else:
        directories[number_shelf].append(number_doc)
        documents.append({'type': type_doc, 'number': number_doc, 'name': person})
        return


def main(documents):
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            show_people()
        elif command == 's':
            show_shelf()
        elif command == 'l':
            show_list()
        elif command == 'a':
            show_add()
        else:
            print('Команда неизвестна')
            break
    return


main(documents)
