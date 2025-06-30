# 139112739

num = int(input())  # Ввод количества чисел в массиве.
input_str = input()  # Ввод массива.

data = []  # Сделаем строку списком целых чисел.

if len(input_str.split()) != num:  # Если не совпадает количество, то
    print("Ошибка: количество чисел не совпадает.")  # выведем ошибку.

for item in input_str.split():  # Создадим список в data.
    data.append(int(item))

sorted_data = set()  # Создадим пустое множество.
exit_massive = []  # Создадим список уникальных чисел.
dublicate = 0   # Создадим счетчик дубликатов.

for i in data:   # Для всех элементов в списке data:
    if i not in sorted_data:  # если элемента нет во множестве, то
        exit_massive.append(i)  # добавляем в список уникальных,
        sorted_data.add(i)
    else:
        dublicate += 1  # если элемент не уникален, то плюсуем 1.

result = exit_massive + dublicate*['_']  # Выводим сначала уникальные элементы.


print(' '.join(str(x) for x in result))  # Выводим строки через пробел.
