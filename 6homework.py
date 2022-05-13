summa = 0
numbers = 123456
text = str(numbers)
print(text)

for i in range(6):
    num = int(text[i])
    summa = num + summa
print('Сумма цифр числа=', summa)
