# Все имена с заглавной буквы
# Проверка на ввод правильной команды от пользователя
# Ошибки при пустом вводе
# Ошибка при пустом значении для удаления контакта
# Один коннект. Минимум закрытий
import sqlite3 as sq
from pprint import pprint


db_name = 'phone_book.db'
# db_connection = None


def create_db():

    with sq.connect(db_name) as phone_book:
        cursor = phone_book.cursor()

        query = ('''
                CREATE TABLE IF NOT EXISTS контакты
                (
                    id_contact INTEGER PRIMARY KEY,
                    фамилия TEXT,
                    имя TEXT NOT NULL,
                    отчество TEXT,
                    Email TEXT
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


def get_db():
    db_connection = sq.connect(db_name)
    return db_connection


# def db_cursor(phone_book=get_db()):
#     cursor = phone_book.cursor()
#     return cursor


def execute_add_del(query, values, phone_book=get_db()):
    cursor = phone_book.cursor()
    cursor.execute(query, values)
    phone_book.commit()


def cursor_execute(query, values, phone_book=get_db()):
    cursor = phone_book.cursor()
    return cursor.execute(query, values)


def is_valid_email(email, phone_book=get_db()):
    if email == None or email == '':
        return True
    
    cursor = phone_book.cursor()

    exist_email = cursor.execute('SELECT email FROM контакты WHERE email LIKE ?', [email]).fetchone()
    return exist_email is None


def is_valid_name(name):
    if not name:
        return False
    return True


def is_valid_number(number):
    if number[0] != '+' and number[0] != '8':
            return False
    return True


def add_contact():

    try:
        surname = input('Фамилия --> ')
        name = input('Имя --> ')
        while not is_valid_name(name):
            print('Это поле не может быть пустым.')
            name = input('Имя --> ')

        father_name = input('Отчество --> ')
        email = input('Email --> ')
        while not is_valid_email(email):
            print('Такой email уже есть в телефонной книге. Попробуте еще раз.')
            email = input('Email --> ')

        number = input('Номер телефона --> ')
        while not is_valid_number(number):
            print('Формат номера должен быть "+7..." или "8..."')
            number = input('Номер телефона --> ')

        home_number = input('Домашний номер --> ')
        work_number = input('Рабочий номер --> ')

        values_for_contacts = [surname, name, father_name, email]
        values_for_numbers = [number, home_number, work_number]

        execute_add_del('INSERT INTO контакты(фамилия, имя, отчество, email) VALUES (?, ?, ?, ?);', values_for_contacts)
        execute_add_del('INSERT INTO номера (номер, домашний, рабочий) VALUES (?, ?, ?);', values_for_numbers)
    except sq.Error as e:
        print('ERROR: ', e)
    
    result = '\nКонтакт добавлен.'
    return result



def show_book():

    try:
        query = ('''SELECT фамилия, имя, отчество, email, номера.номер, номера.домашний, номера.рабочий 
                          FROM контакты 
                          JOIN номера ON контакты.id_contact = номера.id_number;
                          ''')  
        cursor = db_cursor(query)
        contacts = cursor.fetchall()    
    except sq.Error as e:
        print('ERROR: ', e)
    finally:
        cursor.close()
        

    return contacts


def del_contact():

    try:
        name = input('Имя контакта для удаления контакта --> ')
        names_for_del = [name]
        ('''SELECT id_contact, фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий 
                          FROM контакты JOIN номера ON контакты.id_contact = номера.id_number 
                          WHERE имя = ?;''', names_for_del)
        print('-' * 20)
        pprint(db_cursor().fetchall()) #!!!!!!!!!!
        print('-' * 20)
        select_id = int(input('Выбери ID контакта для удаления --> '))
        id_for_del = [select_id]
        execute_add_del('PRAGMA foreign_keys=on')
        execute_add_del('DELETE FROM контакты WHERE id_contact = ?', id_for_del)
    except sq.Error as e:
        print('ERROR: ', e)

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