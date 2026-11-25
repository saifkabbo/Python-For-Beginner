1. Variables, assignment, dynamic typing
What it is
A variable in Python is a name bound to an object. Assignment does not copy a value into a box — it makes a name point at an object that lives somewhere in memory.

x = 42          # create int object 42, bind the name "x" to it
y = x           # bind "y" to the SAME object; nothing is copied
print(x, y)     # -> 42 42
print(x is y)   # -> True   (same object identity)
id() shows the identity (in CPython, the memory address):

a = [1, 2, 3]
b = a
print(id(a) == id(b))   # -> True
b.append(4)
print(a)                # -> [1, 2, 3, 4]   <- a "changed" because a and b are the same list
Rebinding a name never affects other names:

a = [1, 2, 3]
b = a
b = [9, 9]      # REBIND b to a new list. a is untouched.
print(a)        # -> [1, 2, 3]
Dynamic typing
The object has a type; the name does not. A name can point at anything, and can be re-pointed at something of a different type.

v = 10
print(type(v))      # -> <class 'int'>
v = "now a string"
print(type(v))      # -> <class 'str'>
v = [1, 2]
print(type(v))      # -> <class 'list'>
Python is dynamically typed (types checked at runtime) but also strongly typed (it will not silently coerce unrelated types):

print(1 + 2)        # -> 3
print("1" + "2")    # -> '12'
print(1 + "2")      # !! TypeError: unsupported operand type(s) for +: 'int' and 'str'
Compare with JavaScript, which is dynamically and weakly typed (1 + "2" === "12").

Assignment forms
a = b = c = 0                # chained: all three names -> the same int 0
x, y = 1, 2                  # tuple unpacking
x, y = y, x                  # swap, no temp variable needed
print(x, y)                  # -> 2 1

first, *rest = [1, 2, 3, 4]  # extended unpacking (Tier 2)
print(first, rest)           # -> 1 [2, 3, 4]

n = 5
n += 3                       # augmented assignment
print(n)                     # -> 8
Naming rules and conventions (PEP 8)
snake_case_for_variables_and_functions = 1
CONSTANTS_IN_UPPER_SNAKE = 3.14159
class PascalCaseForClasses: ...
_internal_use = "leading underscore: 'private by convention'"
__name_mangled = "double leading underscore inside a class: name mangling"
trailing_underscore_ = "avoid clashing with a keyword, e.g. class_, id_, list_"
Names may contain letters, digits and _, but cannot start with a digit and cannot be a keyword.

import keyword
print(keyword.kwlist[:8])
# -> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await']
print(keyword.iskeyword("match"))      # -> False  (match is a SOFT keyword)
print(keyword.issoftkeyword("match"))  # -> True
Gotcha — small integer and string caching. CPython pre-creates the ints -5..256 and interns some short strings. So is sometimes "works" for equality by accident:

a = 256; b = 256
print(a is b)     # -> True   (cached)
a = 257; b = 257
print(a is b)     # -> may be True in a script (compiler folds constants), False in the REPL
Never use is to compare values. Use is only for None, True, False, and sentinel objects. Use == for values.

Gotcha — the mutable alias trap. The single most common beginner bug:

grid = [[0] * 3] * 3     # THREE REFERENCES TO ONE LIST
grid[0][0] = 9
print(grid)              # -> [[9, 0, 0], [9, 0, 0], [9, 0, 0]]

grid = [[0] * 3 for _ in range(3)]   # correct: three distinct lists
grid[0][0] = 9
print(grid)              # -> [[9, 0, 0], [0, 0, 0], [0, 0, 0]]
Gotcha — deleting a name. del x unbinds the name, it does not "free memory" directly. The object is collected when its last reference goes away.

x = [1, 2]
y = x
del x
print(y)      # -> [1, 2]   object still alive, y still references it
print(x)      # !! NameError
Interview note. "What's the difference between is and ==?" is the entry-level probe; the senior version is "explain what happens in memory when you write b = a for a list, and what b += [1] does versus b = b + [1]."

a = [1]; b = a
b += [2]        # in-place extend -> mutates the shared list
print(a)        # -> [1, 2]

