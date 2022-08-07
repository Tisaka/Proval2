def add_telefon():
    telefon = int(input('Введите ваш телефон: '))
    return print(telefon)

def add_person():
    person = str(input('Введите ваше имя: '))
    return print(person)

def add_status():
    status = str(input('Введите ваш статус: '))
    return print(status)

def add_birthday():
    birthday = str(input('Введите вашу дату рождения: '))
    return print(birthday)

def add_everything():
    return print(f'{add_telefon}'), print(f'{add_person}'), print(f'{add_status}'), print(f'{add_birthday}')

def add_everything2():
    return print(f'Телефон: {add_telefon}'), print(f'Человек: {add_person}'), print(f'Статус: {add_status}'), print(f'День рождения: {add_birthday}')
