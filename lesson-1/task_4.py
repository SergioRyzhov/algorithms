"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

auth_dict = {
    'Vasily': ['qwerty', True],
    'Petr': ['123', True],
    'Igor': ['ferrari', False],
    'Dan': ['school', False]
}

# Сложность O(1) - константная
def try_to_auth_1(name):
    if auth_dict[name][1] == False:             # O(1) - константная
        return "You haven't activation. You should activate your account"  # O(1) - константная
    else:                                       # O(1) - константная
        return 'You are activated'              # O(1) - константная

# Сложность O(n) - линейная
def try_to_auth_2(name):
    for i in auth_dict.keys():                  # O(n) - линейная
        if i == name:                           # O(1) - константная
            if auth_dict[i][1] == False:        # O(1) - константная
                return "You haven't activation. You should activate your account"  # O(1) - константная
            else:                               # O(1) - константная
                return 'You are activated'      # O(1) - константная


inp_name_string = input('Input your name: ')
inp_pass_string = input('Input the password: ')
if auth_dict[inp_name_string][0] == inp_pass_string:
    print(try_to_auth_1(inp_name_string))
    print(try_to_auth_2(inp_name_string))

# Вывод: Первая функция эффективнее потому что ее сложность константная.
# Если смотреть на график роста О-большое, то видно, что константная функция
# занимает меньше времени чем линейная при одинаковом количестве элементов.