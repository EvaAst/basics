amount = input('Введите количество элементов ')
numbers = int(amount)
result = []

for i in range(numbers):
    number = int(input('Введите элемент: '))
    result.append(number)  # append добавляет элемент в конец

result.sort()
print(result)
