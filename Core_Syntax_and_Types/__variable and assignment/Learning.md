
                           <h1> variables_and_assignment</h1>




# x = 42          # create int object 42, bind the name "x" to it
# y = x           # bind "y" to the SAME object; nothing is copied
# print(x, y)     # -> 42 42
# print(x is y)   # -> True   (same object identity)

# a = [1, 2, 3]
# b = a
# # # # print(id(a) == id(b))   # -> True
# # # # b.append(4)
# # # # print(a)                # -> [1, 2, 3, 4]   <- a "changed" because a and b are the same list

# v = 10
# print(type(v))      # -> <class 'int'>
# v = "now a string"
# print(type(v))      # -> <class 'str'>
# v = [1, 2]
# print(type(v))      # -> <class 'list'>

# print(1 + 2)        # -> 3
# print("1" + "2")    # -> '12'
# print(1 + "2")      # !! TypeError: unsupported operand type(s) for +: 'int' and 'str'

# a = b = c = 0                # chained: all three names -> the same int 0
# x, y = 1, 2                  # tuple unpacking
# x, y = y, x                  # swap, no temp variable needed
# print(x, y)                  # -> 2 1

# first, *rest = [1, 2, 3, 4]  # extended unpacking (Tier 2)
# print(first, rest)           # -> 1 [2, 3, 4]

# n = 5
# n += 3                       # augmented assignment
# print(n)                     # -> 8

# import keyword
# print(keyword.kwlist[:8])
# # -> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await']
# print(keyword.iskeyword("match"))      # -> False  (match is a SOFT keyword)
# print(keyword.issoftkeyword("match"))  # -> True

# x = [1, 2]
# y = x
# del x
# print(y)      # -> [1, 2]   object still alive, y still references it
# print(x)      # !! NameError

# a = [1]; b = a
# b += [2]        # in-place extend -> mutates the shared list
# print(a)        # -> [1, 2]

# a = [1]; b = a
# b = b + [2]     # builds a NEW list and rebinds b
# print(a)        # -> [1]

# big = 2 ** 1000
# print(len(str(big)))     # -> 302     digits. No overflow, ever.

# print(0.1 + 0.2)         # -> 0.30000000000000004    <- floats are binary approximations
# print(1e400)             # -> inf     floats DO overflow, to infinity

# z = 3 + 4j
# print(z.real, z.imag)    # -> 3.0 4.0
# print(abs(z))            # -> 5.0     magnitude
# print(z.conjugate())     # -> (3-4j)

# print(0b1010)      # -> 10    binary
# print(0o17)        # -> 15    octal
# print(0xff)        # -> 255   hex
# print(1_000_000)   # -> 1000000   underscores are ignored, just for humans
# print(int("ff", 16))  # -> 255   parse a string in a given base
# print(bin(10), oct(10), hex(10))  # -> 0b1010 0o12 0xa

# print(7 + 3)     # -> 10     addition
# print(7 - 3)     # -> 4      subtraction
# print(7 * 3)     # -> 21     multiplication
# print(7 / 3)     # -> 2.3333333333333335   TRUE division, ALWAYS returns float
# print(7 // 3)    # -> 2      FLOOR division (rounds toward -infinity)
# print(7 % 3)     # -> 1      modulo (remainder)
# print(7 ** 3)    # -> 343    exponentiation
# print(-7 // 3)   # -> -3     NOT -2!  floor(-2.333) == -3
# print(-7 % 3)    # -> 2      sign follows the DIVISOR in Python
# print(divmod(7, 3))   # -> (2, 1)   quotient and remainder in one call

# print(2 ** 3 ** 2)   # -> 512   ** is RIGHT-associative: 2 ** (3 ** 2) == 2 ** 9
# print(-2 ** 2)       # -> -4    ** binds tighter than unary minus: -(2 ** 2)
# print((-2) ** 2)     # -> 4

