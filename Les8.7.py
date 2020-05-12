class ComplexNumber:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return ComplexNumber(self.num1 + other.num1)

    def __mul__(self, other):
        return ComplexNumber(self.num1 * other.num1,)

    def __str__(self):
        return f"Результат {self.num1}"


number1 = ComplexNumber(complex(1, 2))
number2 = ComplexNumber(complex(3, 4))
print(number1 + number2)
print(number1 * number2)
