class ComplexNumber:
    def __init__(self, complex_1):
        self.complex_1 = complex_1

    def __add__(self, other):
        real = self.complex_1.real + other.complex_1.real
        real = float_in_int(real)
        imag = self.complex_1.imag + other.complex_1.imag
        imag = float_in_int(imag)
        return f'Действительная часть: {real} + ' \
               f''f'Мнимая часть: {imag}'

    def __mul__(self, other):
        real = self.complex_1.real * other.complex_1.real - self.complex_1.imag * other.complex_1.imag
        real = float_in_int(real)
        imag = self.complex_1.real * other.complex_1.imag + self.complex_1.imag * other.complex_1.real
        imag = float_in_int(imag)
        return f'Действительная часть: {real} + ' \
               f''f'Мнимая часть: {imag}'


def float_in_int(num):
    return int(num) if num == int(num) else num


c_1 = ComplexNumber(1 + 2j)
c_2 = ComplexNumber(2 + 3j)
print(c_1 + c_2)
print(c_1 * c_2)
