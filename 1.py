print ('Задание 1')

spisok = [1, 'list', True, 0.214]
dlina = len(spisok)
i = 0
while i < dlina:
    r = type(spisok[i])
    print (r)
    i= i+1