a = [1]; b = a
b = b + [2]     # builds a NEW list and rebinds b
print(a)        # -> [1]
The reason: += on a list calls __iadd__ (in-place), + calls __add__ (new object).

2. Numeric types and arithmetic operators
The three built-in numeric types
Type	Literal	Notes
int	42, -7, 0, 1_000_000	Arbitrary precision — no overflow, limited only by RAM
float	3.14, 1e-9, 2.0	IEEE-754 double, 64-bit, ~15–17 significant digits
complex	3+4j, complex(3, 4)	Real + imaginary, both stored as floats
big = 2 ** 1000
print(len(str(big)))     # -> 302     digits. No overflow, ever.

print(0.1 + 0.2)         # -> 0.30000000000000004    <- floats are binary approximations
print(1e400)             # -> inf     floats DO overflow, to infinity

z = 3 + 4j
print(z.real, z.imag)    # -> 3.0 4.0
print(abs(z))            # -> 5.0     magnitude
print(z.conjugate())     # -> (3-4j)
Integer literals in other bases, and readability underscores
print(0b1010)      # -> 10    binary
print(0o17)        # -> 15    octal
print(0xff)        # -> 255   hex
print(1_000_000)   # -> 1000000   underscores are ignored, just for humans
print(int("ff", 16))  # -> 255   parse a string in a given base
print(bin(10), oct(10), hex(10))  # -> 0b1010 0o12 0xa
Arithmetic operators
print(7 + 3)     # -> 10     addition
print(7 - 3)     # -> 4      subtraction
print(7 * 3)     # -> 21     multiplication
print(7 / 3)     # -> 2.3333333333333335   TRUE division, ALWAYS returns float
print(7 // 3)    # -> 2      FLOOR division (rounds toward -infinity)
print(7 % 3)     # -> 1      modulo (remainder)
print(7 ** 3)    # -> 343    exponentiation
print(-7 // 3)   # -> -3     NOT -2!  floor(-2.333) == -3
print(-7 % 3)    # -> 2      sign follows the DIVISOR in Python
print(divmod(7, 3))   # -> (2, 1)   quotient and remainder in one call
Precedence, highest first: ** → unary -x → * / // % → + -. Use parentheses when in doubt; they cost nothing.

print(2 ** 3 ** 2)   # -> 512   ** is RIGHT-associative: 2 ** (3 ** 2) == 2 ** 9
print(-2 ** 2)       # -> -4    ** binds tighter than unary minus: -(2 ** 2)
print((-2) ** 2)     # -> 4
Bitwise operators (integers)
print(0b1100 & 0b1010)   # -> 8    (0b1000)  AND
print(0b1100 | 0b1010)   # -> 14   (0b1110)  OR
print(0b1100 ^ 0b1010)   # -> 6    (0b0110)  XOR
print(~5)                # -> -6   NOT (two's complement: ~n == -n-1)
print(1 << 4)            # -> 16   left shift  (multiply by 2**4)
print(256 >> 4)          # -> 16   right shift (floor-divide by 2**4)
Useful numeric built-ins and helpers
print(abs(-4.5))        # -> 4.5
print(round(2.675, 2))  # -> 2.67   <- NOT 2.68, see gotcha below
print(round(2.5))       # -> 2      banker's rounding: ties go to EVEN
print(round(3.5))       # -> 4
print(pow(2, 10))       # -> 1024
print(pow(2, 10, 1000)) # -> 24     (2**10) % 1000, computed efficiently
print(min(3, 1, 2), max(3, 1, 2), sum([1, 2, 3]))   # -> 1 3 6

import math
print(math.floor(-2.3), math.ceil(-2.3))   # -> -3 -2
print(math.sqrt(16), math.isqrt(17))       # -> 4.0 4        isqrt is exact integer sqrt
print(math.inf, -math.inf, math.nan)       # -> inf -inf nan
print(math.isclose(0.1 + 0.2, 0.3))        # -> True   <- how to compare floats
print(math.gcd(12, 18), math.lcm(4, 6))    # -> 6 12
print(math.factorial(5))                   # -> 120
Gotcha — floats are not decimals. 0.1 cannot be represented exactly in binary, the same way 1/3 cannot be written exactly in decimal.

print(0.1 + 0.2 == 0.3)                  # -> False
print(math.isclose(0.1 + 0.2, 0.3))      # -> True     <- do this instead
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))   # -> Decimal('0.3')   <- or this, for money
Never store money as float. Use decimal.Decimal or integer cents. (Tier 2 covers decimal and fractions properly.)

