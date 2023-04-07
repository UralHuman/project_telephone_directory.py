from tabulate import tabulate

file_path = r"telephone_directory.txt"

def select_function():
    select = input(
        "Чтобы найти контакт введите - 1\n"
        "Чтобы посмотреть контакты введите - 2\n"
        "Чтобы добавить контакт введите - 3\n"
        "Чтобы редоктировать контакт введите - 4\n"
        "Чтобы удалить контакт введите - 5\n"
        ">>> "
    )
    if select == "1":
        find_contact()
    elif select == "2":
        print_contacts()
    elif select == "3":
        add_contact()
    elif select == "4":
        edit_contact()
    elif select == "5":
        delete_contact()
    else:
        print("Некорректный выбор.")

def add_contact():
    with open(file_path, "a") as f_man:
        for _ in range(1):
            f_man.writelines("\n" + input("Введите номер и ФИО: "))

def find_contact():
    find_kontakt = input("Введите имя искомого контакта: ")
    with open(file_path, "r") as f_man:
        for line in f_man:
            if find_kontakt.casefold() in line.casefold():
                print(line)

def edit_contact():
    find_kontakt = input('Введите полное название контактна для редактирования: ')
    new_kontakt = input('Введите корректировочные данные которые хотите сохранить: ')
    with open(file_path, 'r+') as f_man:
        lines = f_man.readlines()
        f_man.seek(0)
        found = False  # Флаг, чтобы отслеживать, был ли найден контакт для редактирования
        for line in lines:
            if find_kontakt.casefold() in line.casefold():
                f_man.write(new_kontakt + '\n')
                found = True
            else:
                f_man.write(line)
        f_man.truncate()
        if found:
            print('Контакт успешно отредактирован.')
        else:
            print('Контакт не найден.')

def delete_contact():
    contact_to_delete = input("Введите контакт для удаления: ")
    with open(file_path, "r") as f:
        lines = f.readlines()
    with open(file_path, "w") as f:
        for line in lines:
            if contact_to_delete.casefold() not in line.casefold():
                f.write(line)
    print("Контакт успешно удален.")

def print_contacts():
    with open(file_path, "r") as f:
        lines = f.readlines()
    contacts = [line.strip().split(",") for line in lines]
    headers = ["Тел.Номер\ Фамилия Имя Отчество"]
    print(tabulate(contacts, headers=headers, tablefmt="grid"))

select_function()
