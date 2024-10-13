def multiplication_generator(x):
    for i in range(1, 10):
        yield f"{i} x {x} = {i * x}"


def test():
    gen = multiplication_generator(2)
    while True:
        try:
            print(next(gen))
        except StopIteration:
            break


test()
