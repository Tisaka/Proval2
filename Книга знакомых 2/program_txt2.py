'''from add2 import add_everything2 as ae2

def everything_program():
    with open('file.cvs', 'a') as file:
        file.write(f'{ae2()}\n')
    return'''

import add2 as ad2
import logger2 as log

def telefon_view(sensor):
    data = ad2.add_telefon((sensor))
    log.telefon_logger((data))
    return data

def person_view(sensor):
    data = ad2.add_person((sensor))
    log.person_logger((data))
    return data

def status_view(sensor):
    data = ad2.add_status((sensor))
    log.status_logger((data))
    return data

def birthday_view(sensor):
    data = ad2.add_birthday((sensor))
    log.birthday_logger((data))
    return data

def everything_view(sensor):
    return print(f'{telefon_view(sensor)}'), print(f'{person_view(sensor)}'), print(f'{status_view(sensor)}'), print(f'{birthday_view(sensor)}')