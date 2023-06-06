# Напишите программу, которая на вход принимает два 
# числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
def degree_recursion(num, to_the_power_of_num):
    if to_the_power_of_num == 0:
        return 1
    return num * degree_recursion(num, to_the_power_of_num - 1)
num = int(input('Введите число: '))
to_the_power_of_num = int(input('Введите степень: '))
print(degree_recursion(num, to_the_power_of_num))
