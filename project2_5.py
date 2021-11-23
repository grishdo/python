rating = int(input('Введите элемент рейтинга: '))
my_list = [7, 5, 3, 3, 2, rating]
index = 0

for i in reversed(my_list):
    if index == 0:
        index -= 1
        continue
    if rating == i:
        break
    elif rating > i:
        a = my_list[index]
        b = my_list[index - 1]
        my_list[index] = b
        my_list[index - 1] = a
    index -= 1

print(my_list)



