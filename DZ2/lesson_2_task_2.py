def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = 2025
result = is_year_leap(year)
print(f'{year}: {result}')
