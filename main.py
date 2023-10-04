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
#         - длина: более 3 и менее 20 (включительно всё)
#         - символы: допускается использовать только буквы и цифры (нет в ТЗ)
#         - уникальность: нового логина не должно быть в файле
#         - доступность файла: проверяем файл на доступность к записи и существование
#       - пароль:
#         - длина: более 4 и менее 32 (включительно)
#         - простота: пароль должен состоять из букв и хотя бы одной цифры (нет в ТЗ)
#         - страховка: вводим новый пароль 2 раза (нет в ТЗ)
#   3) сообщаем об успешной регистрации или неудаче

# + В) Модуль Авторизация:
# +  1) запрашиваем логин и пароль
# +  2) проверяем наличие в файле введённого логина и пароля
# +     - строчные и заглавные буквы должны отличаться
# +  3) сообщаем об успешной авторизации или неудаче

def main():
    while True:
        answer = input('Введите 1, если вы хотите авторизоваться, и 2 - зарегистрироваться):')
        if not answer.isnumeric():
            continue
        elif 1 <= int(answer) <= 2:
            get_authorization() if int(answer) == 1 else get_registration()
            break


def get_authorization():
    print(f'Вызвана функция 1: авторизация')
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
            continue
        else:
            break

    try:
        with open('file_with_login_pass.txt') as file:
            body_file = file.readlines()
    except:
        print('Файл с данными не найден. Авторизация не выполнена.')
        return -1

    for l in body_file:
        if user_login == l.split()[0] and user_paswd in l.split()[1]:
            print('Авторизация выполнена успешно!')
            return 1

    else:
        print('Логин или пароль не найдены или указаны неверно.\n')
        repeat = input('Напишите 1, если хотите попробовать ввести логин и пароль ещё раз.')
        try:
            int(repeat) == 1
            user_login = user_paswd = ''
            get_authorization()
        except:
            return 0


def get_registration():
    print(f'Вызвана функция 2: регистрация')
    pass


if __name__ == '__main__':
    main()
