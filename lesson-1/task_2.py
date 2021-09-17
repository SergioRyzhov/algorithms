"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

# Сложность O(n^2) - квадратичная

def minimalizator_quadratic(ls):
    for i in range(len(ls)):                    # O(n) - линейная
        for j in range(len(ls)):                # O(n) - линейная
            if i == j:                          # O(1) - константная
                continue                        # O(1) - константная
            if ls[i] < ls[j]:                   # O(1) - константная
                ls[i], ls[j] = ls[j], ls[i]     # O(1) - константная
    return ls[0]                                # O(1) - константная


print(minimalizator_quadratic([5, 2, 8, 3, 2, 1, 9]))
print(minimalizator_quadratic([6, 5, 3, 2, 9, 8, 7]))


# Сложность O(n) - линейная

def minimalizator(ls):
    temp_min = ls[0]                        # O(1) - константная
    for i in range(1, len(ls) - 1):         # O(n) - линейная
        if ls[i] < temp_min:                # O(1) - константная
            temp_min = ls[i]                # O(1) - константная
    return temp_min                         # O(1) - константная


print(minimalizator([5, 2, 8, 3, 2, 1, 9]))
print(minimalizator([6, 5, 3, 2, 9, 8, 7]))