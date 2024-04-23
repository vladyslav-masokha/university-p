class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def add_element(self, row, col, value):
        self.data[row][col] = value

    def sum(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid matrix dimensions for multiplication")
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum
        return result

    def is_symmetric(self):
        if self.rows != self.cols:
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False
        return True

    def rotate_right(self):
        n = self.rows
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                offset = i - first
                top = self.data[first][first + offset]

                self.data[first][first + offset] = self.data[last - offset][first]
                self.data[last - offset][first] = self.data[last][last - offset]
                self.data[last][last - offset] = self.data[first + offset][last]
                self.data[first + offset][last] = top

    def flatten(self):
        return [val for row in self.data for val in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0])
        matrix = Matrix(rows, cols)
        for i in range(rows):
            for j in range(cols):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def diagonal(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square")
        return [self.data[i][i] for i in range(self.rows)]