Gotcha — round() does banker's rounding, not the "always round .5 up" you learned in school. round(0.5) == 0, round(1.5) == 2, round(2.5) == 2. This is deliberate: it avoids statistical bias when summing many rounded values. And round(2.675, 2) == 2.67 because 2.675 is actually stored as 2.67499999999999982....

Gotcha — nan is not equal to itself.

n = float("nan")
print(n == n)             # -> False
print(math.isnan(n))      # -> True    <- the correct test
print([n] == [n])         # -> True    !! list comparison checks identity first
Gotcha — bool is a subclass of int.

print(isinstance(True, int))   # -> True
print(True + True)             # -> 2
print(sum([True, False, True]))# -> 2      (a genuinely useful idiom for counting)
Interview note. Expect: "Why is 0.1 + 0.2 != 0.3?" — answer with binary floating point and IEEE-754, then immediately name the fixes (math.isclose, Decimal, integer cents). A follow-up is often "how would you store currency in a database?" — integer minor units. Also common: "what does -7 // 3 give and why?" — floor semantics, and the invariant a == (a // b) * b + (a % b) holds for all ints.

3. Booleans, truthiness, short-circuit and/or
The bool type
print(True, False)              # -> True False
print(type(True))               # -> <class 'bool'>
print(int(True), int(False))    # -> 1 0
Comparison operators produce booleans
print(3 == 3.0)     # -> True    == compares VALUE (across numeric types)
print(3 is 3.0)     # -> False   is compares IDENTITY (and gives a SyntaxWarning here)
print(1 != 2)       # -> True
print(1 < 2 < 3)    # -> True    CHAINED comparison: (1 < 2) and (2 < 3), 2 evaluated once
print(1 < 2 > 0)    # -> True    legal but confusing; avoid
Truthiness — what counts as false
Every object can be used in a boolean context. These are falsy; everything else is truthy:

falsy = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), frozenset(), range(0), b""]
print(any(falsy))     # -> False    not one of them is truthy
from decimal import Decimal
print(bool(Decimal("0")))   # -> False
An object controls its own truthiness via __bool__, falling back to __len__:

class Basket:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)

print(bool(Basket([])))       # -> False   (len == 0)
print(bool(Basket(["a"])))    # -> True
Idiomatic style:

items = []
if not items:            # GOOD — pythonic
    print("empty")
if len(items) == 0:      # ok, but noisier
    ...
if items == []:          # bad — breaks for tuples, sets, custom types
    ...
and / or short-circuit and return operands, not booleans
This surprises people: and/or do not return True/False, they return one of the operands.

print(1 and 2)          # -> 2      both truthy -> returns the LAST
print(0 and 2)          # -> 0      first is falsy -> returns it, 2 never evaluated
print(1 or 2)           # -> 1      first is truthy -> returns it, 2 never evaluated
print(0 or 2)           # -> 2
print(0 or "" or None or "found")   # -> 'found'   first truthy wins
print(not 5)            # -> False  `not` DOES return a real bool
Short-circuiting is a control-flow tool — the right side may never run:

def expensive():
    print("ran!")
    return True

flag = False
if flag and expensive():   # expensive() never called
    ...

user = None
name = user and user.name          # -> None, no AttributeError
name = (user.name if user else "anonymous")

# guard against division by zero / index errors
xs = []
if xs and xs[0] > 0:               # xs[0] never evaluated when xs is empty
    ...
The or default-value idiom, and its trap:

def greet(name=None):
    name = name or "guest"      # convenient...
    return f"hi {name}"

print(greet())        # -> hi guest
print(greet(""))      # -> hi guest    <- "" is falsy, maybe you wanted the empty string
print(greet("ali"))   # -> hi ali

def greet2(name=None):
    if name is None:            # ...but this is precise
        name = "guest"
    return f"hi {name}"
print(greet2(""))     # -> hi
Gotcha — and/or vs &/|. and/or are boolean, lazy, and work on truthiness. &/| are bitwise, eager, and operate on values. On plain bools they look the same but have different precedence and no short-circuit.

