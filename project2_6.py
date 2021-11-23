num_values = int(input('Введите количество кортежей: '))
list_tuples = []
name_key = 'Название'
price_key = 'Цена'
number_key = 'Количество'
unit_key = 'Ед'

i = 0
while i < num_values:
    name = input('Введите название: ')
    price = int(input('Введите цену: '))
    number = int(input('Введите количество: '))
    unit = input('Введите единицу: ')

    i += 1
    list_tuples.append((i, {name_key: name, price_key: price, number_key: number, unit_key: unit}))

print(list_tuples)

character_dict = {name_key: [], price_key: [], number_key: [], unit_key: set()}

for i in list_tuples:
    items = i[1]
    list_character = character_dict.get(name_key)
    list_character.append(items.get(name_key))

    list_character = character_dict.get(price_key)
    list_character.append(items.get(price_key))

    list_character = character_dict.get(number_key)
    list_character.append(items.get(number_key))

    list_character = character_dict.get(unit_key)
    list_character.add(items.get(unit_key))

print(character_dict)