# print(0b1100 & 0b1010)   # -> 8    (0b1000)  AND
# print(0b1100 | 0b1010)   # -> 14   (0b1110)  OR
# print(0b1100 ^ 0b1010)   # -> 6    (0b0110)  XOR
# print(~5)                # -> -6   NOT (two's complement: ~n == -n-1)
# print(1 << 4)            # -> 16   left shift  (multiply by 2**4)
# print(256 >> 4)          # -> 16   right shift (floor-divide by 2**4)

# print(abs(-4.5))        # -> 4.5
# print(round(2.675, 2))  # -> 2.67   <- NOT 2.68, see gotcha below
# print(round(2.5))       # -> 2      banker's rounding: ties go to EVEN
# print(round(3.5))       # -> 4
# print(pow(2, 10))       # -> 1024
# print(pow(2, 10, 1000)) # -> 24     (2**10) % 1000, computed efficiently
# print(min(3, 1, 2), max(3, 1, 2), sum([1, 2, 3]))   # -> 1 3 6

# import math
# print(math.floor(-2.3), math.ceil(-2.3))   # -> -3 -2
# print(math.sqrt(16), math.isqrt(17))       # -> 4.0 4        isqrt is exact integer sqrt
# print(math.inf, -math.inf, math.nan)       # -> inf -inf nan
# print(math.isclose(0.1 + 0.2, 0.3))        # -> True   <- how to compare floats
# print(math.gcd(12, 18), math.lcm(4, 6))    # -> 6 12
# print(math.factorial(5))                   # -> 120

# falsy = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), frozenset(), range(0), b""]
# print(any(falsy))     # -> False    not one of them is truthy
# from decimal import Decimal
# print(bool(Decimal("0")))   # -> False

# print(1 and 2)          # -> 2      both truthy -> returns the LAST
# print(0 and 2)          # -> 0      first is falsy -> returns it, 2 never evaluated
# print(1 or 2)           # -> 1      first is truthy -> returns it, 2 never evaluated
# print(0 or 2)           # -> 2
# print(0 or "" or None or "found")   # -> 'found'   first truthy wins
# print(not 5)            # -> False  `not` DOES return a real bool

# x = 1
# print(x == True)      # -> True
# print(x is True)      # -> False   x is int 1, not bool True
# if x: ...             # <- just do this

# String

# s1 = 'single'
# s2 = "double"                      # identical; pick one style per project
# s3 = """multi
# line"""                            # keeps the newline
# s4 = 'He said "hi"'                # no escaping needed
# s5 = "It's fine"
# s6 = 'escaped \' quote and a \\ backslash and a \n newline and a \t tab'
# s7 = r"raw\nstring"                # r prefix: backslashes are literal -> raw\nstring
# s8 = f"formatted {1 + 1}"          # f-string -> 'formatted 2'
# s9 = b"bytes, not str"             # bytes literal (different type!)
# s10 = ("implicit "                 # adjacent literals concatenate at COMPILE time
#        "concatenation")            # -> 'implicit concatenation'
# print(len(s10))                    # -> 22

# # s = "Python"
# # #    012345      forward index
# # #   -654321      negative index

# # print(s[0])       # -> 'P'
# # print(s[-1])      # -> 'n'      last character
# # print(s[1:4])     # -> 'yth'    [start:stop) — stop is EXCLUSIVE
# # print(s[:3])      # -> 'Pyt'    start defaults to 0
# # print(s[3:])      # -> 'hon'    stop defaults to len
# # print(s[:])       # -> 'Python' full copy
# # print(s[::2])     # -> 'Pto'    step 2
# # print(s[::-1])    # -> 'nohtyP' reversed
# # print(s[10:20])   # -> ''       out-of-range SLICES are safe (no error)
# # print(s[10])      # !! IndexError: string index out of range