print(True & False)        # -> False   (bitwise, but bools are ints)
print(1 & 2)               # -> 0       !! bitwise AND of 01 and 10
print(1 and 2)             # -> 2
print(True | False)        # -> True
# precedence trap: | binds TIGHTER than ==
print(False == False | True)     # -> False   parses as False == (False | True)
print((False == False) | True)   # -> True    what you probably meant
(In pandas/NumPy you must use &/| on arrays, with parentheses — and raises there.)

Gotcha — comparing to True/False explicitly.

x = 1
print(x == True)      # -> True
print(x is True)      # -> False   x is int 1, not bool True
if x: ...             # <- just do this
Linters flag == True for good reason.

Gotcha — chained comparison with in/is.

print("a" in "abc" == True)   # -> False !  parses as ("a" in "abc") and ("abc" == True)
Interview note. "What does x or y return?" separates people who memorised syntax from people who read the language reference. Follow-up: "implement a default helper that treats 0 and "" as valid values" — the answer is a None check or a unique sentinel:

_MISSING = object()          # unique sentinel, never equal to user data
def get(d, key, default=_MISSING):
    ...
4. Strings
str is an immutable sequence of Unicode code points.

Creating strings
s1 = 'single'
s2 = "double"                      # identical; pick one style per project
s3 = """multi
line"""                            # keeps the newline
s4 = 'He said "hi"'                # no escaping needed
s5 = "It's fine"
s6 = 'escaped \' quote and a \\ backslash and a \n newline and a \t tab'
s7 = r"raw\nstring"                # r prefix: backslashes are literal -> raw\nstring
s8 = f"formatted {1 + 1}"          # f-string -> 'formatted 2'
s9 = b"bytes, not str"             # bytes literal (different type!)
s10 = ("implicit "                 # adjacent literals concatenate at COMPILE time
       "concatenation")            # -> 'implicit concatenation'
print(len(s10))                    # -> 22
Raw strings are what you want for regex and Windows paths:

import re
print(re.findall(r"\d+", "a1b22"))   # -> ['1', '22']    r"" keeps \d intact
Indexing and slicing
s = "Python"
#    012345      forward index
#   -654321      negative index

print(s[0])       # -> 'P'
print(s[-1])      # -> 'n'      last character
print(s[1:4])     # -> 'yth'    [start:stop) — stop is EXCLUSIVE
print(s[:3])      # -> 'Pyt'    start defaults to 0
print(s[3:])      # -> 'hon'    stop defaults to len
print(s[:])       # -> 'Python' full copy
print(s[::2])     # -> 'Pto'    step 2
print(s[::-1])    # -> 'nohtyP' reversed
print(s[10:20])   # -> ''       out-of-range SLICES are safe (no error)
print(s[10])      # !! IndexError: string index out of range
Concatenation and repetition
print("ab" + "cd")     # -> 'abcd'
print("ab" * 3)        # -> 'ababab'
print("-" * 20)        # -> '--------------------'   handy separator
print("".join(["a", "b", "c"]))         # -> 'abc'
print(", ".join(["a", "b", "c"]))       # -> 'a, b, c'
Building a string in a loop with += is O(n²) in general. Collect into a list and join:

parts = []
for i in range(5):
    parts.append(str(i))
print("".join(parts))    # -> '01234'
Essential string methods
Every one of these returns a new string — strings are immutable.

s = "  Hello, World  "

# case
print(s.upper())            # -> '  HELLO, WORLD  '
print(s.lower())            # -> '  hello, world  '
print("hi there".title())   # -> 'Hi There'
print("hi there".capitalize())  # -> 'Hi there'
print("AbC".swapcase())     # -> 'aBc'
print("Straße".casefold())  # -> 'strasse'   aggressive lowercase for comparisons

# whitespace / trimming
print(s.strip())            # -> 'Hello, World'
print(s.lstrip(), "|")      # -> 'Hello, World  |'
print(s.rstrip(), "|")      # -> '  Hello, World|'
print("xxhixx".strip("x"))  # -> 'hi'      strips any of the CHARACTERS given
print("file.txt".removesuffix(".txt"))    # -> 'file'   (3.9+, use this not strip!)
print("pre_name".removeprefix("pre_"))    # -> 'name'

