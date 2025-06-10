from functools import reduce
age = 17
if (age < 18):
    print("Берем в детский лагерь")
else:
    print("Не берем в детский лагерь")

rate_as_str = input('Оцените работу сотрудника от 1 до 5: ')
rate = int(rate_as_str)

if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

print(rate)

feedback = ' '

if rate == 1:
    feedback = input('Раскажите, что нам улучшить: ')
elif rate == 2:
    feedback = input('Расскажите, что вас смутило: ')
elif rate == 3:
    feedback = input("Расскажите, как нам стать лучше: ")
elif rate == 4:
    feedback = input("Расскажите, почему не 5: ")
else:
    feedback = input("Расскажите, за что похвалить сотрудника: ")
print(feedback)

for x in range(1, 21):
    print('x = ', x, 'x² = ', x*x)

students = ["Александр", "Михаил", "Мария", "Ольга", "Кирилл", "Олеся"]
for y in range(0, len(students)):
    print(students[y])

word = 'Test'
for spelling in word:
    print(spelling)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    if (n % 2 == 1):
        print(n)

user_login = 'admin'
user_password = 'Qwerty123456'
login = input('Login: ')
password = input('Password: ')
if login == user_login and password == user_password:
    print('Добро пожаловать')
else:
    print('Неверный логин или пароль')

password = input('Введите пароль: ')
password2 = input('Повторите пароль: ')
if password == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')


def min_number():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    num4 = float(input("Введите четвертое число: "))
    min_number = min(num1, num2, num3, num4)
    return min_number


result = min_number()
print(f"Наименьшее число: {result}")

# Сложение всех элементов списка
current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce(lambda x, y: x + y, current_list)
print(summa)
# Более простой вариант сложения
print(sum(current_list))  # Самый простой и питонический способ
