import functions_for_book_2 as func
from pprint import pprint


main_menu = '''\n________МЕНЮ________
1 - Добавить контакт
2 - Показать телефонную книгу
3 - Удалить контакт
4 - Найти контакт
5 - Редактировать контакт
0 - Выход'''

search_menu = '''\nВ каком столбе искать контакт?
1 - Фамилия
2 - Имя
3 - Отчество
4 - Email
5 - Номер
6 - Домашний номер
7 - Рабочий номер
0 - Отмена'''

edit_menu = '''\nКакое поле контакта отредактировать?
1 - Фамилия
2 - Имя
3 - Отчество
4 - Email
5 - Номер
6 - Домашний номер
7 - Рабочий номер
0 - Отмена'''


def main():
    func.create_db()
    flag = True
    while flag:
        main_response = func.get_response(main_menu)
        if main_response == "0":
            func.exit()
            flag = False

        elif main_response == "1":
            val_tabl_contacts = func.get_val_for_contacts()
            if val_tabl_contacts == "0":
                print("\nКонтакт не добавлен.")
                continue
            val_tabl_numbers = func.get_val_for_numbers()
            if val_tabl_numbers == "0":
                print("\nКонтакт не добавлен.")
                continue
            func.add_contact_mode(val_tabl_contacts, val_tabl_numbers)
            print("\nКонтакт добавлен.")
            
        elif main_response == "2":
            print("*" * 100)
            pprint(func.show_book())
            print("*" * 100)

        elif main_response == "3":
            names_for_del = func.search_by_name()
            if names_for_del == "0":
                continue
            if not names_for_del:
                print("\nКонтакт не найден.")
                continue
            else:
                print("*" * 100)
                pprint(names_for_del)
                print("*" * 100)
            id_for_del = func.get_id_contact()
            if id_for_del == 0:
                print("\nКонтакт не удален.")
                continue
            if not func.is_valid_id(id_for_del, names_for_del):
                print("\nID нет в списке. Контакт не удален.")
                continue
            func.del_contact(id_for_del)
            print("\nКонтакт удален.")

        elif main_response == "4":
            search_flag = True
            while search_flag:
                search_response = func.get_response(search_menu)
                if search_response == "0":
                    search_flag = False

                elif search_response == "1":
                    found_surnames = func.search_by_surname()
                    if found_surnames == "0":
                        continue
                    if not found_surnames:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_surnames)
                        print("*" * 100)

                elif search_response == "2":
                    found_names = func.search_by_name()
                    if found_names == "0":
                        continue
                    if not found_names:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_names)
                        print("*" * 100)

                elif search_response == "3":
                    found_father_names = func.search_by_father_name()
                    if found_father_names == "0":
                        continue
                    if not found_father_names:
                        print('\nКонтакт не найден.')
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_father_names)
                        print("*" * 100)

                elif search_response == "4":
                    found_emails = func.search_by_email()
                    if found_emails == "0":
                        continue
                    if not found_emails:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_emails)
                        print("*" * 100)

                elif search_response == "5":
                    found_numbers = func.search_by_number()
                    if found_numbers == "0":
                        continue
                    if not found_numbers:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_numbers)
                        print("*" * 100)
                
                elif search_response == "6":
                    found_home_numbers = func.serach_by_home_number()
                    if found_home_numbers == "0":
                        continue
                    if not found_home_numbers:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_home_numbers)
                        print("*" * 100)
                
                elif search_response == "7":
                    found_work_numbers = func.search_by_work_number()
                    if found_work_numbers == "0":
                        continue
                    if not found_work_numbers:
                        print("\nКонтакт не найден.")
                    else:
                        print()
                        print("*" * 100)
                        pprint(found_work_numbers)
                        print("*" * 100)
                
                else:
                    print("\nНет такой команды.")
        
        elif main_response == "5":
            names_for_editing = func.search_by_name()
            if names_for_editing == "0":
                continue
            else:
                print("*" * 100)
                pprint(names_for_editing)
                print("*" * 100)
            id_for_edit = func.get_id_contact()
            if id_for_edit == 0:
                continue
            if not func.is_valid_id(id_for_edit, names_for_editing):
                print("\nID нет в списке. Контакт не отредактирован.")
                continue
            edit_flag = True
            while edit_flag:
                edit_response = func.get_response(edit_menu)
                if edit_response == "0":
                    edit_flag = False
                
                elif edit_response == "1":
                    new_surname = func.get_new_surname()
                    if new_surname == "0":
                        continue
                    func.edit_surname(new_surname, id_for_edit) 
                    print("\nКонтакт отредактирован.")
                
                elif edit_response == "2":
                    new_name = func.get_new_name()
                    while not func.is_valid_name(new_name):
                        print("Это поля не может быть пустым.")
                        new_name = func.get_new_name()
                    if new_name == "0":
                        continue
                    func.edit_name(new_name, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "3":
                    new_father_name = func.get_new_father_name()
                    if new_father_name == "0":
                        continue
                    func.edit_father_name(new_father_name, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "4":
                    new_email = func.get_new_email()
                    if func.the_same_email(new_email, id_for_edit):
                        print("\nКонтакт отредактирован.")
                        continue
                    while not func.is_valid_email(new_email):
                        print("Такой email уже есть в телефонной книге.")
                        new_email = func.get_new_email()
                    if new_email == "0":
                        continue
                    func.edit_email(new_email, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "5":
                    new_number = func.get_new_number()
                    if new_number == "0":
                        continue
                    while not func.is_valid_number(new_number):
                        print("Формат номера должен быть +7... или 8...")
                        new_number = func.get_new_number()
                        if new_number == "0":
                            break
                    func.edit_number(new_number, id_for_edit)
                    print("\nКонтакт отредактирован.")

                elif edit_response == "6":
                    new_home_number = func.get_new_home_number()
                    if new_home_number == "0":
                        continue
                    func.edit_home_number(new_home_number, id_for_edit)
                    print("\nКонтакт отредактирован.")
                
                elif edit_response == "7":
                    new_work_number = func.get_new_work_number()
                    if new_work_number == "0":
                        continue
                    func.edit_work_number(new_work_number, id_for_edit)
                    print("\nКонтакт отредактирован.")
                
                else:
                    print("\nНет такой команды.")

        else:
            print("\nНет такой команды.")
    print('\nХорошего дня!')

if __name__ == "__main__":
    main()