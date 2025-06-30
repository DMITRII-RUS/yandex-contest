# 139121870

sorted_numbers = input()  # Ввод исходного массива.
element = int(input())  # Ввод целевого значения.
data = []

for item in sorted_numbers.split():  # Создадим список в data.
    data.append(int(item))

def find_element(data: list, element: int) -> (int | None):
    """Находит индекс element в отсортированном списке data."""
    left = 0
    right = len(data)
    while left < right:
        # Находим в наборе элементов индекс среднего элемента.
        # mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        if data[left] == element:
            return left
        # Если средний элемент меньше искомого...
        if data[left] < element:
            # ...то изменяем левую границу поиска:
            left = left + 1
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = left
    # Если левая граница оказалась больше правой, 
    # значит, элемент не найден. Возвращаем None.
    return left

print(find_element(data, element))
