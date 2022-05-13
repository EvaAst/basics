summa = 1
numbers = 1203457
text = str(numbers)
print(text)

for i in range(7):
    num = int(text[i])
    if num == 0: num = 1
    summa = num * summa
print('Произведение цифр числа=', summa)
