# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

number = int(input('Enter n-> '))
slovar_number = {}

for i in range(1,number+1):
    slovar_number[i] = round((1+1/i)**i,2)

print(slovar_number)
print('Sum elements-> '+str(sum(slovar_number.values())))
