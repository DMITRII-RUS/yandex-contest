# 139165179

nums = input()    # Ввод исходного массива от 0 до 100.
data = []
result = []

for item in nums.split():  # Создадим список в data.
    data.append(int(item))

for i in range(len(data)):
    counter = 0
    for j in range(len(data)):
        if data[j] < data[i]:
            counter += 1
    result.append(counter)

print(' '.join(str(item) for item in result))
