print ('Задание 4')

text = input("Введите слова через пробелы ")
new_text = text.split()
print (new_text)
l =  int(len(new_text))

k=0
while k < l:
    lil_text = list(new_text[k])
    lil_l = len(lil_text)
    if lil_l <= 10:
     print (k+1, ').', new_text[k])
     k = k+1
    else :
        lil_text = new_text[k]
        print (k+1, ').', lil_text[0:9])
        k = k+1
        lil_text = lil_text[9:]
        print(k + 1, ').', lil_text[0:9])
        lil_text = lil_text[9:]
        while lil_text :
            print(k + 1, ').', lil_text[0:9])
            k = k + 1
            lil_text = lil_text[9:]


