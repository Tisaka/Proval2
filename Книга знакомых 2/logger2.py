from datetime import datetime as dt

def telefon_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('\n{}:{}\n'
                   .format(time, data))

def person_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('\n{}:{}\n'
                   .format(time, data))

def status_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('\n{}:{}\n'
                   .format(time, data))

def birthday_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('\n{}:{}\n'
                   .format(time, data))