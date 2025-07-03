import pytest
from string_processor import StringProcessor

# Позитивные тесты


@pytest.mark.parametrize("input_str, expected", [
    ("hello", "Hello."),
    ("test", "Test."),
    ("a", "A."),
    ("   test", "   test."),
    ("test   ", "Test   ."),
    ("Hello world", "Hello world."),
])
def test_positive(input_str, expected):
    assert StringProcessor.process(input_str) == expected

# Негативные тесты


@pytest.mark.parametrize("invalid_input, expected_exception", [
    (123, TypeError),
    (True, TypeError),
    (3.14, TypeError),
])
def test_non_string_inputs(invalid_input, expected_exception):
    with pytest.raises(expected_exception):
        StringProcessor.process(invalid_input)


def test_empty_string():
    assert StringProcessor.process("") == "."