# searching
print("hello".find("l"))     # -> 2     first index, -1 if absent
print("hello".rfind("l"))    # -> 3     last index
print("hello".index("l"))    # -> 2     like find but RAISES ValueError if absent
print("hello".count("l"))    # -> 2
print("hello".startswith("he"))          # -> True
print("hello".endswith((".py", ".txt"))) # -> False   accepts a TUPLE of options
print("ell" in "hello")      # -> True   simplest membership test

# splitting and joining
print("a,b,c".split(","))          # -> ['a', 'b', 'c']
print("a b  c".split())            # -> ['a', 'b', 'c']  no-arg split collapses whitespace
print("a,b,c".split(",", 1))       # -> ['a', 'b,c']     maxsplit
print("a,b,c".rsplit(",", 1))      # -> ['a,b', 'c']     from the right
print("k=v=w".partition("="))      # -> ('k', '=', 'v=w')  always a 3-tuple
print("line1\nline2".splitlines()) # -> ['line1', 'line2']

# replacing
print("a-b-c".replace("-", "+"))       # -> 'a+b+c'
print("a-b-c".replace("-", "+", 1))    # -> 'a+b-c'   count limit

# padding / alignment
print("5".zfill(3))          # -> '005'
print("hi".ljust(5, "."))    # -> 'hi...'
print("hi".rjust(5, "."))    # -> '...hi'
print("hi".center(6, "*"))   # -> '**hi**'

# classification (all return bool; all are False for the empty string)
print("abc".isalpha(), "123".isdigit(), "a1".isalnum())   # -> True True True
print("  ".isspace(), "Hi".istitle(), "ABC".isupper())    # -> True True True
print("var_1".isidentifier())      # -> True
f-strings (preview — full coverage in Tier 2)
name, score = "Ada", 0.87561
print(f"{name} scored {score:.1%}")     # -> Ada scored 87.6%
print(f"{name!r}")                      # -> 'Ada'      !r calls repr()
print(f"{score=}")                      # -> score=0.87561   self-documenting (3.8+)
print(f"{42:>8}|")                      # -> '      42|'  right-align in 8 columns
print(f"{1234567:,}")                   # -> 1,234,567
Gotcha — strings are immutable.

s = "hello"
s[0] = "H"          # !! TypeError: 'str' object does not support item assignment
s = "H" + s[1:]     # correct: build a new string
Gotcha — strip() is not removesuffix(). strip takes a set of characters:

print("test.txt".strip(".txt"))       # -> 'es'   !!  stripped t, x, . from BOTH ends
print("test.txt".removesuffix(".txt"))# -> 'test'  correct
This is a real bug that ships to production regularly.

Gotcha — len() counts code points, not visible characters.

print(len("café"))          # -> 4
print(len("cafe\u0301"))    # -> 5   same-looking text, combining accent
print(len("👍"))            # -> 1
print(len("👨‍👩‍👧"))          # -> 5   one emoji, five code points (ZWJ sequence)
Normalise before comparing user text: unicodedata.normalize("NFC", s). Tier 2 goes deeper.

Interview note. "How would you reverse a string?" → s[::-1]. "Why is repeated += in a loop bad?" → strings are immutable, each += allocates and copies, O(n²) total; use str.join. (CPython has an in-place optimisation when the refcount is 1, but never rely on it — it vanishes the moment the string has another reference.)

5. None and its role
None is the single instance of NoneType. It means "no value here" — not zero, not empty.

x = None
print(x)                 # -> None
print(type(None))        # -> <class 'NoneType'>
print(None is None)      # -> True
print(bool(None))        # -> False

# It's a SINGLETON: there is exactly one None object in the whole process.
print(None is None)      # -> True, always
Where None shows up
# 1. Functions with no explicit return
def f():
    pass
print(f())               # -> None

# 2. Mutating methods return None (they changed the object in place)
xs = [3, 1, 2]
print(xs.sort())         # -> None      <- classic bug source
xs.sort()
print(xs)                # -> [1, 2, 3]
print(sorted([3, 1, 2])) # -> [1, 2, 3] sorted() RETURNS a new list

