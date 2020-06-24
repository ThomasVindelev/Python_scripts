from math import factorial
import sys


class Shop:

    def __init__(self, name, category, employees):
        self.name = name
        self.category = category
        self.employees = employees
        self.products = []

    def __add__(self, other):
        self.products.append(other)

    def __getitem__(self, item):
        return self.products[item]

    def __delitem__(self, key):
        del self.products[key]

    def __str__(self):
        return


# ['__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
# 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees',
# 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
# 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf',
# 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma',
# 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow',
# 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

