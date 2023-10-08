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
from typing import Union

REQUEST_REENTER_DATA = 'Введите 1 для повторного ввода: '
DATA_FILE = 'file_with_login_pass.txt'


def main() -> None:
    """
    Запуск кода для регистрации или авторизации пользователя
    :return: ничего не возвращает - только запускает выбранные модуль
    """
    while True:
        answer = input('Введите 1 для авторизации, и 2 для регистрации: ')
        if answer == '1':
            login()
            break
        elif answer == '2':
            register()
            break


def user_data(displ_user_text: str) -> str:
    """Запрашивает у пользователя данные"""
    user_answr = input(f'{displ_user_text}: ')
    return user_answr


def processing_file(name_file: str,
                    mode: str = 'r',
                    text_for_write: str = '') -> Union[list, bool]:
    """
    Функция возвращая содержимое файла или записывает данные в файл
    :param name_file: имя файла
    :param mode: режим открытия файла
    :param text_for_write: текст для записи в файл
    :return: True - успешное выполнение функции, иначе False
    """
    try:
        with open(name_file, mode, encoding='utf-8') as file:
            if mode == 'r':
                body_file = file.readlines()
                return body_file
            file.write(f'{text_for_write}\n')
            return True
    except FileNotFoundError:
        print('Ошибка: файл с данными не найден.')
        return False
    except PermissionError:
        print('Ошибка: недостаточно прав для чтения файла.')
        return False


def error_details(chek_name: str, chek_data: str,
                  min_limit: int, max_limit: int) -> bool:
    """
    Функция проверяет переданный параметр на соответствие критериям:
    :param chek_name: имя проверяемого параметра
    :param chek_data: проверяемый параметр
    :param min_limit: минимальная длина параметра
    :param max_limit: максимальная длина параметра
    :return: True - параметр соответствует критериям,
             False - возвращается перечень несоответствий
    """
    chek_num, chek_alf = 0, 0
    for i in chek_data:
        if i.isnumeric():
            chek_num += 1
        elif i.isalpha():
            chek_alf += 1

    err_detls = ''
    chek_data_len = len(chek_data)
    if chek_data_len < min_limit:
        err_detls = f'- cлишком короткий {chek_name}\n'
    elif chek_data_len > max_limit:
        err_detls = f'- cлишком длинный {chek_name}\n'

    if chek_num == 0 and chek_alf == 0:
        err_detls += f'- {chek_name} не содержит ни одну букву или цифру.\n'
    if chek_data_len != chek_num + chek_alf:
        err_detls += f'- {chek_name} содержит недопустимые символы:\n'

    if err_detls != '':
        print(f'{chek_name.capitalize()} "{chek_data}" противоречит критериям:'
              f'\n{err_detls}')
        return False
    return True


def chek_login(login_name: str, creat_log: bool = False) -> bool:
    """
    Функция проверяет логин на соответствие критериям при разных ситуациях:
    - при регистрации - проверка на уникальность, длину и допустимые символы
    - при авторизации - только на длину и допустимые символы
    :param login_name: логин для проверки на соответствие критериям
    :param creat_log: регистрация логина (True) или авторизация (False)
    :return: True - верификация прошла успешно, False - есть ошибки
    """
    if creat_log:
        body_lines = processing_file(DATA_FILE)
        if body_lines == 0:
            return False
        for line in body_lines:
            if login_name == line.split()[0]:
                print(f'Логин {login_name} уже занят.')
                return False

    if error_details('логин', login_name, 3, 20):
        return True
    return False


def chek_pass(passwd: str) -> bool:
    """
    Функция верифицирует пароль вводимый пользователем по критериям:
    - длина пароля, содержание букв, цифр и недопустимых символов.
    :param passwd: пароль который ввёл пользователь
    :return: True - верификация прошла успешно, False - есть ошибки.
    """
    if error_details('пароль', passwd, 4, 32):
        return True
    return False


def login() -> bool:
    """
    Функция выполняем авторизацию пользователя.
    :return: True - авторизация успешно выполнена, иначе False
    """
    print('Вызвана функция 1: авторизация\n')
    login_user = user_data('Введите ваш логин')
    passwd = user_data('Введите ваш пароль')
    verif_login = chek_login(login_user)
    verif_passwd = chek_pass(passwd)
    if verif_login == 0 or verif_passwd == 0:
        repeat = input(REQUEST_REENTER_DATA)
        if repeat == '1':
            login()
        return False

    body_lines = processing_file(DATA_FILE)
    if body_lines != 0:
        for line in body_lines:
            if login_user == line.split()[0] and passwd == line.split()[1]:
                print('Авторизация успешно выполнена!')
                return True

    print('Авторизация не выполнена.')
    return False


def creat_login() -> Union[str, bool]:
    """
    Функция создаёт новый логин.
    :return: True - создание логина успешно выполнено, иначе False
    """
    while True:
        new_login = input(
            'Придумайте логин подходящий под следующие критерии:\n'
            '  1) длина от 3 по 20 символов\n'
            '  2) использованы только буквы и/или цифры\n'
            'Введите новый логин здесь: ')

        if chek_login(new_login, True) == 1:
            print('Прекрасный логин!\n')
            return new_login

        repeat = input(REQUEST_REENTER_DATA)
        if repeat != '1':
            return False


def creat_passwd() -> Union[str, bool]:
    """
    Функция создаёт новый пароль.
    :return: True - создание логина успешно выполнено, иначе False
    """
    while True:
        new_passwd = input(
            'Придумайте пароль подходящий под следующие критерии:\n'
            '  1) длина от 4 по 32 символов\n'
            '  2) состоит из букв и хотя бы одной цифры\n'
            'Введите новый пароль здесь: ')

        if chek_pass(new_passwd) == 1:
            print('Прекрасный пароль!\n')
            return new_passwd

        repeat = input(REQUEST_REENTER_DATA)
        if repeat != '1':
            return False


def passwd_compare(passwd: str) -> bool:
    """
    Функция сравнивает второй ввод пароля с перым.
    :param passwd: первый ввод пароля пользователем
    :return: True - пароли совпадают, иначе False
    """
    while True:
        test_passwd = input('Введите пароль ещё раз, чтобы запомнить его: ')
        if passwd == test_passwd:
            return True

        repeat = input(REQUEST_REENTER_DATA)
        if repeat != '1':
            return False


def register() -> bool:
    """
    Функция регистрирует логин и пароль нового пользователя
    :return: True - регистрация прошла успешно, иначе False
    """
    print('Вызвана функция 2: регистрация\n')

    new_login = creat_login()
    if new_login == 0:
        print('Регистрация отменена пользователем: этап создание логина.')
        return False

    new_paswd = creat_passwd()
    if new_paswd == 0:
        print('Регистрация отменена пользователем: этап создание пароля.')
        return False

    if not passwd_compare(new_paswd):
        print('Регистрация отменена пользователем: разные пароли')
        return False

    if not processing_file(DATA_FILE,
                           'a',
                           f'{new_login} {new_paswd}'):
        return False

    print('Регистрация выполнена успешно!')
    return True


if __name__ == '__main__':
    main()