# # print("ab" + "cd")     # -> 'abcd'
# # print("ab" * 3)        # -> 'ababab'
# # print("-" * 20)        # -> '--------------------'   handy separator
# # print("".join(["a", "b", "c"]))         # -> 'abc'
# # print(", ".join(["a", "b", "c"]))       # -> 'a, b, c'

# # parts = []
# # for i in range(5):
# #     parts.append(str(i))
# # print("".join(parts))    # -> '01234'

# s = "  Hello, World  "

# # case
# print(s.upper())            # -> '  HELLO, WORLD  '
# print(s.lower())            # -> '  hello, world  '
# print("hi there".title())   # -> 'Hi There'
# print("hi there".capitalize())  # -> 'Hi there'
# print("AbC".swapcase())     # -> 'aBc'
# print("Straße".casefold())  # -> 'strasse'   aggressive lowercase for comparisons

# # whitespace / trimming
# print(s.strip())            # -> 'Hello, World'
# print(s.lstrip(), "|")      # -> 'Hello, World  |'
# print(s.rstrip(), "|")      # -> '  Hello, World|'
# print("xxhixx".strip("x"))  # -> 'hi'      strips any of the CHARACTERS given
# print("file.txt".removesuffix(".txt"))    # -> 'file'   (3.9+, use this not strip!)
# print("pre_name".removeprefix("pre_"))    # -> 'name'

# # searching
# print("hello".find("l"))     # -> 2     first index, -1 if absent
# print("hello".rfind("l"))    # -> 3     last index
# print("hello".index("l"))    # -> 2     like find but RAISES ValueError if absent
# print("hello".count("l"))    # -> 2
# print("hello".startswith("he"))          # -> True
# print("hello".endswith((".py", ".txt"))) # -> False   accepts a TUPLE of options
# print("ell" in "hello")      # -> True   simplest membership test

# # splitting and joining
# print("a,b,c".split(","))          # -> ['a', 'b', 'c']
# print("a b  c".split())            # -> ['a', 'b', 'c']  no-arg split collapses whitespace
# print("a,b,c".split(",", 1))       # -> ['a', 'b,c']     maxsplit
# print("a,b,c".rsplit(",", 1))      # -> ['a,b', 'c']     from the right
# print("k=v=w".partition("="))      # -> ('k', '=', 'v=w')  always a 3-tuple
# print("line1\nline2".splitlines()) # -> ['line1', 'line2']

# # replacing
# print("a-b-c".replace("-", "+"))       # -> 'a+b+c'
# print("a-b-c".replace("-", "+", 1))    # -> 'a+b-c'   count limit

# # padding / alignment
# print("5".zfill(3))          # -> '005'
# print("hi".ljust(5, "."))    # -> 'hi...'
# print("hi".rjust(5, "."))    # -> '...hi'
# print("hi".center(6, "*"))   # -> '**hi**'

# # classification (all return bool; all are False for the empty string)
# print("abc".isalpha(), "123".isdigit(), "a1".isalnum())   # -> True True True
# print("  ".isspace(), "Hi".istitle(), "ABC".isupper())    # -> True True True
# print("var_1".isidentifier())      # -> True

# name, score = "Ada", 0.87561
# print(f"{name} scored {score:.1%}")     # -> Ada scored 87.6%
# print(f"{name!r}")                      # -> 'Ada'      !r calls repr()
# print(f"{score=}")                      # -> score=0.87561   self-documenting (3.8+)
# print(f"{42:>8}|")                      # -> '      42|'  right-align in 8 columns
# print(f"{1234567:,}")                   # -> 1,234,567

# 1. Functions with no explicit return
# def f():
#     pass
# print(f())               # -> None

# # 2. Mutating methods return None (they changed the object in place)
# xs = [3, 1, 2]
# print(xs.sort())         # -> None      <- classic bug source
# xs.sort()
# print(xs)                # -> [1, 2, 3]
# print(sorted([3, 1, 2])) # -> [1, 2, 3] sorted() RETURNS a new list

