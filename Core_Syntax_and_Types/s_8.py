# Docstring. Write a fully documented fizzbuzz(n) with a Google-style docstring including two doctest examples, and make python -m doctest pass on it.

def fizzbuzz(n):
    """
    Return FizzBuzz for the given integer.

    Args:
        n (int): The number to check.

    Returns:
        str: The corresponding FizzBuzz result.

    Examples:
        >>> fizzbuzz(3)
        'Fizz'
        >>> fizzbuzz(5)
        'Buzz'
        >>> fizzbuzz(15)
        'FizzBuzz'
    """

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'

    elif n % 3 == 0:
        return "Fizz"

    elif n % 5 == 0:
        return "Buzz"

    else:
        return f" '{n}' "

print(fizzbuzz(11))