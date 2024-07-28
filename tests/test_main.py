import pytest
from main import sum_of_elements, is_palindrome, factorial


@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3, 4], 10),
    ([0, 0, 0], 0),
    ([-1, -2, -3], -6),
    ([1.5, 2.5, 3.5], 7.5),
    ([], 0)
])
def test_sum_of_elements(lst, expected):
    assert sum_of_elements(lst) == expected


@pytest.mark.parametrize("s, expected", [
    ("radar", True),
    ("hello", False),
    ("level", True),
    ("", True),
    ("a", True)
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial(n, expected):
    assert factorial(n) == expected
