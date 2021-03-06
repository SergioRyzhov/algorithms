"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import randint, random
from timeit import timeit
import operator
arr_1000 = [randint(0, 49) + random() for _ in range(1000)]
arr_100 = arr_1000[:100]
arr_10 = arr_1000[:10]
print('Массивы большие, поэтому вывожу 5 последних эл-тов.')
print(f'Исходный 1000 : {arr_1000[-5:]}')
print(f'Исходный 100 : {arr_100[-5:]}')
print(f'Исходный 10 : {arr_10[-5:]}')


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print('')
print(f'Сортированный 1000 : ',end='')
print(merge_sort(arr_1000)[-5:])
print(timeit('merge_sort(arr_1000)', globals=globals(), number=1000))
print(f'Сортированный 100 : ',end='')
print(merge_sort(arr_100)[-5:])
print(timeit('merge_sort(arr_100)', globals=globals(), number=1000))
print(f'Сортированный 10 : ',end='')
print(merge_sort(arr_10)[-5:])
print(timeit('merge_sort(arr_10)', globals=globals(), number=1000))

"""
Аналитика:

Массивы большие, поэтому вывожу 5 последних эл-тов.
Исходный 1000 : [16.018398138477426, 5.443759873794566, 8.460446864843856, 29.993293572686426, 12.648687318563375]
Исходный 100 : [10.615718677309044, 7.174039307888709, 13.166936511408531, 23.473593336655817, 34.82551943365891]
Исходный 10 : [14.698575162151478, 20.751596626588853, 38.56567099440529, 31.939403572938925, 17.614100210443528]

Сортированный 1000 : [49.8679311505532, 49.882924741715286, 49.915295628412245, 49.91598526044102, 49.96426269693435]
3.8621704
Сортированный 100 : [45.860810573893, 47.387400864808995, 47.588750311863826, 48.11234303165015, 49.515933132649316]
0.2817479000000005
Сортированный 10 : [20.751596626588853, 31.939403572938925, 31.951161720118538, 38.56567099440529, 43.65620832636023]
0.019445799999999736

Предложенный вариант реализации выглядит элегантно и прост в понимании. Он основан на подходе сверху вниз,
это рекурсивный подход мы делим массив на N подмассивов одного элемента и сортируем пары смежных одноэлементных массивов, затем сортируем соседние пары двухэлементных массивов и т. д.
По результатам замеров время сортировки увеличивается кратно увеличению длины массива.

Вывод: Сортировка слиянием является выигрышным по времени алгоритмом, его обязательно нужно изучать и применять.
"""