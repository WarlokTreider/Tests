def sum_of_elements(lst):
    return sum(lst)


def is_palindrome(s):
    return s == s[::-1]


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
