# Python Fundamentals: Variables, Types & Core Syntax

> A practical beginner-friendly reference for Python's core syntax.  
> Work through the **Core concepts** first. The **Deeper details** sections are useful reference material—don't feel you need to memorize everything at once.

---

## Learning roadmap

1. [Variables, assignment, and dynamic typing](#1-variables-assignment-and-dynamic-typing)
2. [Numeric types and arithmetic](#2-numeric-types-and-arithmetic)
3. [Booleans and truthiness](#3-booleans-and-truthiness)
4. [Strings](#4-strings)
5. [The `None` value](#5-the-none-value)
6. [Type conversion and type checking](#6-type-conversion-and-type-checking)
7. [Comments and docstrings](#7-comments-and-docstrings)
8. [Practice exercises](#8-practice-exercises)
9. [Quick reference](#9-quick-reference)

### How to use these notes

- **Read:** Understand the explanation before moving on.
- **Run:** Type the examples into a `.py` file or the Python REPL.
- **Predict:** Guess the output before running the code.
- **Practise:** Complete the exercises without immediately looking up the answer.
- **Review:** Return to the common mistakes when something behaves unexpectedly.

### Difficulty guide

- **Core concept** — learn and practise this now.
- **Useful detail** — understand the idea; memorization can wait.
- **Deeper detail** — keep as a reference for later.

---

# 1. Variables, assignment, and dynamic typing

## 1.1 What is a variable?

A variable is a **name that refers to an object**. Assignment with `=` binds a name to an object.

```python
age = 22
name = "Saif"

print(age)
print(name)
```

**Output**
```text
22
Saif
```

Think of a variable name as a label attached to an object. It is not a box that permanently stores one kind of value.

## 1.2 Assigning one variable to another

```python
x = 42
y = x

print(x, y)
```

**Output**
```text
42 42
```

Both names refer to the same integer object. With immutable objects such as integers and strings, this usually feels like ordinary value assignment.

Lists are mutable, so shared references become more visible:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

**Output**
```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

`a` and `b` refer to the same list. Changing that list through `b` is visible through `a` too.

### Reassignment is different from mutation

```python
a = [1, 2, 3]
b = a

b = [9, 9]  # b now refers to a different list

print(a)
print(b)
```

**Output**
```text
[1, 2, 3]
[9, 9]
```

Reassigning `b` does not change the original list.

## 1.3 Dynamic typing

Python is dynamically typed: a name can be rebound to objects of different types.

```python
value = 10
print(type(value))

value = "hello"
print(type(value))

value = [1, 2, 3]
print(type(value))
```

**Output**
```text
<class 'int'>
<class 'str'>
<class 'list'>
```

The object has a type; the variable name does not have a permanent type.

Python is also strongly typed. It does not automatically combine unrelated types in every situation:

```python
print(1 + 2)       # 3
print("1" + "2")   # 12
print(1 + "2")     # TypeError
```

## 1.4 Common assignment forms

```python
# Assign one value to several names
a = b = c = 0

# Assign several values at once
x, y = 1, 2

# Swap two values
x, y = y, x

# Augmented assignment
count = 5
count += 3
print(count)  # 8
```

Extended unpacking is useful when you want to collect the remaining values:

```python
first, *rest = [1, 2, 3, 4]

print(first)  # 1
print(rest)   # [2, 3, 4]
```

## 1.5 Naming rules and conventions

**Rules:**

- A name may contain letters, digits, and underscores.
- A name cannot begin with a digit.
- A name cannot be a Python keyword.
- Names are case-sensitive: `score` and `Score` are different names.

**PEP 8 conventions:**

```python
user_name = "Ada"             # variables and functions: snake_case
MAX_RETRIES = 3               # constants: UPPER_SNAKE_CASE

class UserProfile:
    pass                      # classes: PascalCase
```

A leading underscore, such as `_internal_value`, signals that a name is intended for internal use by convention.

To inspect Python keywords:

```python
import keyword

print(keyword.kwlist)
print(keyword.iskeyword("class"))  # True
```

## 1.6 Common mistakes and useful details

### `is` versus `==`

- `==` asks whether two values are equal.
- `is` asks whether two names refer to the exact same object.

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: same contents
print(a is b)  # False: different list objects
```

Use `is` for identity checks, especially `value is None`. Use `==` to compare ordinary values.

### A common mutable-list trap

```python
# Avoid this: each row refers to the same list
grid = [[0] * 3] * 3
grid[0][0] = 9
print(grid)
```

All three rows change because they are references to one inner list.

Create separate rows with a comprehension:

```python
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 9
print(grid)
```

**Output**
```text
[[9, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### `del` removes a name binding

```python
x = [1, 2]
y = x

del x
print(y)  # [1, 2]
```

Deleting `x` does not delete the list while `y` still refers to it.

### Deeper detail: `+=` and `+` with lists

```python
a = [1]
b = a
b += [2]
print(a)  # [1, 2]
```

For lists, `+=` usually updates the existing list. By contrast:

```python
a = [1]
b = a
b = b + [2]
print(a)  # [1]
```

`+` creates a new list and rebinds `b`.

---

# 2. Numeric types and arithmetic

## 2.1 The three built-in numeric types

| Type | Example | What it represents |
|---|---|---|
| `int` | `42`, `-7`, `0` | Integers |
| `float` | `3.14`, `2.0`, `1e-9` | Floating-point numbers |
| `complex` | `3 + 4j` | Numbers with real and imaginary parts |

Python integers can grow very large, limited mainly by available memory:

```python
big_number = 2 ** 1000
print(len(str(big_number)))  # 302
```

Floats have finite precision and can overflow to infinity:

```python
print(0.1 + 0.2)  # 0.30000000000000004
print(1e400)      # inf (on typical Python float implementations)
```

Complex numbers:

```python
z = 3 + 4j

print(z.real)        # 3.0
print(z.imag)        # 4.0
print(abs(z))        # 5.0
print(z.conjugate()) # (3-4j)
```

## 2.2 Number bases and underscores

Python supports binary, octal, and hexadecimal integer literals:

```python
print(0b1010)  # 10: binary
print(0o17)    # 15: octal
print(0xff)    # 255: hexadecimal
```

Underscores can make large numbers easier to read:

```python
population = 1_000_000
print(population)  # 1000000
```

Convert an integer to a string in a chosen base:

```python
print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(10))  # 0xa
print(int("ff", 16))  # 255
```

## 2.3 Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---:|---:|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | True division | `7 / 3` | `2.333...` |
| `//` | Floor division | `7 // 3` | `2` |
| `%` | Remainder | `7 % 3` | `1` |
| `**` | Exponentiation | `7 ** 3` | `343` |

Important: `/` returns a float. `//` rounds down toward negative infinity:

```python
print(7 / 3)    # 2.3333333333333335
print(7 // 3)   # 2
print(-7 // 3)  # -3
print(-7 % 3)   # 2
print(divmod(7, 3))  # (2, 1)
```

## 2.4 Operator precedence

A simplified order, from higher to lower:

1. Parentheses
2. Exponentiation `**`
3. Unary `+x` and `-x`
4. `*`, `/`, `//`, `%`
5. `+`, `-`

When an expression is hard to read, use parentheses.

```python
print(2 ** 3 ** 2)  # 512: 2 ** (3 ** 2)
print(-2 ** 2)      # -4: -(2 ** 2)
print((-2) ** 2)    # 4
```

## 2.5 Useful built-in functions

```python
print(abs(-4.5))              # 4.5
print(round(3.14159, 2))      # 3.14
print(pow(2, 10))             # 1024
print(min(3, 1, 2))           # 1
print(max(3, 1, 2))           # 3
print(sum([1, 2, 3]))         # 6
```

The `math` module provides more numeric tools:

```python
import math

print(math.floor(2.8))       # 2
print(math.ceil(2.2))        # 3
print(math.sqrt(16))         # 4.0
print(math.isqrt(17))        # 4: integer square root
print(math.gcd(12, 18))      # 6
print(math.lcm(4, 6))        # 12
print(math.factorial(5))     # 120
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

## 2.6 Floating-point precision

A computer stores ordinary floats in binary. Many decimal fractions cannot be represented exactly.

```python
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False
```

For approximate comparisons, use `math.isclose()`:

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))  # True
```

For decimal arithmetic such as money, use `Decimal` with strings:

```python
from decimal import Decimal

total = Decimal("0.1") + Decimal("0.2")
print(total)  # 0.3
```

## 2.7 Understanding `round()`

Python's `round()` uses **ties-to-even** rounding for exact halfway cases:

```python
print(round(0.5))  # 0
print(round(1.5))  # 2
print(round(2.5))  # 2
print(round(3.5))  # 4
```

Also, `round(2.675, 2)` can produce `2.67` because the stored float is slightly below the decimal value `2.675`.

For predictable decimal rounding:

```python
from decimal import Decimal, ROUND_HALF_UP

amount = Decimal("2.675")
rounded = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(rounded)  # 2.68
```

## 2.8 Deeper numeric details

Bitwise operators work on the binary representation of integers:

| Operator | Meaning |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left shift |
| `>>` | Right shift |

```python
print(0b1100 & 0b1010)  # 8
print(0b1100 | 0b1010)  # 14
print(0b1100 ^ 0b1010)  # 6
print(~5)               # -6
print(1 << 4)           # 16
print(256 >> 4)         # 16
```

Other details worth knowing later:

```python
import math

number = float("nan")
print(math.isnan(number))  # True
print(number == number)    # False
print(isinstance(True, int))  # True
print(True + True)            # 2
```

`bool` is a subclass of `int`, although you should generally treat booleans as logical values.

---

# 3. Booleans and truthiness

## 3.1 The `bool` type

A Boolean represents one of two values: `True` or `False`.

```python
is_learning = True
is_finished = False

print(type(is_learning))  # <class 'bool'>
print(int(True))          # 1
print(int(False))         # 0
```

Comparison operators produce Boolean results:

```python
print(3 == 3.0)  # True
print(1 != 2)    # True
print(1 < 2)     # True
print(1 < 2 < 3) # True
```

Use `==` for value equality. Use `is` for object identity.

## 3.2 Truthy and falsy values

Python allows many values in an `if` condition. Some values are **falsy**; most others are **truthy**.

Common falsy values:

```python
False
None
0
0.0
0j
""
[]
()
{}
set()
```

Examples:

```python
if "":
    print("This will not run")

if "Python":
    print("This will run")
```

A Pythonic way to check whether a collection is empty:

```python
items = []

if not items:
    print("The collection is empty")
```

This works for empty lists, tuples, dictionaries, sets, and other objects with a false Boolean value.

## 3.3 `and`, `or`, and `not`

- `and` returns the first falsy operand, or the last operand if all are truthy.
- `or` returns the first truthy operand, or the last operand if all are falsy.
- `not` always returns a Boolean.

```python
print(1 and 2)  # 2
print(0 and 2)  # 0
print(1 or 2)   # 1
print(0 or 2)   # 2
print(not 5)    # False
```

### Short-circuit evaluation

Python may skip evaluating the right-hand side:

```python
def do_something():
    print("Function called")
    return True

flag = False

if flag and do_something():
    print("Inside if")
```

Nothing is printed because `flag` is false, so `do_something()` is not called.

Short-circuiting can also protect an operation:

```python
numbers = []

if numbers and numbers[0] > 0:
    print("First number is positive")
```

Python never evaluates `numbers[0]` when the list is empty.

## 3.4 A common default-value mistake

This pattern is convenient:

```python
def greet(name=None):
    name = name or "Guest"
    return f"Hello, {name}"
```

But it replaces every falsy value, including an empty string:

```python
print(greet(""))  # Hello, Guest
```

If only `None` should trigger the default, write:

```python
def greet(name=None):
    if name is None:
        name = "Guest"
    return f"Hello, {name}"
```

Now an empty string remains an empty string.

## 3.5 `and`/`or` versus `&`/`|`

`and` and `or` are logical operators with short-circuit behavior. `&` and `|` are bitwise operators and do not short-circuit.

```python
print(True and False)  # False
print(True & False)    # False

print(1 and 2)         # 2
print(1 & 2)           # 0
```

For normal conditions, use `and`, `or`, and `not`.

---

# 4. Strings

## 4.1 What is a string?

A string (`str`) is an immutable sequence of text characters represented as Unicode code points.

```python
single = 'Hello'
double = "Python"
multiline = """This is
a multiline string."""

print(single)
print(double)
print(multiline)
```

Single and double quotes work the same way. Choose a consistent style.

## 4.2 Useful string forms

```python
message = "It's fine"
quote = 'She said "hello"'

escaped = "First line\nSecond line"
raw = r"C:\new\table"
formatted = f"Two plus two is {2 + 2}"

print(escaped)
print(raw)
print(formatted)
```

- `\n` means newline.
- `\t` means tab.
- `r"..."` creates a raw string, useful for regular expressions and Windows paths.
- `f"..."` creates a formatted string.

Bytes (`bytes`) are different from strings:

```python
text = "hello"
data = b"hello"

print(type(text))  # <class 'str'>
print(type(data))  # <class 'bytes'>
```

## 4.3 Indexing and slicing

Python strings use zero-based indexing.

```python
word = "Python"
#       012345

print(word[0])    # P
print(word[-1])   # n
print(word[1:4])  # yth
print(word[:3])   # Pyt
print(word[3:])   # hon
print(word[::2])  # Pto
print(word[::-1]) # nohtyP
```

The stop position in a slice is **exclusive**: `word[1:4]` includes indexes 1, 2, and 3.

An out-of-range index raises `IndexError`, but an out-of-range slice is safe:

```python
print(word[10:20])  # ""
# print(word[10])   # IndexError
```

## 4.4 Joining and concatenating strings

```python
print("Hello" + " " + "Python")  # Hello Python
print("ha" * 3)                  # hahaha

letters = ["a", "b", "c"]
print("".join(letters))          # abc
print(", ".join(letters))        # a, b, c
```

When building a large string in a loop, collect pieces in a list and join them:

```python
parts = []

for number in range(5):
    parts.append(str(number))

result = "".join(parts)
print(result)  # 01234
```

## 4.5 Essential string methods

String methods return new strings because strings are immutable.

### Changing letter case

```python
text = "Hello, World"

print(text.upper())       # HELLO, WORLD
print(text.lower())       # hello, world
print(text.title())       # Hello, World
print(text.capitalize())  # Hello, world
print("AbC".swapcase())   # aBc
print("Straße".casefold()) # strasse
```

### Removing whitespace or prefixes/suffixes

```python
text = "  Hello  "

print(text.strip())   # "Hello"
print(text.lstrip())  # "Hello  "
print(text.rstrip())  # "  Hello"

print("file.txt".removesuffix(".txt"))  # file
print("pre_name".removeprefix("pre_"))  # name
```

**Important:** `strip(chars)` removes any matching characters from the ends; it does not remove an exact substring.

```python
print("test.txt".strip(".txt"))        # "es" — surprising!
print("test.txt".removesuffix(".txt")) # "test" — intended result
```

### Searching and checking

```python
text = "hello"

print(text.find("l"))       # 2; -1 if not found
print(text.rfind("l"))      # 3; search from the right
print(text.index("e"))      # 1; raises ValueError if not found
print(text.count("l"))      # 2
print(text.startswith("he")) # True
print(text.endswith("lo"))   # True
print("ell" in text)         # True
```

### Splitting and partitioning

```python
print("a,b,c".split(","))       # ['a', 'b', 'c']
print("a b  c".split())         # ['a', 'b', 'c']
print("a,b,c".split(",", 1))    # ['a', 'b,c']
print("a,b,c".rsplit(",", 1))   # ['a,b', 'c']
print("key=value".partition("=")) # ('key', '=', 'value')
print("one\ntwo".splitlines())  # ['one', 'two']
```

`split()` separates text into a list. `partition()` always returns a three-item tuple: the part before the separator, the separator, and the part after it.

### Replacing and aligning

```python
print("a-b-c".replace("-", "+"))     # a+b+c
print("a-b-c".replace("-", "+", 1))  # a+b-c

print("5".zfill(3))       # 005
print("hi".ljust(5, ".")) # hi...
print("hi".rjust(5, ".")) # ...hi
print("hi".center(6, "*")) # **hi**
```

### Checking string contents

```python
print("abc".isalpha())       # True
print("123".isdigit())       # True
print("a1".isalnum())        # True
print("  ".isspace())        # True
print("Hello".istitle())     # True
print("ABC".isupper())       # True
print("var_1".isidentifier()) # True
```

These checks return `False` for an empty string.

## 4.6 F-strings

F-strings are a readable way to insert values into strings:

```python
name = "Ada"
score = 0.87561

print(f"{name} scored {score:.1%}")  # Ada scored 87.6%
print(f"{name!r}")                   # 'Ada'
print(f"{score=}")                   # score=0.87561
print(f"{42:>8}|")                   #       42|
print(f"{1234567:,}")                # 1,234,567
```

- `:.1%` formats a number as a percentage with one decimal place.
- `!r` uses `repr()`.
- `:>8` right-aligns within eight spaces.
- `:,` adds thousands separators.

## 4.7 String gotchas

Strings cannot be changed in place:

```python
text = "hello"
# text[0] = "H"  # TypeError

text = "H" + text[1:]
print(text)  # Hello
```

`len()` counts Unicode code points, not necessarily user-perceived characters:

```python
print(len("café"))  # 4
print(len("👍"))    # 1
```

Some emoji and accented characters are made from multiple code points. Unicode normalization may be needed when comparing user-entered text.

---

# 5. The `None` value

## 5.1 What is `None`?

`None` represents the absence of a value. It is not the same as `0`, `False`, or an empty string.

```python
result = None

print(result)       # None
print(type(result)) # <class 'NoneType'>
print(result is None) # True
print(bool(result)) # False
```

There is only one `None` object, so use `is` and `is not` to check for it.

## 5.2 Where does `None` appear?

### A function with no explicit return

```python
def say_hello():
    print("Hello")

result = say_hello()
print(result)  # None
```

The function prints a message but does not return a value.

### Methods that modify an object

```python
numbers = [3, 1, 2]

result = numbers.sort()
print(result)   # None
print(numbers)  # [1, 2, 3]
```

`list.sort()` changes the existing list. `sorted()` returns a new sorted list:

```python
print(sorted([3, 1, 2]))  # [1, 2, 3]
```

### Optional arguments and dictionary lookups

```python
def connect(timeout=None):
    if timeout is None:
        timeout = 30
    return timeout

config = {"host": "localhost"}

print(config.get("port"))       # None
print(config.get("port", 8080)) # 8080
```

## 5.3 Correctly checking for `None`

```python
value = None

if value is None:
    print("No value supplied")

if value is not None:
    print("A value is available")
```

Avoid `if not value` when `0`, `""`, or `[]` might be valid values. Those are falsy too.

## 5.4 The mutable default argument trap

Default argument values are evaluated once when the function is defined—not every time it is called.

**Problematic version:**

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item("apple"))  # ['apple']
print(add_item("pear"))   # ['apple', 'pear']
```

The same list is reused between calls.

**Safer version:**

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []

    bucket.append(item)
    return bucket

print(add_item("apple"))  # ['apple']
print(add_item("pear"))   # ['pear']
```

## 5.5 Remember to return a result

```python
def double(number):
    number * 2  # The result is calculated but not returned

print(double(5))  # None
```

Correct version:

```python
def double(number):
    return number * 2

print(double(5))  # 10
```

`print()` displays something. `return` sends a value back to the caller.

---

# 6. Type conversion and type checking

## 6.1 Explicit type conversion

Python provides built-in functions to convert values.

### Convert to `int`

```python
print(int("42"))       # 42
print(int("  42  "))   # 42
print(int(3.99))       # 3
print(int(-3.99))      # -3
print(int(True))       # 1
```

`int()` truncates a float toward zero; it does not round.

A string containing a decimal point cannot be converted directly to an integer:

```python
# int("3.0")  # ValueError
print(int(float("3.0")))  # 3
```

### Convert to `float`

```python
print(float("3.14"))  # 3.14
print(float(7))       # 7.0
print(float("1e-3"))  # 0.001
```

### Convert to `str`

```python
print(str(42))       # '42'
print(str([1, 2]))   # '[1, 2]'
print(str(None))     # 'None'
```

### Convert to `bool`

```python
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool("False")) # True
```

A non-empty string is truthy—even if its contents spell `"False"`.

### Convert to collection types

```python
print(list("abc"))              # ['a', 'b', 'c']
print(tuple([1, 2]))            # (1, 2)
print(set([1, 1, 2]))           # {1, 2}
print(dict([("a", 1), ("b", 2)])) # {'a': 1, 'b': 2}
```

Iterating over a dictionary gives its keys:

```python
data = {"name": "Ada", "age": 30}

print(list(data))         # ['name', 'age']
print(list(data.items())) # [('name', 'Ada'), ('age', 30)]
```

## 6.2 Converting between strings and bytes

Text is encoded into bytes and decoded back into text:

```python
text = "héllo"

encoded = text.encode("utf-8")
print(encoded)

decoded = encoded.decode("utf-8")
print(decoded)
```

Use the same compatible encoding when decoding data.

## 6.3 Implicit numeric conversion

Python sometimes promotes numeric values to a wider numeric type:

```python
print(1 + 2.0)       # 3.0
print(True + 1.5)    # 2.5
print((1 + 2j) + 3)  # (4+2j)
```

A simplified promotion order is:

`bool → int → float → complex`

## 6.4 Checking types

Use `type()` to inspect an object's exact type:

```python
value = 5
print(type(value))  # <class 'int'>
```

Use `isinstance()` when checking whether a value belongs to a type or its subclasses:

```python
print(isinstance(5, int))             # True
print(isinstance(5, (int, float)))    # True
print(isinstance(True, int))          # True
```

Usually, `isinstance()` is preferable to comparing `type(value)` directly.

Python code often uses **duck typing**: instead of asking exactly what type an object is, it tries to use the behavior it needs.

```python
def total(values):
    return sum(values)

print(total([1, 2, 3]))  # 6
print(total((4, 5)))     # 9
```

## 6.5 Handling conversion errors

Conversion can fail. Use `try` and `except` when invalid input is expected:

```python
def to_int(value, default=None):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

print(to_int("42"))      # 42
print(to_int("hello"))   # None
print(to_int(None, 0))   # 0
```

## 6.6 `str()` versus `repr()`

- `str()` aims to produce readable text for people.
- `repr()` aims to produce an unambiguous representation useful to developers.

```python
print(str("hello"))   # hello
print(repr("hello"))  # 'hello'
```

---

# 7. Comments and docstrings

## 7.1 Comments

Comments explain code to people reading it. Prefer explaining **why** something is done when the reason is not obvious.

```python
# Compensate for range() excluding its stop value.
last_index = len(items) - 1
```

Avoid comments that simply repeat the code:

```python
# Not very useful:
count = count + 1  # Add one to count
```

Python uses `#` for comments. It does not have a special `/* ... */` block-comment syntax.

## 7.2 What is a docstring?

A docstring is a string literal placed as the first statement in a module, function, class, or method. Python stores it in the object's `__doc__` attribute. Tools such as `help()` can display it.

```python
def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

print(greet.__doc__)
help(greet)
```

## 7.3 Writing a useful docstring

A common format is Google style:

```python
def clamp(value, low, high):
    """Return value limited to the inclusive range from low to high.

    Args:
        value: The number to limit.
        low: The lower boundary.
        high: The upper boundary.

    Returns:
        The limited value.

    Raises:
        ValueError: If low is greater than high.

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-1, 0, 10)
        0
    """
    if low > high:
        raise ValueError("low must not exceed high")

    return max(low, min(value, high))
```

A good docstring should explain:

- What the function does.
- What arguments it expects.
- What it returns.
- Which errors it may raise.
- Examples, when they make usage clearer.

## 7.4 Docstring conventions

- Use triple double quotes: `"""..."""`.
- Put the docstring immediately after the `def`, `class`, or module declaration.
- Start with a short summary.
- For a longer docstring, leave a blank line after the summary.
- Keep the description accurate as the code changes.

This is a docstring:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

This is not a docstring because another statement comes first:

```python
def add(a, b):
    result = a + b
    """This is just a string expression, not the function docstring."""
    return result
```

## 7.5 Testing examples with doctest

Doctest can execute examples written in a docstring and compare the actual output with the expected output.

Save this in `example.py`:

```python
def add(a, b):
    """Return the sum of two numbers.

    Examples:
        >>> add(2, 3)
        5
        >>> add(10, 5)
        15
    """
    return a + b
```

Run it from the directory containing the file:

```powershell
py -m doctest -v example.py
```

If the actual output matches the expected output, the test passes.

Doctest is useful for small examples and documentation. Larger projects often use tools such as `unittest` or `pytest`.

## 7.6 Other docstring styles

| Style | Common structure |
|---|---|
| Google | `Args:`, `Returns:`, `Raises:` |
| NumPy | `Parameters` with underlined headings |
| reStructuredText / Sphinx | `:param name:`, `:returns:` |

Pick one style and use it consistently in a project.

---

# 8. Practice exercises

Try these without looking at the solutions first. Run your code and check the result.

## Exercise 1 — Variables

What does this code print?

```python
x = 10
y = x
x = 20

print(y)
```

## Exercise 2 — Shared lists

Predict the output:

```python
first = [1, 2]
second = first
second.append(3)

print(first)
```

## Exercise 3 — Arithmetic

What are the results of these expressions?

```python
print(7 / 2)
print(7 // 2)
print(-7 // 2)
print(7 % 2)
```

## Exercise 4 — Truthiness

Which of these values are falsy?

```python
values = [0, 1, "", "0", [], [0], None, False]

for value in values:
    print(repr(value), bool(value))
```

## Exercise 5 — Strings

Given:

```python
path = "/home/user/report.final.txt"
```

Extract the filename and extension so the result is:

```python
("report.final", ".txt")
```

Hint: Try `rsplit()`.

## Exercise 6 — `None` and return

What does this function return?

```python
def multiply(a, b):
    print(a * b)

result = multiply(3, 4)
print(result)
```

How would you change it so `result` contains `12`?

## Exercise 7 — Type conversion

Why does this work, but the next line fail?

```python
print(int("42"))
print(int("4.2"))
```

## Exercise 8 — Docstrings

Write a documented function called `is_even(number)` that:

- Accepts an integer.
- Returns `True` if it is even.
- Returns `False` otherwise.
- Includes at least two doctest examples.

Run your tests with:

```powershell
py -m doctest -v your_file.py
```

---

# 9. Quick reference

## Core operators

| Purpose | Syntax |
|---|---|
| Assignment | `=` |
| Equality | `==` |
| Not equal | `!=` |
| Identity | `is`, `is not` |
| Addition / subtraction | `+`, `-` |
| Multiplication / division | `*`, `/` |
| Floor division / remainder | `//`, `%` |
| Exponentiation | `**` |
| Logical operators | `and`, `or`, `not` |
| Membership | `in`, `not in` |

## Useful built-ins

| Function | Purpose |
|---|---|
| `print()` | Display output |
| `type()` | Inspect an object's type |
| `isinstance()` | Check type or subclass |
| `id()` | Inspect object identity |
| `len()` | Get the number of items |
| `int()` | Convert to integer |
| `float()` | Convert to float |
| `str()` | Convert to string |
| `bool()` | Convert to Boolean |
| `round()` | Round a number |
| `abs()` | Absolute value |
| `sum()` | Add values |
| `min()` / `max()` | Find smallest / largest |
| `help()` | Display documentation |

## Before moving on

You should be comfortable with:

- [ ] Creating variables and assigning values.
- [ ] Understanding that names refer to objects.
- [ ] Recognizing `int`, `float`, `complex`, `bool`, `str`, and `None`.
- [ ] Using arithmetic and comparison operators.
- [ ] Understanding truthy and falsy values.
- [ ] Indexing, slicing, and using common string methods.
- [ ] Converting between common types.
- [ ] Explaining the difference between `print()` and `return`.
- [ ] Writing a simple function docstring.
- [ ] Running a basic doctest.

---

**Keep practising:** You do not need to memorize every advanced detail on the first read. Focus on understanding the core concepts, writing small programs, and learning from the mistakes you encounter.
