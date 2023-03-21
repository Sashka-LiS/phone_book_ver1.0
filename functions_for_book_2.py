import sqlite3 as sq
from pprint import pprint

DB_NAME = 'phone_book_2.db'


def create_db():
    """Создание БД"""
    with sq.connect(DB_NAME) as phone_book:
        cursor = phone_book.cursor()

        query = ('''
                CREATE TABLE IF NOT EXISTS contacts
                (
                    id_contact INTEGER PRIMARY KEY,
                    surname TEXT,
                    name TEXT NOT NULL,
                    father_name TEXT,
                    email TEXT
                );

                CREATE TABLE IF NOT EXISTS numbers
                (
                    id_number INTEGER PRIMARY KEY,
                    number TEXT,
                    home_number TEXT,
                    work_number TEXT,
                    FOREIGN KEY (id_number) REFERENCES контакты (id_contact) ON DELETE CASCADE
                );
                ''')

        cursor.executescript(query)
        print("\nТелефонная книга готова к использованию.")
    return True

def get_db():
    """Возвращает контакт к БД"""
    connection_db = sq.connect(DB_NAME)
    return connection_db

def get_val_for_contacts(val_tabl_contacts=[]):
    """Возвращает значения для таблицы contacts"""
    surname = input("Фамилия (Для отмены нажми 0)--> ")
    if surname == "0":
        return surname
    val_tabl_contacts.append(surname)
    name = input("Имя (Для отмены нажми 0)--> ")
    if name == "0":
        return name
    while not is_valid_name(name):
        print("Это поля не может быть пустым.")
        name = input("Имя (Для отмены нажми 0)--> ")
        if name == "0":
            return name
    val_tabl_contacts.append(name)
    father_name = input("Отчество (Для отмены нажми 0)--> ")
    if father_name == "0":
        return father_name
    val_tabl_contacts.append(father_name)
    email = input("Email (Для отмены нажми 0)--> ")
    if email == "0":
        return email
    while not is_valid_email(email):
        print("Такой email уже есть в телефонной книге.")
        email = input("Email (Для отмены нажми 0)--> ")
        if email == "0":
            return email
    val_tabl_contacts.append(email)
    return val_tabl_contacts

def get_val_for_numbers(val_tabl_numbers=[]):
    """Возвращает значения для таблицы numbers"""
    number = input("Номер (Для отмены нажми 0)--> ")
    if number == "0":
        return number
    while not is_valid_number(number):
        print("Формат номера должен быть +7... или 8...")
        number = input("Номер (Для отмены нажми 0)--> ")
        if number == "0":
            return number
    val_tabl_numbers.append(number)
    home_number = input("Домашний номер (Для отмены нажми 0)--> ")
    if home_number == "0":
        return home_number
    val_tabl_numbers.append(home_number)
    work_number = input("Рабочий номер (Для отмены нажми 0)--> ")
    if work_number == "0":
        return work_number
    val_tabl_numbers.append(work_number)
    return val_tabl_numbers

def get_response(menu):
    '''Выводит меню и возвращает отклик'''
    print(menu)
    response = input('--> ')
    return response

def get_id_contact():
    """Возвращает ID контакта. Тип ID = integer"""
    id  = int(input("ID контакта (Для отмены нажми 0)--> "))
    return id

def is_valid_name(name):
    """Проверка имени на валидность"""
    if not name:
        return False
    return True

def is_valid_email(email, phone_book=get_db()):
    """Проверка email на дубликат в БД"""
    cursor = phone_book.cursor()
    if email == None or email == '':
        return True
    exist_email = cursor.execute("SELECT email FROM contacts WHERE email = ?", [email]).fetchone()
    cursor.close()
    return exist_email is None

def is_valid_number(number):
    """Проверяет правильность ввода номера"""
    if not number:
        return False
    if number[0:2] != '+7' and number[0] != '8':
        return False
    return True

def is_valid_id(id, list_contacts):
    '''Проверка на вхождение ID в список контактов для манипулиций'''
    list_id = []
    for contact in list_contacts:
        for value in contact:
            if type(value) == int:
                list_id.append(value)
    return id in list_id

def add_contact_mode(val_tabl_contacts, val_tabl_numbers, phone_book=get_db()):
    """Добавляет контакт в БД"""
    cursor = phone_book.cursor()
    cursor.execute("INSERT INTO contacts(surname, name, father_name, email) VALUES (?, ?, ?, ?);", val_tabl_contacts)
    cursor.execute("INSERT INTO numbers(number, home_number, work_number) VALUES (?, ?, ?);", val_tabl_numbers)
    phone_book.commit()
    cursor.close()
    return True

def exit(phone_book=get_db()):
    """Закрывает контакт к БД и за"""
    phone_book.close()
    return True

def show_book(phone_book=get_db()):
    """Возвращает всю БД со всеми контактами"""
    cursor = phone_book.cursor()
    all_book = cursor.execute('''SELECT id_contact, surname, name, father_name, email, numbers.number, numbers.home_number, numbers.work_number 
                      FROM contacts 
                      JOIN numbers ON contacts.id_contact = numbers.id_number;''').fetchall()
    cursor.close()
    return all_book

def del_contact(id_for_del, phone_book=get_db()):
    """Удаляет запись из БД по ID"""

    cursor = phone_book.cursor()    
    cursor.execute("PRAGMA foreign_keys = on")
    cursor.execute("DELETE FROM contacts WHERE id_contact = ?", [id_for_del])
    phone_book.commit()
    cursor.close()
    return True

