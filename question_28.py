# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.
def sum_recursion(first_temp, second_temp):
    if second_temp == 0:
        return first_temp
    return 1 + sum_recursion(first_temp, second_temp - 1)
first_temp = int(input('Введите первое слагаемое: '))
second_temp = int(input('Введите второе слагаемое: '))
print(sum_recursion(first_temp, second_temp))
