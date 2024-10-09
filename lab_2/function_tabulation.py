import math

from numpy.ma.core import around

a = 0.5
b = 0.9
h = 0.02

def cos(value ):
    return math.cos(x ** 0.5)
def tan(value):
    return  1 / math.tan(x ** 2)
def atan(value):
    return math.atan(x ** 3)


# Табулювання функції
x = a
while x <= b:
    f_x = 0

    if 0.6 > x :
        f_x = cos(x)
    elif 0.6 <= x < 0.7:
        f_x = tan(x)
    elif  x >= 0.7:
        f_x = atan(x)

    print(f"x = {x}, f(x) = { round(f_x, 3)}")
    x += h
    x = round(x, 3)

print(x)
 #Task2

a = 0.5
b = 0.7
h = 0.005
d = 0.001

# Функція для обчислення суми ряду з контролем похибки
def f(x, d, n_max=1):
    total = 0
    for k in range(1, n_max + 1):
        term = (x + 2) / (k * (k + 2))
        total += term
        if abs(term) < d:
            break
    return total

# Табулювання функції на інтервалі [a, b] з кроком h
x = a
while x <= b:
    f_x = f(x, d)

    print(f"x2 = {x}, f(x2) ≈ {round (f_x , 3)}")
    x += h
    x = round(x, 3)
    print(x)




