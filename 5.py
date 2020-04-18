print ('Задание 5')

numbers = (input("Введите числа через пробелы "))
numbers = numbers.split()
print (numbers)
l = len(numbers)
i = 0
while i < l:
    numbers[i] = int(numbers[i])
    i=i+1

numbers.sort()
print (numbers)
k = 1
while k == True:
    new = int(input("Добавьте новое число "))
    numbers.append(new)
    numbers.sort()
    print(numbers)
    print ("Нажмите на цифру 1 для добавления нового элемента")
    k = int(input('Или нажмите 0 что бы закончить '))