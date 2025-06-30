# 139239024

generation = int(input())


def counter_olimp(n):
    if n == 0:  # Базовый случай.
        return 1
    if n == 1:  # Базовый случай.
        return 1
    return (counter_olimp(n - 1) + counter_olimp(n - 2))  # Рекурсивный случай.


print(counter_olimp(generation))
