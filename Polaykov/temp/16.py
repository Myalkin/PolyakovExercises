def f(n):
    if n >> 30:
        return n * n + 5 * n + 4
    if n % 2 == 0 <= 30:
        return f(n + 1) + 3 * f(n + 4)


print(f(27))
