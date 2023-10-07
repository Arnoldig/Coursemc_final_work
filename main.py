"""   Условия задачи:
 + - создать два модуля Регистрация и Авторизация
 + - можо использовать любые библиотеки
 + - программа должна быть консольной

   Критерии хорошего решения (КХР):
 + - придерживаемся стандартов PEP8
 + - любые названия должны быть обоснованы
 + - программа должна быть написана на "функциях"
 + - должны быть тесты с защитой от основных ошибок

 Использование:
 + А) При старте спрашиваем что необходимо: авториазоваться или зарегистрироваться
 + Б) Модуль Регистрация:
 +  1) просим Пользователя придумать логин и пароль
 +  2) проверяем и сохряняем полученные данные
 +     - логин:
 +       - длина: более 3 и менее 20 (включительно всё)
 +       - символы: допускается использовать только буквы и/или цифры (нет в ТЗ)
 +       - уникальность: нового логина не должно быть в файле
 +       - доступность файла: проверяем файл на существование и чтение
 +     - пароль:
 +      - длина: более 4 и менее 32 (включительно)
 +       - символы: пароль должен состоять из букв и хотя бы одной цифры (нет в ТЗ)
 +       - страховка: вводим новый пароль 2 раза (нет в ТЗ)
 +     - доступность файла: проверяем файл на доступность к записи и существование
 + 3) сообщаем об успешной регистрации или неудаче

 + В) Модуль Авторизация:
 +  1) запрашиваем логин и пароль
 +  2) проверяем наличие в файле введённого логина и пароля
 +     - строчные и заглавные буквы должны отличаться
 +  3) сообщаем об успешной авторизации или неудаче
"""


def main():
    while True:
        answer = input('Введите 1 для авторизации, и 2 для регистрации: ')
        if answer == '1':
            get_authorization()
            break
        elif answer == '2':
            get_registration()
            break


def get_authorization():
    print('Вызвана функция 1: авторизация\n')
    while True:
        if 'user_login' not in locals():
            user_login = input('Ваш логин пожалуйста: ')
        if user_login == '':
            user_login = input('Попробуйте ещё раз: ')
            if user_login == '':
                print('Ошибка: введён пустой логин')
                continue

        user_paswd = input('Ваш пароль пожалуйста: ')
        if user_paswd == '':
            print('Ошибка: введён пустой пароль')
        else:
            break

    try:
        with open('file_with_login_pass.txt', encoding='utf-8') as file:
            body_file = file.readlines()
    except FileNotFoundError:
        print('Ошибка авторизации: файл с данными не найден.')
        return -1
    except PermissionError:
        print('Ошибка авторизации: недостаточно прав для чтения файла.')
        return -1

    for line in body_file:
        if user_login == line.split()[0] and user_paswd == line.split()[1]:
            print('Авторизация выполнена успешно!')
            return 1

    print('Логин или пароль не найдены или указаны неверно.\n')
    repeat = input('Введите 1, если хотите попробовать ещё раз: ')
    if repeat == '1':
        get_authorization()
    else:
        return 0


def get_login_verification(login: str):
    try:
        with open('file_with_login_pass.txt', encoding='utf-8') as file:
            body = file.readlines()
    except FileNotFoundError:
        print('Ошибка верификации: файл с данными не найден.')
        return 0
    except PermissionError:
        print('Ошибка верификации: недостаточно прав для чтения файла.')
        return 0

    for i in body:
        if i.split()[0] == login:
            print(f'Логин {login} уже занят.')
            return 0

    chek_num, chek_alf = 0, 0
    for i in login:
        if i.isnumeric():
            chek_num += 1
        elif i.isalpha():
            chek_alf += 1

    err_detls = ''
    log_len = len(login)
    if log_len < 3:
        err_detls = '- cлишком короткий логин\n'
    elif log_len > 20:
        err_detls = '- cлишком длинный логин\n'

    if chek_num == 0 and chek_alf == 0:
        err_detls += '- логин не содержит ни одну букву или цифру.\n'

    if log_len != chek_num + chek_alf:
        err_detls += '- логин содержит недопустимые символы:\n'

    if err_detls != '':
        print(f'Логин "{login}" не соответствует критериям:\n{err_detls}')
        return 0
    else:
        return 1


def creat_login():
    while True:
        new_login = input(
            'Придумайте логин подходящий под следующие критерии:\n'
            '  1) длина от 3 по 20 символов\n'
            '  2) использованы только буквы и/или цифры\n'
            'Введите новый логин здесь: ')

        if new_login == '':
            new_login = input('Попробуйте ещё раз: ')
            if new_login == '':
                print('Ошибка: введён пустой логин\n')
        else:
            if get_login_verification(new_login) == 1:
                print('Прекрасный логин!\n')
                return new_login

            repeat = input('Введите 1, чтобы попробовать ещё раз: ')
            if repeat != '1':
                return 0


def get_new_passwd_verification(passwd: str):
    chek_num, chek_alf = 0, 0
    for i in passwd:
        if i.isnumeric():
            chek_num += 1
        elif i.isalpha():
            chek_alf += 1

    err_detls = ''
    passwd_len = len(passwd)
    if passwd_len < 4:
        err_detls = '- cлишком короткий пароль\n'
    elif passwd_len > 32:
        err_detls = '- cлишком длинный пароль\n'

    if chek_num == 0 and chek_alf == 0:
        err_detls += '- пароль не содержит ни букв ни цифр.\n'

    if passwd_len != chek_num + chek_alf:
        err_detls += '- пароль содержит недопустимые символы:\n'

    if err_detls != '':
        print(f'Пароль "{passwd}" не соответствует критериям:\n{err_detls}')
        return 0
    else:
        return 1


def creat_passwd():
    while True:
        new_passwd = input(
            'Придумайте пароль подходящий под следующие критерии:\n'
            '  1) длина от 4 по 32 символов\n'
            '  2) состоит из букв и хотя бы одной цифры\n'
            'Введите новый пароль здесь: ')

        if new_passwd == '':
            new_passwd = input('Попробуйте ещё раз: ')
            if new_passwd == '':
                print('Ошибка: введён пустой пароль\n')
        else:
            if get_new_passwd_verification(new_passwd) == 1:
                print('Прекрасный пароль!\n')
                return new_passwd
            else:
                repeat = input('Введите 1, чтобы попробовать ещё раз: ')
                if repeat != '1':
                    return 0


def get_registration():
    print('Вызвана функция 2: регистрация\n')

    new_login = creat_login()
    if new_login == 0:
        print('Регистрация отменена пользователем: этап создание логина.')
        return 0

    new_paswd = creat_passwd()
    if new_paswd == 0:
        print('Регистрация отменена пользователем: этап создание пароля.')
        return 0

    while True:
        test_passwd = input(
            'Введите пароль ещё раз, чтобы запомнить его: ')
        if new_paswd == test_passwd:
            print('Всё правильно, сохряняю ваши данные ...\n')
            break
        else:
            repeat = input('Введите 1, чтобы попробовать ещё раз: ')
            if repeat != '1':
                print('Регистрация отменена пользователем: разные пароли')
                return 0

    try:
        with open('file_with_login_pass.txt', 'a', encoding='utf-8') as file:

            file.write(f'{new_login} {new_paswd}')
        print('Регистрация выполнена успешно!')
        return 1
    except PermissionError:
        print('Ошибка регистрации: недостаточно прав для работы с файлом.')
        return 0


if __name__ == '__main__':
    main()