# 3. Default "nothing was supplied" marker
def connect(timeout=None):
    if timeout is None:
        timeout = 30      # compute a real default at call time
    return timeout

# 4. Safe dict lookup
config = {"host": "localhost"}
print(config.get("port"))        # -> None
print(config.get("port", 8080))  # -> 8080
Always test with is / is not
x = None
if x is None: ...        # correct
if x is not None: ...    # correct
if x == None: ...        # works, but slower and overridable by __eq__; linters flag it
if not x: ...            # WRONG when 0, "", [] are valid values
Why it matters:

class Weird:
    def __eq__(self, other): return True

print(Weird() == None)     # -> True   !! __eq__ lied
print(Weird() is None)     # -> False  identity cannot be faked
Gotcha — the mutable default argument. The most famous Python trap, and the reason None is used as a default everywhere:

def add(item, bucket=[]):        # BROKEN: the list is created ONCE, at def time
    bucket.append(item)
    return bucket
print(add(1))     # -> [1]
print(add(2))     # -> [1, 2]    !! shared across calls

def add(item, bucket=None):      # CORRECT
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
print(add(1))     # -> [1]
print(add(2))     # -> [2]
Gotcha — forgetting return.

def double(x):
    x * 2            # computed and thrown away
print(double(5))     # -> None
Interview note. Two near-certain questions: (1) "Why is None and not == None?" — None is a singleton, is is an identity check that can't be overridden and is faster; (2) "Explain the mutable default argument." Bonus points for naming the why: default values are evaluated once when the def statement executes and stored on the function object at func.__defaults__.

def f(a=[]): pass
print(f.__defaults__)   # -> ([],)   the actual shared object
6. Type conversion / casting
Python does not auto-convert between unrelated types. You convert explicitly by calling the type.

# to int
print(int("42"))         # -> 42
print(int("  42  "))     # -> 42     surrounding whitespace is fine
print(int("0x1f", 16))   # -> 31     explicit base
print(int(3.99))         # -> 3      TRUNCATES toward zero, does not round
print(int(-3.99))        # -> -3
print(int(True))         # -> 1
print(int("3.0"))        # !! ValueError: invalid literal for int() with base 10: '3.0'
print(int(float("3.0"))) # -> 3      two-step for numeric strings with a decimal point

# to float
print(float("3.14"))     # -> 3.14
print(float(7))          # -> 7.0
print(float("inf"))      # -> inf
print(float("1e-3"))     # -> 0.001

# to str
print(str(42))           # -> '42'
print(str([1, 2]))       # -> '[1, 2]'
print(str(None))         # -> 'None'

# to bool
print(bool(0), bool(""), bool([]))       # -> False False False
print(bool("False"))     # -> True   !! any non-empty string is truthy

# to the container types
print(list("abc"))               # -> ['a', 'b', 'c']
print(tuple([1, 2]))             # -> (1, 2)
print(set([1, 1, 2]))            # -> {1, 2}
print(dict([("a", 1), ("b", 2)]))# -> {'a': 1, 'b': 2}
print(list({"a": 1}))            # -> ['a']   iterating a dict gives KEYS
print(list({"a": 1}.items()))    # -> [('a', 1)]

# to bytes / from bytes
print("héllo".encode("utf-8"))          # -> b'h\xc3\xa9llo'
print(b"h\xc3\xa9llo".decode("utf-8"))  # -> 'héllo'
Implicit conversion that does happen: numeric promotion
print(1 + 2.0)          # -> 3.0     int promoted to float
print(type(1 + 2.0))    # -> <class 'float'>
print(True + 1.5)       # -> 2.5     bool -> int -> float
print((1 + 2j) + 3)     # -> (4+2j)
# The ladder: bool -> int -> float -> complex
Checking types
x = 5
print(type(x) is int)         # -> True   exact type, no subclasses
print(isinstance(x, int))     # -> True   type OR subclass — prefer this
print(isinstance(x, (int, float)))   # -> True   accepts a tuple
print(isinstance(True, int))  # -> True   because bool subclasses int

# Duck typing is usually better than type checking:
def total(values):
    return sum(values)        # works for any iterable of numbers

