def equality (recipient, sender):
    d = ()
    if recipient == sender:
        d = print(f'Нельзя отправить письмо самому себе!')
    else:
        if sender == 'university.help@gmail.com':
            d = print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        else:
            d = print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    return d

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    a = "@"
    mail = [recipient, sender]
    for j in range(0, 2):
        if a in mail[j]:
            b = [".com", ".ru", ".net"]
            for i in range(0, len(b)):
                if b[i] in mail[j]:
                    break
                else:
                    if i == 2:
                        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    equality (recipient, sender)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
