import functions_for_book as func

def main():
    my_response = None

    func.create_db()

    while my_response != '0':
        print('''\n1 - Добавить контакт
2 - Показать телефонную книгу
3 - Удалить контакт
0 - Выход''')
        
        my_response = input('--> ')

        if my_response == '1':
            func.add_contact()
        elif my_response == '2':
            print('-' * 20)
            print(func.show_book())
            print('-' * 20)
        elif my_response == '3':
            func.del_contact()



if __name__ == '__main__':
    main()