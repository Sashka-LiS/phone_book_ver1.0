import functions_for_book as func



def main():
    my_response = None

    print(func.create_db())

    while my_response != '0':
        print('''\n1 - Добавить контакт
2 - Показать телефонную книгу
3 - Удалить контакт
4 - Найти контакт
0 - Выход''')
        
        my_response = input('--> ')

        if my_response == '1':
            surname = input('Фамилия --> ')
            name = input('Имя --> ')
            while not func.is_valid_name(name):
                print('Это поле не может быть пустым.')
                name = input('Имя --> ')

            father_name = input('Отчество --> ')
            email = input('Email --> ')
            while not func.is_valid_email(email):
                print('Такой email уже есть в телефонной книге. Попробуте еще раз.')
                email = input('Email --> ')

            number = input('Номер телефона --> ')
            while not func.is_valid_number(number):
                print('Формат номера должен быть "+7..." или "8..."')
                number = input('Номер телефона --> ')

            home_number = input('Домашний номер --> ')
            work_number = input('Рабочий номер --> ')

            values_contacts = [surname, name, father_name, email]
            values_numbers = [number, home_number, work_number]

            func.add_contact(values_contacts, values_numbers)

            print('\nКонтакт добавлен.')

        elif my_response == '2':
            func.show_book()

        elif my_response == '3':
            names_del = input('Имя контакта --> ')
            
            func.del_contact([names_del])

            print('\nКонтакт удален.')

        elif my_response == '4':
            response_finde = None
            while response_finde != '0':
                print('''
Где искать контакт?
1 - Фамилия
2 - Имя
3 - Отчество
4 - Основной номер
5 - Домашний номер
6 - Рабочий
0 - Отмена''')
                response_finde = input(' --> ')
                if response_finde == '1':
                    surname = input('Фамилия контакта --> ')
                    while not func.is_valid_value(surname):
                        print('Поле не может быть пустым.')
                        surname = input('Фамилия контакта --> ')

                    func.search_by_surname(surname)
            
                elif response_finde == '2':
                    name = input('Имя контакта --> ')
                    while not func.is_valid_value(name):
                        print('Поле не может быть пустым.')
                        name = input('Имя контакта --> ')

                    func.search_by_name(name)
            
                elif response_finde == '3':
                    father_name = input('Отчество контакта --> ')
                    while not func.is_valid_value(father_name):
                        print('Поле не может быть пустым.')
                        father_name = input('Отчество контакта --> ')

                    func.search_by_father_name(father_name)

                elif response_finde == '4':
                    number = input('Номер контакта --> ')
                    while not func.is_valid_value(number):
                        print('Поле не может быть пустым.')
                        number = input('Номер контакта --> ')

                    func.search_by_number(number)
            
                elif response_finde == '5':
                    home_number = input('Номер контакта --> ')
                    while not func.is_valid_value(home_number):
                        print('Поле не может быть пустым.')
                        home_number = input('Номер контакта --> ')

                    func.search_by_home_number(home_number)
            
                elif response_finde == '6':
                    work_number = input('Номер контакта --> ')
                    while not func.is_valid_value(work_number):
                        print('Поле не может быть пустым.')
                        work_number = input('Номер контакта --> ')

                    func.search_by_work_number(work_number)

            


if __name__ == '__main__':
    main()