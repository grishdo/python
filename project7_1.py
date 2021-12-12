class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print("{:4d}".format(i), end="")
            print()
        return ''

    def __add__(self, second_matrix):
        new_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        new_matrix = Matrix(new_list)
        for i in range(len(self.my_list)):
            for j in range(len(second_matrix.my_list[i])):
                new_matrix.my_list[i][j] = self.my_list[i][j] + second_matrix.my_list[i][j]
        return Matrix.__str__(new_matrix)


matrix = Matrix([[-4, 1, 0], [-2, 14, 1], [5, 1, -2], [0, 1, 3]])
second_matrix = Matrix([[2, 1, 2], [-1, 0, 8], [-1, 3, -2], [1, 2, 4]])
print(matrix + second_matrix)

