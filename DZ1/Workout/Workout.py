# Создать переменную
my_heigh = 172
print(my_heigh)

# Перезаписать переменную
my_name = 'Sergey'
my_name = 'Sergey Latynin'
print(my_name)

# Получить пользовательский ввод
pet_name = input("What is your pet's name? ")
print('Your pet ' + pet_name)

# Создать функцию


def print_python():
    print('Учу Python!')


print_python()

# Параметризация функции


def print_letter(let):
    print(let, end='')


print_letter('С')
print_letter('Т')
print_letter('У')
print_letter('Д')
print_letter('Е')
print_letter('Н')
print_letter('Т')
