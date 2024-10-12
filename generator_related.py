import operator


def fib(n):
    """Fibonacci generator"""
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


def pascal_triangle(n):
    """Pascal triangle generator"""
    cur = [1]
    for _ in range(n):
        yield cur
        a = [0] + cur
        b = cur + [0]
        cur = list(map(operator.add, a, b))


def main() -> None:
    fib_gen = fib(10)

    while True:
        try:
            print(next(fib_gen))
        except StopIteration:
            break

    pasc_gen = pascal_triangle(10)
    while True:
        try:
            print(next(pasc_gen))
        except StopIteration:
            break


main()
