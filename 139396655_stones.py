# 139396655

def delivery_of_stones(massive: list[int], delivery: list[int]):
    '''Метод распределения образцов между заказчиками оптимальным образом.'''
    sort_massive: list[int] = sorted(massive, reverse=True)  # Отсортируем.
    sort_delivery: list[int] = sorted(delivery, reverse=True)  # Отсортируем.
    ready = 0  # Счетчик выполненных заказов.
    order = 0  # Индекс текущего заказа в sort_massive.
    for value in sort_delivery:
        # Перебирает веса доставленных образцов от тяжелого к легкому.
        while order < len(sort_massive) and sort_massive[order] > value:
            order += 1  # Если заказ тяжелый, переходим к следующему заказу.
        if order < len(sort_massive):   # Если заказ меньше длины массива,
            ready += 1  # значит заказ найден,
            order += 1  # двигаемся к следующему заказу.
    return ready


if __name__ == '__main__':
    n = int(input())  # n — количество заказов от музеев и лабораторий.
    request_massive = input()  # Заказано, где каждый элемент - вес образца.
    m = int(input())  # m — количество образцов, доставленных с Марса.
    fact_massive = input()  # Доставлено, где каждый элемент - вес образца.
    # Преобразуем строки в списки целых чисел.
    request = [int(item) for item in request_massive.split()]
    fact = [int(item) for item in fact_massive.split()]
    print(delivery_of_stones(request, fact))
