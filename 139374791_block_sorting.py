# 139374791

def block_sorting(massive):
    blocks = 0  # Переменная для подсчета макс. числа блоков, изначально = 0.
    max_number = 0  # Инициализируем переменную, хранящую максимум.
    for i, value in enumerate(massive):  # Переберем индексы и значения.
        max_number = max(max_number, value)  # Отбираем максимум.
        if max_number == i:  # Если максимум равен текущему индексу,
            blocks += 1  # увеличиваем blocks на 1.
    return blocks  # Вернем количество blocks.

if __name__ == '__main__':
    n = int(input())
    if not (1 <= n <= 1000):  # Количество чисел для сортировки (n ≤ 1000).
        print("False: n должно быть от 1 до 1000")
    non_sorted_massive = input()  # числа от 0 до n - 1, которые надо разбить.
    massive = [int(item) for item in non_sorted_massive.split()]
    print(block_sorting(massive))
