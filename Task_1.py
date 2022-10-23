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


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def search_name_people(number_of_document):
    print("---------------ПОИСК ПОЛЬЗОВАТЕЛЯ---------------")
    for people in documents:
        if people["number"] == number_of_document:
            return people["name"]
    return "Нет такого пользователя"


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
def search_number_of_folder(number_of_document):
    print("---------------ПОИСК В АРХИВЕ---------------")
    for number, numbers_of_doc in directories.items():
        if number_of_document in numbers_of_doc:
            return "Номер полки: " + number
    return "Нет такого пользоватля"


# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_documents():
    print("---------------ВЫВОД СПИСКА---------------")
    for doc in documents:
        print(f"{doc['type']} {doc['number']} {doc['name']}")
    for dict_doc, docs in directories.items():
        print(f"{dict_doc}: {docs}")


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер,
# тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию,
# когда пользователь будет пытаться добавить документ на несуществующую полку.
def add_to_documents(type_doc, number_of_document, name):
    print("-----ДОБАВЛЕНИЕ В СПИСОК ПОЛЬЗОВАТЕЛЕЙ-----")
    doc_list = sum([number for number in directories.values()], [])
    if number_of_document not in doc_list:
        documents.append({"type": type_doc, "number": number_of_document, "name": name})
    else:
        print("Такой документ уже существует")
        return
    print(f"Пользователь добавлен: {type_doc} {number_of_document} {name} в список")


def add_to_directories(number_of_document, number_of_dict):
    print("-----------ДОБАВЛЕНИЕ В АРХИВ-------------")
    if number_of_dict in list(directories.keys()):
        directories[number_of_dict] += [number_of_document]
        print(f"Пользователь добавлен на полку: {number_of_dict}")
        return True
    else:
        if number_of_dict not in directories.keys():
            directories.update({number_of_dict: [number_of_document]})
            print(f"Пользователь добавлен на новую полку: {number_of_dict}")
        else:
            print("Полка существует")
        return False


# d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога
# и его номер из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
def delete_from_documents(number_of_document):
    print("---------------УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ---------------")
    for doc in documents:
        if doc["number"] == number_of_document:
            documents.remove(doc)
            print(f"Пользователь с номером {number_of_document} удален из списка документов")
            break
    else:
        print("Номера отсутствует в списке пользователей")
        return False


# delete номера документа из полки
def delete_from_directories(number_of_document):
    print(f"-----------УДАЛЕНИЕ ИЗ ПОЛКИ------------")
    for numbers in directories.values():
        if number_of_document in numbers:
            numbers.remove(number_of_document)
            print(f"Пользователь с номером {number_of_document} удален из архива")
            return True
    else:
        print("Номер отсутствует на полках")
        return False


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
# Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
def add_shelf(number_of_shelf):
    print("--------------ДОБАВЛЕНИЕ ПОЛКИ---------------")
    if number_of_shelf not in directories.keys():
        directories.update({number_of_shelf: []})
    else:
        print("Полка существует")


# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить
# документ на несуществующую полку;
def move(number_of_document, number_of_shelf):
    print("---------------ПЕРЕМЕЩЕНИЕ---------------")
    if delete_from_directories(number_of_document):
        add_to_directories(number_of_document, number_of_shelf)


def main():
    run = True
    while run:
        command = input("Введите команду на англ.: ")
        if command.lower() == "p":
            print(search_name_people(input("Введте номер документа: ")))
        elif command.lower() == "s":
            print(search_number_of_folder(input("Введте номер документа: ")))
        elif command.lower() == "l":
            list_documents()
        elif command.lower() == "a":
            type_doc = input("Введите тип документа: ")
            number_of_document = input("Введите номер документа: ")
            name = input("Введите Имя и фамилию полностью: ")
            number_of_directories = input("Введите номер полки: ")
            add_to_documents(type_doc, number_of_document, name)
            add_to_directories(number_of_document, number_of_directories)
        elif command.lower() == "d":
            number_of_document = input("Введите номер удаляемого документа: ")
            delete_from_documents(number_of_document)
            delete_from_directories(number_of_document)
            list_documents()
        elif command.lower() == "m":
            number_of_document = input("Введите номер документа для переноса: ")
            number_of_directories = input("Введите номер новой полки: ")
            move(number_of_document, number_of_directories)
        elif command.lower() == "as":
            number_of_shelf = input("Введите номер доабвляемой полки: ")
            add_shelf(number_of_shelf)
        else:
            print("Код не найден, программа завершена")
            run = False


main()
