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


