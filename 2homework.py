numbers=0
counter=0

for i in range(10):
    numbers = input('введите 10 цифр от 0 до 9 ')
    if numbers == '5':
        counter = counter + 1
print('количество введенных 5 =', counter)