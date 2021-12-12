class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num > 0 and other.num > 0:
            return self.num - other.num
        else:
            print('Число каждой клетки должно быть больше 0')

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return round(self.num / other.num)

    def make_order(self, row):
        result = ''
        for i in range(int(self.num / row)):
            result += '*' * row + '\n'
        result += '*' * (self.num % row) + '\n'
        return result


c = Cell(10)
c2 = Cell(3)
print(c / c2)
print(c.make_order(3))

