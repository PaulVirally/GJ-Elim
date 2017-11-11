class Matrix:

    def __init__(self, data=[]):
        self.data = data

    def fill(self, data):
        self.data = data

    def __str__(self):
        # ┛ ┗ ┓ ┏ ┃ │
        #
        # ┏            ̩   ┓
        # ┃ 1 0 0 0 0 │ 1 ┃
        # ┃ 0 1 0 0 0 │ 2 ┃
        # ┃ 0 0 1 0 0 │ 3 ┃
        # ┃ 0 0 0 1 0 │ 4 ┃
        # ┃ 0 0 0 0 1 │ 5 ┃
        # ┗            ̍   ┛
        widths = []
        for j in range(len(self.data[0])):
            widths.append(max(len('{:g}'.format(self.data[i][j])) for i in range(len(self.data))) + 2) # +2 For padding

        s = ''
        for row in self.data:
            s += '┃ '
            for i in range(len(row)):
                s += '{:g}'.format(row[i]).center(widths[i])
                if i == len(row) - 2:
                    s += '│'
            s += ' ┃\n'
        
        size = max(len(row) for row in s.split('\n')) - 2
        s =  '┏' + ' '*size + '┓\n' + s
        s += '┗' + ' '*size + '┛'
        # s += '┗' + ' '*(size-widths[-1]-2) + '│' + ' '*(widths[-1]+1) + '┛'
        return s

    def get_row(self, n):
        return self.data[n]

    def get_col(self, n):
        return [x[n] for x in self.data]

    def _get_mul_row(self, row, factor):
        return [self.data[row][x] * factor for x in range(len(self.data[row]))]

    def mul_row(self, row, factor):
        self.data[row] = self._get_mul_row(row, factor)

    def _get_div_row(self, row, factor):
        return [self.data[row][x] / factor for x in range(len(self.data[row]))]

    def div_row(self, row, factor):
        self.data[row] = self._get_div_row(row, factor)

    def add_rows(self, row, other_row, factor):
        # pseudo: self.data[row] += factor * self.data[other_row]
        self.data[row] = [self.data[row][x] + self.data[other_row][x] * factor for x in range(len(self.data[row]))]

    def sub_rows(self, row, other_row, factor):
        # pseudo: self.data[row] -= factor * self.data[other_row]
        self.data[row] = [self.data[row][x] - self.data[other_row][x] * factor for x in range(len(self.data[row]))]

    def solve(self):
        # Get to REF
        for i in range(len(self.data)):
            # Do we have a 1?
            if self.data[i][i] != 1:
                # Find the next 1
                self.div_row(i, self.data[i][i])
                print(self)

            # Do we have 0s under that 1?
            below = [self.data[i+x][i] for x in range(1, len(self.data) - i)]
            # Find the next 0 to place
            for idx in range(1, len(below)+1):
                next_row = i + idx
                if self.data[next_row][i] != 0:
                    self.sub_rows(next_row, i, self.data[next_row][i])
                    print(self)

        # # Get to RREF
        # for i in range(len(self.data)):
        #     if not all([x == 0 for x in self.data[i][:i+1]]):
        #         # Find the next 0
        #         return