import sqlite3 as sq
from pprint import pprint
from colorama import init, Fore

# Во всех функциях поиска добавить столб id_contact
init(autoreset=True)

GOOD_STR = Fore.GREEN
WARNING_STR = Fore.YELLOW
INPUT_STR = Fore.BLUE

DB_NAME = 'phone_book.db'


def create_db():

    with sq.connect(DB_NAME) as phone_book:
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
    
    return GOOD_STR + '\nТелефонная книга готова к использованию.'


def get_db():
    db_connection = sq.connect(DB_NAME)
    return db_connection


def is_valid_email(email, phone_book=get_db()):
    cursor = phone_book.cursor()

    if email == None or email == '':
        return True
    exist_email = cursor.execute('SELECT email FROM контакты WHERE email LIKE ?', [email]).fetchone()
    cursor.close()
    return exist_email is None


def is_valid_name(name):
    if not name:
        return False
    return True


def is_valid_number(number):
    if not number:
         return False
    elif number[0] != '+' and number[0] != '8':
            return False
    return True


def is_valid_value(value):
     empty_string = ''
     if value == empty_string:
          return False
     return True


def add_contact(values_contacts, values_numbers, phone_book=get_db()):
        cursor = phone_book.cursor()
        cursor.execute('INSERT INTO контакты(фамилия, имя, отчество, email) VALUES (?, ?, ?, ?);', values_contacts)
        cursor.execute('INSERT INTO номера (номер, домашний, рабочий) VALUES (?, ?, ?);', values_numbers)
        phone_book.commit()
        cursor.close()
        return True


def show_book(phone_book=get_db()):
    cursor = phone_book.cursor()
    cursor.execute('''SELECT id_contact, фамилия, имя, отчество, email, номера.номер, номера.домашний, номера.рабочий 
                      FROM контакты 
                      JOIN номера ON контакты.id_contact = номера.id_number;
                      ''')
    print('*' * 80)
    pprint(cursor.fetchall())
    print('*' * 80)
    cursor.close()
    return True


def del_contact(names_del, phone_book=get_db()):
        cursor = phone_book.cursor()
        cursor.execute('''SELECT id_contact, фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий 
                          FROM контакты JOIN номера ON контакты.id_contact = номера.id_number 
                          WHERE имя = ?;''', names_del)
        
        print('*' * 80)
        pprint(cursor.fetchall())
        print('*' * 80)

        select_id = int(input(INPUT_STR + 'Выбери ID контакта для удаления --> '))
        id_for_del = [select_id]

        cursor.execute('PRAGMA foreign_keys=on')
        cursor.execute('DELETE FROM контакты WHERE id_contact = ?', id_for_del)
        phone_book.commit()
        cursor.close()
        return True


def search_by_surname(surname, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + surname + '%']
    cursor.execute('''SELECT фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                      FROM контакты
                      JOIN номера ON контакты.id_contact = номера.id_number
                      WHERE фамилия LIKE ?''', value_for_finde)

    print('*' * 80)
    pprint(cursor.fetchall())     
    print('*' * 80)
    cursor.close()
    return True


def search_by_name(name, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + name + '%']
    cursor.execute('''SELECT id_contact, фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                      FROM контакты
                      JOIN номера ON контакты.id_contact = номера.id_number
                      WHERE имя LIKE ?''', value_for_finde)

    print('*' * 80)
    pprint(cursor.fetchall())     
    print('*' * 80)
    cursor.close()
    return True


def search_by_father_name(father_name, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + father_name + '%']
    cursor.execute('''SELECT фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                      FROM контакты
                      JOIN номера ON контакты.id_contact = номера.id_number
                      WHERE отчество LIKE ?''', value_for_finde)

    print('*' * 80)
    pprint(cursor.fetchall())     
    print('*' * 80)
    cursor.close()
    return True


def search_by_email(email, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + email + '%']
    cursor.execute('''SELECT фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                     FROM контакты
                     JOIN номера ON контакты.id_contact = номера.id_number
                     WHERE email LIKE ?''', value_for_finde)
    
    print('*' * 80)
    pprint(cursor.fetchall())
    print('*' * 80)
    cursor.close()
    return True


def search_by_number(number, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + number + '%']
    cursor.execute('''SELECT фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                      FROM контакты
                      JOIN номера ON контакты.id_contact = номера.id_number
                      WHERE номер LIKE ?''', value_for_finde)

    print('*' * 80)
    pprint(cursor.fetchall())     
    print('*' * 80)
    cursor.close()
    return True


def search_by_home_number(home_number, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + home_number + '%']
    cursor.execute('''SELECT фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                      FROM контакты
                      JOIN номера ON контакты.id_contact = номера.id_number
                      WHERE домашний LIKE ?''', value_for_finde)

    print('*' * 80)
    pprint(cursor.fetchall())     
    print('*' * 80)
    cursor.close()
    return True


def search_by_work_number(work_number, phone_book=get_db()):
    cursor = phone_book.cursor()
    value_for_finde = ['%' + work_number + '%']
    cursor.execute('''SELECT фамилия, имя, отчество, Email, номера.номер, номера.домашний, номера.рабочий
                      FROM контакты
                      JOIN номера ON контакты.id_contact = номера.id_number
                      WHERE рабочий LIKE ?''', value_for_finde)

    print('*' * 80)
    pprint(cursor.fetchall())     
    print('*' * 80)
    cursor.close()
    return True


def exit(phone_book=get_db()):
    phone_book.close()
    return True


def update_surname(new_surname, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_surname, id_for_update]
    cursor.execute('UPDATE контакты SET фамилия = ? WHERE id_contact = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True
    

def update_name(new_name, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_name, id_for_update]
    cursor.execute('UPDATE контакты SET имя = ? WHERE id_contact = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True


def update_father_name(new_father_name, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_father_name, id_for_update]
    cursor.execute('UPDATE контакты SET отчество = ? WHERE id_contact = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True


def update_email(new_email, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_email, id_for_update]
    cursor.execute('UPDATE контакты SET email = ? WHERE id_contact = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True


def update_number(new_number, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_number, id_for_update]
    cursor.execute('UPDATE номера SET номер = ? WHERE id_number = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True


def update_home_number(new_home_number, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_home_number, id_for_update]
    cursor.execute('UPDATE номера SET домашний = ? WHERE id_number = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True


def update_work_number(new_work_number, id_for_update, phone_book=get_db()):
    cursor = phone_book.cursor()
    values_for_update = [new_work_number, id_for_update]
    cursor.execute('UPDATE номера SET рабочий = ? WHERE id_number = ?;', values_for_update)
    phone_book.commit()
    cursor.close()
    print(GOOD_STR + 'Контакт обновлен.')
    return True