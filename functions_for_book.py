import sqlite3 as sq
from pprint import pprint

name_db = 'phone_book.db'

def create_db():

    with sq.connect(name_db) as phone_book:
        cursor = phone_book.cursor()

        query = ('''
                CREATE TABLE IF NOT EXISTS контакты
                (
                    id_contact INTEGER PRIMARY KEY,
                    фамилия TEXT,
                    имя TEXT NOT NULL,
                    отчество TEXT
                );

                CREATE TABLE IF NOT EXISTS номера
                (
                    id_number INTEGER PRIMARY KEY,
                    номер TEXT,
                    домашний TEXT,
                    рабочий TEXT,
                    FOREIGN KEY (id_number) REFERENCES контакты (id_contact) ON DELETE CASCADE
                );
                ''')

        cursor.executescript(query)
    
    result = '\nТелефонная книга готова к использованию.'

    return result


def add_contact():

    min_simbols = 1
    surname = input('Фамилия --> ')

    name = input('Имя --> ')
    while len(name) < min_simbols:
        print('Это поле не может быть пустым.')
        name = input('Имя --> ')

    father_name = input('Отчество --> ')

    number = input('Номер телефона --> ')
    while number[0] != '+' and number[0] != '8':
        print('Формат номера должен быть "+7..." или "8..."')
        number = input('Номер телефона --> ')

    home_number = input('Домашний номер --> ')
    work_number = input('Рабочий номер --> ')

    values_for_contacts = [surname, name, father_name]
    values_for_numbers = [number, home_number, work_number]

    try:
        phone_book = sq.connect(name_db)
        cursor = phone_book.cursor()

        cursor.execute('INSERT INTO контакты(фамилия, имя, отчество) VALUES (?, ?, ?);', values_for_contacts)
        cursor.execute('INSERT INTO номера (номер, домашний, рабочий) VALUES (?, ?, ?);', values_for_numbers)

        phone_book.commit()
    except sq.Error as e:
        print('ERROR: ', e)
    finally:
        cursor.close()
        phone_book.close()
    
    result = '\nКонтакт добавлен.'

    return result


def show_book():

    try:
        phone_book = sq.connect(name_db)
        cursor = phone_book.cursor()

        cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий 
                          FROM контакты 
                          JOIN номера ON контакты.id_contact = номера.id_number;
                          ''')
        
        tables = cursor.fetchall()
    except sq.Error as e:
        print('ERROR: ', e)
    finally:
        cursor.close()
        phone_book.close()

    return tables


def del_contact():

    name = input('Имя контакта для удаления контакта --> ')
    names_for_del = [name]
    
    try:
        phone_book = sq.connect(name_db)
        cursor = phone_book.cursor()

        cursor.execute('''SELECT id_contact, фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий 
                          FROM контакты JOIN номера ON контакты.id_contact = номера.id_number 
                          WHERE имя = ?;''', names_for_del)
        
        pprint(cursor.fetchall())

        select_id = int(input('Выбери ID контакта для удаления --> '))
        id_for_del = [select_id]
        cursor.execute('PRAGMA foreign_keys=on')
        cursor.execute('DELETE FROM контакты WHERE id_contact = ?', id_for_del)

        phone_book.commit()
    except sq.Error as e:
        print('ERROR: ', e)
    finally:
        cursor.close()
        phone_book.close()
    
    result = '\nКонтакт удален.'

    return result


def find_contact():

    print('''
    Где искать контакт?
    1 - Фамилия
    2 - Имя
    3 - Отчество
    4 - Основной номер
    5 - Домашний номер
    6 - Рабочий
    0 - Отмена''')

    my_response = input('--> ')

    if my_response == '1':
        surname = input('Фамилия или часть фамилии контакта --> ')
        value_for_find = ['%' + surname + '%']
        try:
            phone_book = sq.connect(name_db)
            cursor = phone_book.cursor()
            cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий
                              FROM контакты
                              JOIN номера ON контакты.id_contact = номера.id_number
                              WHERE фамилия LIKE ?
                              ''', value_for_find)
            contacts = cursor.fetchall()
        except sq.Error as e:
            print('ERROR: ', e)
        finally:
            cursor.close()
            phone_book.close()        
        return contacts

    elif my_response == '2':
        name = input('Имя или часть имени контакта --> ')
        value_for_find = ['%' + name + '%']
        try:
            phone_book = sq.connect(name_db)
            cursor = phone_book.cursor()
            cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий
                              FROM контакты
                              JOIN номера ON контакты.id_contact = номера.id_number
                              WHERE имя LIKE ?
                              ''', value_for_find)            
            contacts = cursor.fetchall()
        except sq.Error as e:
            print('ERROR: ', e)
        finally:
            cursor.close()
            phone_book.close()
        return contacts
    
    elif my_response == '3':
        father_name = input('Отчество или часть отчества контакта --> ')
        value_for_find = ['%' + father_name + '%']
        try:
            phone_book = sq.connect(name_db)
            cursor = phone_book.cursor()
            cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий
                              FROM контакты
                              JOIN номера ON контакты.id_contact = номера.id_number
                              WHERE отчество LIKE ?
                              ''', value_for_find)
            
            contacts = cursor.fetchall()
        except sq.Error as e:
            print('ERROR: ', e)
        finally:
            cursor.close()
            phone_book.close()
        return contacts
    
    elif my_response == '4':
        number = input('Номер или часть номера контакта --> ')
        value_for_find = ['%' + number + '%']
        try:
            phone_book = sq.connect(name_db)
            cursor = phone_book.cursor()
            cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий
                              FROM контакты
                              JOIN номера ON контакты.id_contact = номера.id_number
                              WHERE номер LIKE ?
                              ''', value_for_find)
            contacts = cursor.fetchall()
        except sq.Error as e:
            print('ERROR: ', e)
        finally:
            cursor.close()
            phone_book.close()
        return contacts

    elif my_response == '5':
        home_number = input('Домашний номер или часть домашнего номера контакта --> ')
        value_for_find = ['%' + home_number + '%']
        try:
            phone_book = sq.connect(name_db)
            cursor = phone_book.cursor()

            cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий
                              FROM контакты
                              JOIN номера ON контакты.id_contact = номера.id_number
                              WHERE домашний LIKE ?
                              ''', value_for_find)
            
            contacts = cursor.fetchall()
        except sq.Error as e:
            print('ERROR: ', e)
        finally:
            cursor.close()
            phone_book.close()
        return contacts
 
    elif my_response == '6':
        work_number = input('Рабочий номер или часть рабочего номера контакта --> ')
        value_for_find = ['%' + work_number + '%']
        try:
            phone_book = sq.connect(name_db)
            cursor = phone_book.cursor()

            cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий
                              FROM контакты
                              JOIN номера ON контакты.id_contact = номера.id_number
                              WHERE рабочий LIKE ?
                              ''', value_for_find)
            
            contacts = cursor.fetchall()
        except sq.Error as e:
            print('ERROR: ', e)
        finally:
            cursor.close()
            phone_book.close()
        return contacts
        
    elif my_response == '0':
        result = 'Отмена'
        return result
    
    else:
        print('Такой команды нет.')
        find_contact()