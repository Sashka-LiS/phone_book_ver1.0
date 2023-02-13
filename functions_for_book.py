import sqlite3 as sq


name_db = 'Телефонная кнга.db'

def create_db():

    with sq.connect(name_db) as phone_book:
        cursor = phone_book.cursor()

        query = ('''
                PRAGMA foreign_keys=on;
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
                )''')

        cursor.executescript(query)


def add_contact():

    min_simbols = 1
    print('-' * 20)
    surname = input('Фамилия --> ')
    name = input('Имя --> ')
    if name == '':
        while len(name) < min_simbols:
            print('Это поле не может быть пустым.')
            name = input('Имя --> ')
    father_name = input('Отчество --> ')

    number = input('Номер телефона --> ')
    home_number = input('Домашний номер --> ')
    work_number = input('Рабочий номер --> ')
    print('-' * 20)

    values_for_contacts = [surname, name, father_name]
    values_for_numbers = [number, home_number, work_number]

    try:
        phone_book = sq.connect(name_db)
        cursor = phone_book.cursor()

        cursor.execute('INSERT INTO контакты(фамилия, имя, отчество) VALUES (?, ?, ?)', values_for_contacts)
        cursor.execute('INSERT INTO номера (номер, домашний, рабочий) VALUES (?, ?, ?)', values_for_numbers)

        phone_book.commit()
    except sq.Error as e:
        print('ERROR: ', e)
    finally:
        cursor.close()
        phone_book.close()


def show_book():
    try:
        phone_book = sq.connect(name_db)
        cursor = phone_book.cursor()

        cursor.execute('''SELECT фамилия, имя, отчество, номера.номер, номера.домашний, номера.рабочий 
                          FROM контакты 
                          JOIN номера ON контакты.id_contact = номера.id_number
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
                          WHERE имя = ?''', names_for_del)
        
        print(cursor.fetchall())

        select_id = int(input('Выбери ID контакта для удаления --> '))
        id_for_del = [select_id]
        cursor.execute('DELETE FROM контакты WHERE id_contact = ?', id_for_del)

        phone_book.commit()
    except sq.Error as e:
        print('ERROR: ', e)
    finally:
        cursor.close()
        phone_book.close()
