# Напишите функцию month_to_season(), которая принимает один аргумент — номер
# месяца — и возвращает название сезона, к которому относится этот месяц.
def month_to_season(number):
    if not 1 <= number <= 12:
        raise ValueError('Месяц должен быть от 1 до 12')
    if 1 <= number <= 2 or number == 12:
        return 'Зима'
    elif 3 <= number <= 5:
        return 'Весна'
    elif 6 <= number <= 8:
        return 'Лето'
    else:
        return 'Осень'


try:
    number = int(input('Введите месяц от 1 до 12: '))
    season = month_to_season(number)
    print(season)
except ValueError:
    print("Ошибка: нужно ввести целое число от 1 до 12")