# When you must check "is it a sequence / iterable":
from collections.abc import Iterable, Sequence, Mapping
print(isinstance([1], Iterable), isinstance("s", Sequence), isinstance({}, Mapping))
# -> True True True
Safe conversion pattern
def to_int(value, default=None):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

print(to_int("42"))      # -> 42
print(to_int("abc"))     # -> None
print(to_int(None, 0))   # -> 0
Gotcha — int() truncates, it does not round. int(2.9) == 2, int(-2.9) == -2. For rounding use round(); for floor use math.floor() (they differ on negatives).

Gotcha — bool("False") is True. Parsing config strings needs an explicit map:

def parse_bool(s):
    return s.strip().lower() in {"1", "true", "yes", "on"}
print(parse_bool("False"))   # -> False
Gotcha — str() vs repr(). str() is for humans, repr() is for developers and should ideally be valid Python.

import datetime as dt
d = dt.date(2026, 1, 1)
print(str(d))    # -> 2026-01-01
print(repr(d))   # -> datetime.date(2026, 1, 1)
print(str("a"), repr("a"))   # -> a 'a'
Interview note. "How do you check a type in Python?" — the answer they want is "usually you don't; you use duck typing / protocols; when you must, isinstance, not type() ==, because isinstance respects subclasses and ABC registration." Mention isinstance(True, int) is True as the classic edge case.

7. Comments and docstrings
Comments
# A full-line comment. Explain WHY, not WHAT.

x = x + 1            # inline comment: two spaces before #, one space after

# BAD:  x = x + 1    # add one to x        <- restates the code
# GOOD: x = x + 1    # compensate for the exclusive upper bound of range()

# Python has no /* block comment */ syntax.
# Editors comment multiple lines by prefixing each with #.

"""
A bare string literal like this is NOT a comment — it is an expression statement
that creates and discards a string. Sometimes used to disable a block, but it
still gets compiled. Prefer # for commenting out code.
"""
Docstrings
A docstring is a string literal as the first statement of a module, function, class, or method. It becomes __doc__ and is what help() shows.

def clamp(value, low, high):
    """Return value constrained to the inclusive range [low, high].

    Args:
        value: The number to clamp.
        low: Lower bound, inclusive.
        high: Upper bound, inclusive.

    Returns:
        low if value < low, high if value > high, otherwise value.

    Raises:
        ValueError: If low > high.

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-1, 0, 10)
        0
    """
    if low > high:
        raise ValueError("low must not exceed high")
    return max(low, min(value, high))

print(clamp.__doc__.splitlines()[0])
# -> Return value constrained to the inclusive range [low, high].
help(clamp)      # renders the full docstring
Module and class docstrings:

"""Utilities for geometry.

This module-level docstring must be the very first statement in the file,
before any imports.
"""

class Circle:
    """A circle in the plane.

    Attributes:
        radius: Distance from centre to edge, in metres.
    """

    def area(self):
        """Return the area in square metres."""
        ...
PEP 257 conventions
Use """triple double quotes""" even for one-liners.
One-liners: fit on one line, end with a period, no blank line before or after.
Multi-line: summary line, blank line, details, closing """ on its own line.
Write it as a command ("Return the area"), not a description ("Returns the area") — though Google-style docs commonly use the latter; be consistent with your project.
Docstrings are testable
# save as clamp.py, then run:  python -m doctest clamp.py -v
# Any `>>>` example in a docstring is executed and its output compared.
Popular docstring styles — pick one per project:

Style	Looks like	Used by
Google	Args: / Returns:	most modern projects, very readable
NumPy	Parameters\n----------	scientific stack
reST / Sphinx	:param x: / :returns:	older Sphinx projects
Gotcha — a docstring must be the first statement. This is not a docstring:

def f():
    x = 1
    """not a docstring"""     # just a discarded string; f.__doc__ is None
Gotcha — python -O does not strip docstrings (that was -OO), and -OO will break any library that reads __doc__ at runtime (some CLI frameworks do).

Gotcha — backslashes in docstrings. A docstring containing \n or a Windows path needs a raw docstring: r"""Handles C:\new\table."""

Interview note. Low-frequency as a direct question, but code-review-visible. The senior signal is knowing that docstrings are runtime objects (__doc__), that help(), Sphinx, IDE tooltips and doctest all read them, and that comments should carry the rationale the code cannot.