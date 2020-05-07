class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix])
        return self.b

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                my_sum = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(my_sum)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(matrix1)
print(matrix2)
print(matrix3)
print(matrix1 + matrix2 + matrix3)