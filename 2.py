print ('Задание 2')

spisok = []
kol = int(input('Введите размер списка ' ))
for i in range(kol):
    new_element = (input('Введите элемент '))
    spisok.append(new_element)

print (spisok)
k = 0
while k < kol-1:
     now = spisok [k]
     spisok[k] = spisok [k+1]
     spisok [k+1] = now
     print(k)
     k = k+2
print (spisok)

