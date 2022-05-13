numbers =input('Введите число')
text = str(numbers)
counter = 0
for i in range(len(text)):
    num = int(text[i])
    if num == 5:
        counter = counter + 1

if counter > 0:
    print('Цифра 5 есть в числе')
else: print ('Цифры 5 нет в числе')

