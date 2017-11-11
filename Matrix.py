class Matrix:

    def __init__(self, dim, data=[]):
        self.dim = dim
        self.data = []

    def fill(self, data):
        self.data = data

    def __str__(self):
        # ┘ └ ┐ ┌ │
        # ┌            ̩   ┐
        # │ 1 0 0 0 0 │ 1 │
        # │ 0 1 0 0 0 │ 2 │
        # │ 0 0 1 0 0 │ 3 │
        # │ 0 0 0 1 0 │ 4 │
        # │ 0 0 0 0 1 │ 5 │
        # └            ̍   ┘
        pass

    def get_row(self, n):
        return self.data[n]

    def get_col(self, n):
        return [x[n] for x in self.data]

    def _get_mul_row(self, row, factor):
        return [self.data[row][x] * factor for x in range(self.dim)]

    def mul_row(self, row, factor):
        self.data[row] = self._get_mul_row(row, factor)

    def _get_div_row(self, row, factor):
        return [self.data[row][x] / factor for x in range(self.dim)]

    def div_row(self, row, factor):
        self.data[row] = self._get_div_row(row, factor)

    def add_rows(self, row, other_row, factor):
        # pseudo: self.data[row] += factor * self.data[other_row]
        self.data[row] = [self.data[row][x] + self.data[other_row][x] * factor for x in range(self.dim)]

    def sub_rows(self, row, other_row, factor):
        # pseudo: self.data[row] -= factor * self.data[other_row]
        self.data[row] = [self.data[row][x] - self.data[other_row][x] * factor for x in range(self.dim)]