from math import ceil

# Работа со списками
employee_list = ['Jonh Snow', 'Piter Pen',
                 'Drakula', 'IvanIV', 'Moana', 'Juilet']
# Выведите на экран второй и второй с конца элементы через запятую.
# Продумайте такое решение,
# которое можно было бы применить к списку любой длины.
if len(employee_list) >= 2:
    print(employee_list[1] + ', ' + employee_list[-2])
else:
    print('Список слишком короткий')

# Проверить делиться ли число на 3.


def dev_by_three(x):
    return 'Да' if x % 3 == 0 else 'Нет'


x = int(input('Число: '))
result = dev_by_three(x)
print(f'Делиться ли на три {x}? - ', result)

# Округление
# Минимальное количество коробок, необходимых для упаковки предметов,
# если в одну коробку помещается не более пяти предметов


def min_boxes(x):
    return ceil(x/5)


x = int(input('Количество предметов: '))
print(min_boxes(x))

# Два делителя
n = int(input('Введите число: '))


def check_divisibility(n):
    for x in range(1, n+1):
        if x % 4 == 0:
            print(f'{x} - Делится и на 2, и на 4')
        elif x % 2 == 0:
            print(f'{x} - Делится на 2, но не на 4')
        else:
            print(x)


check_divisibility(n)


# Квартал
def quarter_of_year(x):
    if not 1 <= x <= 12:
        raise ValueError('Месяц должен быть от 1 до 12')

    if 1 <= x <= 3:
        return 'I квартал'
    elif 4 <= x <= 6:
        return 'II квартал'
    elif 7 <= x <= 9:
        return 'III квартал'
    else:
        return 'IV квартал'


try:
    x = int(input('Введите месяц: '))
    print(quarter_of_year(x))
except ValueError:
    print("Ошибка: нужно ввести целое число от 1 до 12")

# Фильтрация списка
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
for n in lst:
    if n % 3 == 0 and n > 15:
        print(n)

# Range
set = list(range(25, 0, -5))
print(set)

# Поменять значения местами
var_1 = 50
var_2 = 5
temp = var_1
var_1 = var_2
var_2 = temp
print(var_1, var_2)
