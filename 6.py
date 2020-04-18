print ('Задание 6')


tovari = int(input("Введите количество товара "))

dict = []
list = []
big_dict = {}

i = 1
while i <= tovari:
    print('Информация по товару №', i)
    dict = dict({'название': input("Введите название "), 'цена': input("Введите цену "), 'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    list.append((i, dict))
    i = i + 1

    big_dict = dict(
        {'название': dict.get('название'), 'цена': dict.get('цена'), 'количество': dict.get('количество'), 'ед': dict.get('ед')})

print(list)
print(big_dict)