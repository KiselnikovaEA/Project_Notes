def choose_mode():
    mode = input('Выберите действие:\n1 - Создать\n2 - Посмотреть\n3 - Редактировать\n4 - Удалить\n5 - Обновить список\nq - выход\n')
    return mode

def hello_message():
    print('Добро пожаловать!')

def entry_inp():
    entry = [input('Заголовок: '), input('Текст: ')]
    return entry

def note_created_message():
    print('Запись создана')

def choose_note():
    note_id = input('Введите id заметки: ')
    return note_id

def no_id_message():
    print('Такого id не существует')

def end_message():
    print('Работа завершена')

def error_message():
    print('Ошибка')

def deleted_message():
    print('Запись удалена')
