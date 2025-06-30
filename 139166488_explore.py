# 139166488

text = input()  # Ввод исходной строки.
uniq = set() # Множество для хранения символов в скользящем окне.
max_length = 0  # Длина самой длинной подстроки.
max_start = 0  # Индекс начала самой длинной подстроки.
start = 0  # Начало скользящего окна.

# Алгоритм использует два указателя: start (левая граница) и finish (правая граница).
# Окно [start, finish] представляет подстроку с уникальными символами.
# При обнаружении дубликата окно сужается слева (увеличивается start, 
# удаляются символы из uniq), пока дубликат не исчезнет.
for finish in range(len(text)):
        # Пока текущий символ есть в окне, удаляет символы с начала.
        while text[finish] in uniq:
            uniq.remove(text[start])
            start += 1
        uniq.add(text[finish])
        # Проверяет, является ли текущее окно самым длинным.
        if finish - start + 1 > max_length:
            max_length = finish - start + 1
            max_start = start
    # Возвращаем подстроку от max_start до max_start + max_length.
result = text[max_start:max_start + max_length]

print(len(result))
