import functions_for_book as func
from pprint import pprint


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
            print(func.add_contact())

        elif my_response == '2':
            print('-' * 30)
            pprint(func.show_book())
            print('-' * 30)

        elif my_response == '3':
            print(func.del_contact())

        elif my_response == '4':
            pprint(func.find_contact())
        
        elif my_response == '0':
            print('-' * 30)
            print('Хорошего дня!')
            print('-' * 30)

        else:
            print('-' * 30)
            print('Такой команды нет.')
            print('-' * 30)
            


if __name__ == '__main__':
    main()