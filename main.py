#   Условия задачи:
#   - создать два модуля Регистрация и Авторизация
#   - можо использовать любые библиотеки
#   - программа должна быть консольной

#   Критерии хорошего решения (КХР):
#   - придерживаемся стандартов PEP8
#   - любые названия должны быть обоснованы
#   - программа должна быть написана на "функциях"
#   - должны быть тесты с защитой от основных ошибок

# Использование:
# + А) При старте спрашиваем что необходимо: авториазоваться или зарегистрироваться
#   Б) Модуль Регистрация:
#    1) просим Пользователя придумать логин и пароль
#    2) проверяем и сохряняем полученные данные
#       - логин:
# +       - длина: более 3 и менее 20 (включительно всё)
# +       - символы: допускается использовать только буквы и/или цифры (нет в ТЗ)
#         - уникальность: нового логина не должно быть в файле
#       - пароль:
#         - длина: более 4 и менее 32 (включительно)
#         - символы: пароль должен состоять из букв и хотя бы одной цифры (нет в ТЗ)
#         - страховка: вводим новый пароль 2 раза (нет в ТЗ)
#       - доступность файла: проверяем файл на доступность к записи и существование
#   3) сообщаем об успешной регистрации или неудаче

# + В) Модуль Авторизация:
# +  1) запрашиваем логин и пароль
# +  2) проверяем наличие в файле введённого логина и пароля
# +     - строчные и заглавные буквы должны отличаться
# +  3) сообщаем об успешной авторизации или неудаче

def main():
    while True:
        answer = input('Введите 1 для авторизации, и 2 для регистрации: ')
        if not answer.isnumeric():
            continue
        elif 1 <= int(answer) <= 2:
            get_enter() if int(answer) == 1 else get_register()
            break


def get_enter():
    print('Вызвана функция 1: авторизация\n')
    while True:
        if 'user_login' not in locals():
            user_login = input('Ваш логин пожалуйста: ')
        if user_login == '':
            user_login = input('Попробуйте ещё раз: ')
            if user_login == '':
                print('Ошибка: введён пустой логин')
                continue

        user_paswd = input('Ваш пароль пожалуйста:')
        if user_paswd == '':
            print('Ошибка: введён пустой пароль')
        else:
            break

    try:
        with open('file_with_login_pass.txt') as file:
            body_file = file.readlines()
    except FileNotFoundError:
        print('Файл с данными не найден. Авторизация не выполнена.')
        return -1

    for l in body_file:
        if user_login == l.split()[0] and user_paswd in l.split()[1]:
            print('Авторизация выполнена успешно!')
            return 1

    print('Логин или пароль не найдены или указаны неверно.\n')
    repeat = input('Напишите 1, если хотите попробовать ещё раз: ')
    try:
        if int(repeat) == 1:
            get_enter()
    except (TypeError, ValueError):
        return 0


def get_login_verification(login: str):
    check_len, chek_num, chek_alf = 0, 0, 0
    if 3 <= len(login) <= 20:
        check_len += 1
        for i in login:
            if check_len + chek_num + chek_alf >= 2:
                return 1
            elif i.isnumeric() and chek_num == 0:
                chek_num += 1
            elif i.isalpha() and chek_alf == 0:
                chek_alf += 1
    return 0


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
                print('Прекрасный логин!')
                return 1
            else:
                repeat = input('Логин не соответствует нужным критериям.\n'
                               'Нажмите 1, чтобы попробовать ещё раз: ')
                try:
                    if int(repeat) != 1:
                        break
                except (TypeError, ValueError):
                    return 0


def creat_passwd():
    pass

def get_register():
    print('Вызвана функция 2: регистрация\n')
    new_login = creat_login()
    if new_login == 0:
        return 0
    new_paswd = creat_passwd()
    if new_paswd == 0:
        return 0


if __name__ == '__main__':
    main()
