entering_numbers= input('Введите элементы 1-го списка: ')
input_numbers= input('Введите элементы 2-го списка: ')
# если ввод разными знаками используем метод replace, разделить элементы помогает split
numbers =(entering_numbers.replace(';',',').replace(',', ' ').split())

amount =(input_numbers.replace(';',',').replace(',', ' ').split())

print(set(numbers)-set(amount))

