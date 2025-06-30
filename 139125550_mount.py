# 139125550

numbers = input()    # Ввод исходного массива.
data = []

for item in numbers.split():  # Создадим список data.
    data.append(int(item))


def valid_mountain_array(data) -> bool:
    index = 0
    if len(data) < 3:
        return False
    while index + 1 < len(data) and data[index] < data[index + 1]: # Подъём.
        index += 1
    if index == 0 or index == len(data) - 1: # Высота.
        return False
    while index + 1 < len(data) and data[index] > data[index + 1]:  # Спуск.
        index += 1
    return index == len(data) - 1

print(valid_mountain_array(data))
