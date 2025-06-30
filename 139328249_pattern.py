# 139328249

def sorting(massive: list[int], pattern: list[int]):
    '''Метод сортировки грузового космического корабля по шаблону.'''
    sorted_massive: list[int] = sorted(massive)
    result_main: list = []  # Список для хранения значений массива.
    result_tail: list = []  # Список для хранения значений хвоста.
    for target in pattern:  # Для всех значений в шаблоне,
        for i in sorted_massive:  # проверим наличие в массиве.
            if i == target:  # Если значение массива есть в шаблоне,
                result_main.append(i)  # то запишем в result_main.
    for j in sorted_massive:  # Проверим значения, которых нет в шаблоне.
        if j not in result_main:  # Если значения нет в шаблоне,
            result_tail.append(j)  # то запишем в список result_tail.
    result = result_main + sorted(result_tail)
    return print(*result)  # Распакуем список.


if __name__ == '__main__':
    n = int(input())  # Количество чисел, которые нужно отсортировать.
    non_sorted_massive = input()  # n чисел, которые надо отсортировать.
    m = int(input())  # Длина массива-шаблона.
    massive_pattern = input()  # Массив-шаблон для сортировки.
    # Преобразуем строки в списки чис
    massive = [int(item) for item in non_sorted_massive.split()]
    pattern = [int(item) for item in massive_pattern.split()]
    sorting(massive, pattern)
