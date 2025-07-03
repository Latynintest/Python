import pytest
from calculator import Calculator

calculator = Calculator()

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-6, -10)
assert res == -16

res = calculator.sum(-6, 6)
assert res == 0

res = calculator.sum(5.6, 4.3)
res = round(res, 1)
print(res)
assert res == 9.9

res = calculator.sum(10, 0)
assert res == 10


res = calculator.div(10, 2)
assert res == 5

# res = calculator.div(10, 0)
# assert res == None


numbers = []
res = calculator.avg(numbers)
assert res == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]  # сумма чисел будет = 50
res = calculator.avg(numbers)
print(res)
assert res == 5  # среднее арифметическое равно 50/10


@pytest.mark.positive_test
@pytest.mark.xfail(strict=False)  # или True - на ваше усмотрение
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9


@pytest.mark.skip  # декоратор для пропуска теста
@pytest.mark.skip(reason="починить тест позже")  # указали параметр и причину
def test_sum_negative_nums():  # поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, -10)  # поменяли параметры
    assert res == -16  # поменяли ожидаемую сумму


def test_sum_positive_and_negative_nums():  # поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, 6)  # поменяли параметры
    assert res == 0  # поменяли ожидаемую сумму


def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(7.6, 4.3)
    res = round(res, 1)
    assert res == 11.9


def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(0, 5)
    assert res == 5


@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5


def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):  # предупреждаем Pytest об ошибке
        calculator.div(10, 0)


def test_avg_empty_list():
    calculator = Calculator()
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0


@pytest.mark.positive_test
def test_avg_positive():
    calculator = Calculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]  # сумма чисел будет = 50
    res = calculator.avg(numbers)
    assert res == 5


@pytest.mark.parametrize('num1, num2, result', [
    (4, 5, 9),
    (-6, -10, -16),
    (-6, 6, 0),
    (5.61, 4.29, 9.9),
    (10, 0, 10)])
def test_sum_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result


@pytest.mark.parametrize('nums, result', [
    ([], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)])
def test_avg_list(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.positive_test
def test_div_positive(calculator):
    res = calculator.div(10, 2)
    assert res == 5


def test_div_by_zero(calculator):
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)


def test_avg_empty_list(calculator):
    numbers = []
    res = calculator.avg(numbers)
    assert res == 0


@pytest.mark.positive_test
def test_avg_positive(calculator):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    res = calculator.avg(numbers)
    assert res == 5


@pytest.mark.parametrize('num1, num2, result', [
    (4, 5, 9),
    (-6, -10, -16),
    (-6, 6, 0),
    (5.61, 4.29, 9.9),
    (10, 0, 10)])
def test_sum_nums(calculator, num1, num2, result):
    res = calculator.sum(num1, num2)
    assert res == result


@pytest.mark.parametrize('nums, result', [
    ([], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5)])
def test_avg_list(calculator, nums, result):
    res = calculator.avg(nums)
    assert res == result
