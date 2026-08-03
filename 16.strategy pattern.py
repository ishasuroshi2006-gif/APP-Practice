class Add:
    def execute(self, a, b):
        return a + b

class Multiply:
    def execute(self, a, b):
        return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)

calc = Calculator(Add())
print("Addition:", calc.calculate(10, 5))

calc = Calculator(Multiply())
print("Multiplication:", calc.calculate(10, 5))
