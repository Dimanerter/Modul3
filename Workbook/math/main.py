import math 

# math.ceil(x) - виконує округлення дійсного числа x до найближчого більшого цілого числа;
# math.floor(x) - виконує округлення дійсного числа x до найближчого меншого цілого числа;
# math.trunc(x) - виконує обрізання дробової частини дійсного числа x, та повертає цілу частину числа;

x = 3.7

#  Використання різних методів округлення

ceil_result = math.ceil(x)
floor_result = math.floor(x)
trunc_result = math.trunc(x)

print(ceil_result, floor_result, trunc_result)

# Приклад використання пакета math
# Використання констант
print(math.pi)

# Тригонометрія
angle = math.radians(60)
print(math.sin(angle))

# Корінь числа
print(math.sqrt(9))

# Логарифми
print(math.log(10, 2))


# Сравнение

print(0.1 + 0.2 == 0.3)
# Сравнение math 

r = math.isclose(0.1 + 0.2, 0.3)
print(r)




