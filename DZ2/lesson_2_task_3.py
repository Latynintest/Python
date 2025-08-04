# Площадь квадрата со стороной a
from math import ceil


def square(a):
    side = a if a == int(a) else ceil(a)
    return side * side


print(square(5.1))
