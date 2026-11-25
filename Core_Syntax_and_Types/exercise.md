**1. Aliasing. Without running it, predict the output, then check:**

a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(5)
print(a, b, c)


**2. Floor division. Write ceil_div(a, b) that returns the ceiling of a / b for positive integers, using only integer arithmetic (no math, no floats).**


**3. Truthiness. Write first_truthy(*values) returning the first truthy argument, or None if there is none. Do it in one line.**

**4. Safe default. Write coalesce(*values) that returns the first argument that is not None (so 0 and "" are valid results).**


**5. String surgery. Given path = "/home/user/report.final.txt", produce ("report.final", ".txt") — the stem and the extension — using only str methods.**


**6. Rounding. Explain, with code, why round(2.675, 2) is 2.67, and show two ways to get 2.68.**


**7. Casting. Write parse_number(s) that returns an int if the string is an integer, a float if it's a float, and raises ValueError otherwise. parse_number("3") → 3 (an int), parse_number("3.0") → 3.0 (a float).**


**8. Docstring. Write a fully documented fizzbuzz(n) with a Google-style docstring including two doctest examples, and make python -m doctest pass on it.**

