class Add:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Add(self.number + other)

    def __call__(self, other):
        return Add(self.number + other)

    def __str__(self):
        return f"{self.number}"


def test():
    add_two = Add(2)
    print(add_two)
    print(add_two + 5)
    print(add_two(3))
    print(add_two(3)(5))
    print(Add(1)(2))
    print(Add(1)(2)(3))
    print(Add(1)(2)(3)(4))
    print(Add(1)(2)(3)(4)(5))


test()
