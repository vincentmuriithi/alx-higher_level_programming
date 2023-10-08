#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    signs = ["+", "-", "*", "/"]

    r_add = add(a, b)
    r_sub = sub(a, b)
    r_mul = mul(a, b)
    r_div = div(a, b)

    ans = [r_add, r_sub, r_mul, r_div]

    for k in range(len(signs)):
        print("{} {} {} = {}".format(a,signs[k], b, ans[k]))
