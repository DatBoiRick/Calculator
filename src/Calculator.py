from CsvReader import CsvReader


def add(a, b):
    a = int(a)
    b = int(b)
    c = b + a
    return c


def subtract(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def square(a, b):
    return a ** b


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a, b)
        return self.result

    def square(self, a, b):
        self.result = square(a, b)
        return self.result

    def square_root(self, x, ):
        self.result = (x ** .5)
        return self.result
