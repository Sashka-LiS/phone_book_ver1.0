import functions_for_book as func
from functions_for_book import GOOD_STR, WARNING_STR, INPUT_STR


def main():
    my_response = None

    print(func.create_db())

    while my_response != '0':
        print('''\n1 - Добавить контакт
2 - Показать телефонную книгу
3 - Удалить контакт
4 - Найти контакт
5 - Редактировать контакт
0 - Выход''')
        
        my_response = input(INPUT_STR + '--> ')

        if my_response == '1':
            surname = input(INPUT_STR + 'Фамилия --> ').title()
            name = input(INPUT_STR + 'Имя --> ').title()
            while not func.is_valid_name(name):
                print(WARNING_STR + 'Это поле не может быть пустым.')
                name = input(INPUT_STR + 'Имя --> ')

            father_name = input(INPUT_STR + 'Отчество --> ').title()
            email = input(INPUT_STR + 'Email --> ')
            while not func.is_valid_email(email):
                print(WARNING_STR + 'Такой email уже есть в телефонной книге.')
                email = input(INPUT_STR + 'Email --> ')

            number = input(INPUT_STR + 'Номер телефона --> ')
            while not func.is_valid_number(number):
                print(WARNING_STR + 'Формат номера должен быть "+7..." или "8..."')
                number = input(INPUT_STR + 'Номер телефона --> ')

            home_number = input(INPUT_STR + 'Домашний номер --> ')
            work_number = input(INPUT_STR + 'Рабочий номер --> ')

            values_contacts = [surname, name, father_name, email]
            values_numbers = [number, home_number, work_number]

            func.add_contact(values_contacts, values_numbers)

            print(GOOD_STR + '\nКонтакт добавлен.')

        elif my_response == '2':
            func.show_book()

        elif my_response == '3':
            names_del = input(INPUT_STR + 'Имя контакта --> ').title()
            while not func.is_valid_value(names_del):
                print(WARNING_STR + 'Поле не может быть пустым.')
                names_del = input(INPUT_STR + 'Имя контакта --> ').title()

            func.del_contact([names_del])

            print(GOOD_STR + '\nКонтакт удален.')

        elif my_response == '4':
            response_finde = None
            while response_finde != '0':
                print('''Где искать контакт?
1 - Фамилия
2 - Имя
3 - Отчество
4 - Email
5 - Основной номер
6 - Домашний номер
7 - Рабочий
0 - Отмена''')
                response_finde = input(INPUT_STR + ' --> ')
                if response_finde == '1':
                    surname = input(INPUT_STR + 'Фамилия контакта --> ').title()
                    while not func.is_valid_value(surname):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        surname = input(INPUT_STR + 'Фамилия контакта --> ').title()
                    func.search_by_surname(surname)
            
                elif response_finde == '2':
                    name = input(INPUT_STR + 'Имя контакта --> ').title()
                    while not func.is_valid_value(name):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        name = input(INPUT_STR + 'Имя контакта --> ').title()
                    func.search_by_name(name)
            
                elif response_finde == '3':
                    father_name = input(INPUT_STR + 'Отчество контакта --> ').title()
                    while not func.is_valid_value(father_name):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        father_name = input(INPUT_STR + 'Отчество контакта --> ').title()
                    func.search_by_father_name(father_name)

                elif response_finde == '4':
                    email = input(INPUT_STR + 'Email контакта --> ')
                    while not func.is_valid_value(email):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        email = input(INPUT_STR + 'Email контакта --> ')
                    func.search_by_email(email)
                        

                elif response_finde == '5':
                    number = input(INPUT_STR + 'Номер контакта --> ')
                    while not func.is_valid_value(number):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        number = input(INPUT_STR + 'Номер контакта --> ')
                    func.search_by_number(number)
            
                elif response_finde == '6':
                    home_number = input(INPUT_STR + 'Номер контакта --> ')
                    while not func.is_valid_value(home_number):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        home_number = input(INPUT_STR + 'Номер контакта --> ')
                    func.search_by_home_number(home_number)
            
                elif response_finde == '7':
                    work_number = input(INPUT_STR + 'Номер контакта --> ')
                    while not func.is_valid_value(work_number):
                        print(WARNING_STR + 'Поле не может быть пустым.')
                        work_number = input(INPUT_STR + 'Номер контакта --> ')
                    func.search_by_work_number(work_number)

        elif my_response == '5':
            colomn_for_update = None
            name = input(INPUT_STR + 'Имя контакта --> ').title()
            while not func.is_valid_name(name):
                print(WARNING_STR + 'Это поле не может быть пустым.')
                name = input(INPUT_STR + 'Имя контакта --> ')
            func.search_by_name(name)
            id_for_update = int(input(INPUT_STR + 'ID контаткта --> ')) # ЕСЛИ НИЧЕГО НЕ ВВОДИТЬ
            while colomn_for_update != '0':
                print('''\nДанные для редактирования:
                1 - Фамилия
                2 - Имя
                3 - Отчество
                4 - Email
                5 - Номер
                6 - Домашний номер
                7 - Рабочий номер
                0 - Отмена''')
                colomn_for_update = input(INPUT_STR + ' --> ')
                
                if colomn_for_update == '1':
                    new_surname = input(INPUT_STR + 'Новая фамилия --> ').title()
                    func.update_surname(new_surname, id_for_update)
                
                elif colomn_for_update == '2':
                    new_name = input(INPUT_STR + 'Новое имя --> ').title()
                    while not func.is_valid_name(new_name):
                        print(WARNING_STR + 'Это поле не может быть пустым.')
                        new_name = input(INPUT_STR + 'Новое имя --> ').title()
                    func.update_name(new_name, id_for_update)

                elif colomn_for_update == '3':
                    new_father_name = input(INPUT_STR + 'Новое отчество --> ').title()
                    func.update_father_name(new_father_name, id_for_update)
                
                elif colomn_for_update == '4': # ЕСЛИ ВВЕСТИ ТАКОЙ ЖЕ ИМЭИЛ ЧТО И БЫЛ
                    new_email = input(INPUT_STR + 'Новый email --> ')
                    while not func.is_valid_email(new_email):
                        print(WARNING_STR + 'Такой email уже есть в телефонной книге.')
                        new_email = input(INPUT_STR + 'Новый email --> ')
                    func.update_email(new_email, id_for_update)
                
                elif colomn_for_update == '5':
                    new_number = input(INPUT_STR + 'Новый номер --> ')
                    while not func.is_valid_number(new_number):
                        print(WARNING_STR + 'Формат номера должен быть "+7..." или "8..."')
                        number = input(INPUT_STR + 'Новый номер --> ')
                    func.update_number(new_number, id_for_update)

                elif colomn_for_update == '6':
                    new_home_number = input(INPUT_STR + 'Новый домашний номер --> ')
                    func.update_home_number(new_home_number, id_for_update)
                
                elif colomn_for_update == '7':
                    new_work_number = input(INPUT_STR + 'Новый рабочий номер --> ')
                    func.update_work_number(new_work_number, id_for_update)





    func.exit()
    print(GOOD_STR + '\nХорошего дня!')

        
if __name__ == '__main__':
    main()