def search_by_surname(phone_book=get_db()):
    """Поиск по столбу surname в БД"""
    surname = input("Фамилия контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + surname + "%"]
    if surname == "0":
        return surname
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE surname LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result

def search_by_name(phone_book=get_db()):
    """Поис по столбу name в БД"""
    name = input("Имя контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + name + "%"]
    if name == "0":
        return name
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, father_name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE name LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result

def search_by_father_name(phone_book=get_db()):
    """Поис по столбу father_name в БД"""
    father_name = input("Отчество контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + father_name + "%"]
    if father_name == "0":
        return father_name
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE father_name LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result

def search_by_email(phone_book=get_db()):
    """Поис по столбу email в БД"""
    email = input("Email контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + email + "%"]
    if email == "0":
        return email
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE email LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result

def search_by_number(phone_book=get_db()):
    """Поиск по столбу number в БД"""
    number = input("Номер контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + number + "%"]
    if number == "0":
        return number
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE number LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result

def serach_by_home_number(phone_book=get_db()):
    """Поиск по столбу home_number в БД"""
    home_number = input("Домашний номер контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + home_number + "%"]
    if home_number == "0":
        return home_number
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE home_number LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result

def search_by_work_number(phone_book=get_db()):
    """Поиск по стоблу work_number в БД"""
    work_number = input("Рабочий номер контакта (Для отмены нажми 0)--> ")
    val_for_search = ["%" + work_number + "%"]
    if work_number == "0":
        return work_number
    cursor = phone_book.cursor()
    result = cursor.execute("""SELECT id_contact, surname, name, email, numbers.number, numbers.home_number, numbers.work_number
                               FROM contacts JOIN numbers ON contacts.id_contact = numbers.id_number
                               WHERE work_number LIKE ?;""", val_for_search).fetchall()
    cursor.close()
    return result
    
def get_new_surname():
    """Возвращает новую фамилия для редактирования контакта"""
    new_surname = input("Новая фамилия контакта (Для отмены нажми 0)--> ")
    return new_surname

def edit_surname(new_surname, id_for_edit, phone_book=get_db()):
    """Редактирует поле surname в БД"""
    values_for_edit = [new_surname, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE contacts SET surname = ? WHERE id_contact = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True

def get_new_name():
    """Возвращает новое имя для редактирования контакта"""
    new_name = input("Новое имя для контакта (Для отмены нажми 0)--> ")
    return new_name

def edit_name(new_name, id_for_edit, phone_book=get_db()):
    """Редактирует поле name в БД"""
    values_for_edit = [new_name, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE contacts SET name = ? WHERE id_contact = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True

def get_new_father_name():
    """Возвращает новое отчество для редактирования контакта"""
    new_father_name = input("Новое отчество контакта (Для отмены нажми 0)--> ")
    return new_father_name

def edit_father_name(new_father_name, id_for_edit, phone_book=get_db()):
    """Редактирует поле father_name в БД"""
    values_for_edit = [new_father_name, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE contacts SET father_name = ? WHERE id_contact = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True

def get_new_email():
    """Возвращает новый email для редактирования контакта"""
    new_email = input("Новый email контакта (Для отмены нажми 0)--> ")
    return new_email

def the_same_email(new_email, id_for_edit, phone_book=get_db()):
     """Сравнивает старый email с новым у одного контакта для корректного редактирования поля email в БД"""
     cursor = phone_book.cursor()
     old_email = cursor.execute('SELECT email FROM contacts WHERE id_contact = ?;', [id_for_edit]).fetchone()
     cursor.close()
     return new_email == old_email[0]

def edit_email(new_email, id_for_edit, phone_book=get_db()):
    """Редактирует поле email в БД"""
    values_for_edit = [new_email, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE contacts SET email = ? WHERE id_contact = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True

def get_new_number():
    """Возвращает новый номер тел. для редактирования контакта"""
    new_number = input("Новый номер контакта (Для отмены нажми 0)--> ")
    return new_number

def edit_number(new_number, id_for_edit, phone_book=get_db()):
    """Редактирует поле number в БД"""
    values_for_edit = [new_number, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE numbers SET number = ? WHERE id_number = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True

def get_new_home_number():
    """Возвращает новый домашний номер для редактирования"""
    new_home_number = input("Новый домашний номер контакта (Для отмены нажми 0)--> ")
    return new_home_number

def edit_home_number(new_home_number, id_for_edit, phone_book=get_db()):
    """Редактируе поле home_number в БД"""
    values_for_edit = [new_home_number, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE numbers SET home_number = ? WHERE id_number = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True

def get_new_work_number():
    """Возвращает новый рабочий номер для редактирования"""
    new_work_number = input("Новый рабочий номер контакта (Для отмены нажми 0)-->")
    return new_work_number

def edit_work_number(new_work_number, id_for_edit, phone_book=get_db()):
    """Редактирует поле work_number в БД"""
    values_for_edit = [new_work_number, id_for_edit]
    cursor = phone_book.cursor()
    cursor.execute("UPDATE numbers SET work_number = ? WHERE id_number = ?;", values_for_edit)
    phone_book.commit()
    cursor.close()
    return True