# Casting. Write parse_number(s) that returns an int if the string is an integer, a float if it's a float, and raises ValueError otherwise. parse_number("3") → 3 (an int), parse_number("3.0") → 3.0 (a float).

def parse_number(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            raise ValueError

# parse_number("saif")

x = parse_number("3")
print(x, type(x))  # 3 <class 'int'>

x = parse_number("3.0")
print(x, type(x))  # 3.0 <class 'float'>