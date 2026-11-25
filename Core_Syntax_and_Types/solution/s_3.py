# Truthiness. Write first_truthy(*values) returning the first truthy argument, or None if there is none. Do it in one line.

# values = (0, "", None, 42, 100)

# for v in values:
#     if v:
#         print(v)

def first_truthy(*values):
    print(next((v for v in values if v),None))

first_truthy(0, "", None,6,42,102,1)