# # 3. Default "nothing was supplied" marker
# def connect(timeout=None):
#     if timeout is None:
#         timeout = 30      # compute a real default at call time
#     return timeout

# # 4. Safe dict lookup
# config = {"host": "localhost"}
# print(config.get("port"))        # -> None
# print(config.get("port", 8080))  # -> 8080

# # to int
# print(int("42"))         # -> 42
# print(int("  42  "))     # -> 42     surrounding whitespace is fine
# print(int("0x1f", 16))   # -> 31     explicit base
# print(int(3.99))         # -> 3      TRUNCATES toward zero, does not round
# print(int(-3.99))        # -> -3
# print(int(True))         # -> 1
# print(int("3.0"))        # !! ValueError: invalid literal for int() with base 10: '3.0'
# print(int(float("3.0"))) # -> 3      two-step for numeric strings with a decimal point

# # to float
# print(float("3.14"))     # -> 3.14
# print(float(7))          # -> 7.0
# print(float("inf"))      # -> inf
# print(float("1e-3"))     # -> 0.001

# # to str
# print(str(42))           # -> '42'
# print(str([1, 2]))       # -> '[1, 2]'
# print(str(None))         # -> 'None'

# # to bool
# print(bool(0), bool(""), bool([]))       # -> False False False
# print(bool("False"))     # -> True   !! any non-empty string is truthy

# # to the container types
# print(list("abc"))               # -> ['a', 'b', 'c']
# print(tuple([1, 2]))             # -> (1, 2)
# print(set([1, 1, 2]))            # -> {1, 2}
# print(dict([("a", 1), ("b", 2)]))# -> {'a': 1, 'b': 2}
# print(list({"a": 1}))            # -> ['a']   iterating a dict gives KEYS
# print(list({"a": 1}.items()))    # -> [('a', 1)]

# # to bytes / from bytes
# print("héllo".encode("utf-8"))          # -> b'h\xc3\xa9llo'
# print(b"h\xc3\xa9llo".decode("utf-8"))  # -> 'héllo'


# x = 5
# print(type(x) is int)         # -> True   exact type, no subclasses
# print(isinstance(x, int))     # -> True   type OR subclass — prefer this
# print(isinstance(x, (int, float)))   # -> True   accepts a tuple
# print(isinstance(True, int))  # -> True   because bool subclasses int

# # Duck typing is usually better than type checking:
# def total(values):
#     return sum(values)        # works for any iterable of numbers

# # When you must check "is it a sequence / iterable":
# from collections.abc import Iterable, Sequence, Mapping
# print(isinstance([1], Iterable), isinstance("s", Sequence), isinstance({}, Mapping))
# # -> True True True

# A full-line comment. Explain WHY, not WHAT.

# x = x + 1            # inline comment: two spaces before #, one space after

# BAD:  x = x + 1    # add one to x        <- restates the code
# GOOD: x = x + 1    # compensate for the exclusive upper bound of range()

# Python has no /* block comment */ syntax.
# Editors comment multiple lines by prefixing each with #.

# """
# A bare string literal like this is NOT a comment — it is an expression statement
# that creates and discards a string. Sometimes used to disable a block, but it
# still gets compiled. Prefer # for commenting out code.
# """


# def clamp(value, low, high):
#     """Return value constrained to the inclusive range [low, high].

#     Args:
#         value: The number to clamp.
#         low: Lower bound, inclusive.
#         high: Upper bound, inclusive.

#     Returns:
#         low if value < low, high if value > high, otherwise value.

#     Raises:
#         ValueError: If low > high.

#     Examples:
#         >>> clamp(5, 0, 10)
#         5
#         >>> clamp(-1, 0, 10)
#         0
#     """
#     if low > high:
#         raise ValueError("low must not exceed high")
#     return max(low, min(value, high))

# print(clamp.__doc__.splitlines()[0])
# # -> Return value constrained to the inclusive range [low, high].
# help(clamp)      # renders the full docstring