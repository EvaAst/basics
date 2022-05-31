entering_numbers = input('Введите любые цифры через запятую ')
# если ввод разными знаками используем метод replace, разделить элементы помогает split
numbers = (entering_numbers.replace(';', ',').replace(',', ' ').split())

result = []
for i in numbers:
    if numbers.count(i) == 1:
        result.append(i)  # append добавляет элемент в конец
print(result)
