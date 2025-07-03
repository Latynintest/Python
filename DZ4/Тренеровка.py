# функция string_or_not(), проверяет является ли переданный параметр строкой.
# def string_or_not(parameter):
#     return isinstance(parameter, str) and "yes" or "no"


# print(string_or_not('10'))

# функция guess_number(), принимает число и проверяет, равно ли число заданному
# def guess_number(namber):
#     if namber == 42:
#         return 'You win!'
#     return 'Try again!'

# функция normalize_url(), выполняет нормализацию данных.
# # Она принимает адрес сайта и возвращает его с https:// в начале
# def normalize_url(url):
#     if url.startswith('https://'):
#         return url
#     elif url.startswith('http://'):
#         return 'https://' + url[7:]  # Удаляем 'http://' и добавляем 'https://'
#     else:
#         return 'https://' + url


# print(normalize_url('https://yandex.ru'))

# def who_is_this_house_to_starks(family):
#     if family == 'Karstark' or family == 'Tully':
#         return 'friend'
#     elif family == 'Lannister' or family == 'Frey':
#         return 'enemy'
#     else:
#         return 'neutral'


# print(who_is_this_house_to_starks('Frey'))

# функция get_number_explanation(), принимает на вход число и возвращает
# объяснение этого числа.
# Если для числа нет объяснения, то возвращается just a number.
# Объяснения есть только для следующих чисел:

# 666 - 'devil number'
# 42 - 'answer for everything'
# 7 - 'prime number'


# def get_number_explanation(number):
#     match number:
#         case 666:
#             return 'devil number'
#         case 42:
#             return 'answer for everything'
#         case 7:
#             return 'prime number'
#         case _:
#             return 'just a number'


# print(get_number_explanation(0))
